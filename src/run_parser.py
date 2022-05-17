import asyncio
import os
import django
from django.contrib.auth import get_user_model
from django.db import DatabaseError

# Связка джанго со скриптом
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'work_search.settings')
django.setup()

from works_core.parser import *
from works_core.models import *

User = get_user_model()

# Адреса и их функции-парсеры
parsers = (
    (hh_ru, 'hh_ru'),
    (rabota_ru, 'rabota_ru'),
    (habr_career, 'habr_career')
)

jobs, errors = [], []


def get_settings():
    user_qs = User.objects.filter(is_mailing=True).values()
    settings_conf = set((q['city_id'], q['specialization_id']) for q in user_qs)
    return settings_conf


def get_urls(_settings):
    url_qs = Url.objects.all().values()
    url_dict = {(q['city_id'], q['specialization_id']): q['url_data'] for q in url_qs}
    urls = []
    for pair in _settings:
        tmp = {}
        tmp['city'] = pair[0]
        tmp['specialization'] = pair[1]
        tmp['url_data'] = url_dict[pair]
        urls.append(tmp)
    return urls


settings = get_settings()
url_list = get_urls(settings)


async def main(value):
    func, url, city, specialization = value
    job, err = await loop.run_in_executor(None, func, url, city, specialization)
    errors.extend(err)
    jobs.extend(job)


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

tmp_tasks = [(func, data['url_data'][key], data['city'], data['specialization'])
             for data in url_list
             for func, key in parsers]
tasks = asyncio.wait([loop.create_task(main(f)) for f in tmp_tasks])

loop.run_until_complete(tasks)
loop.close()

# Запись вакансий в БД
for job in jobs:
    vacancy = Vacancy(**job)
    try:
        vacancy.save()
    except DatabaseError:
        pass

if errors:
    er = Error(data=errors).save()
