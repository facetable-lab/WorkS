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
    (hh_ru, 'https://rostov.hh.ru/search/vacancy?text=python&from=suggest_post&fromSearchLine=true&area=76'),
    (rabota_ru, 'https://rostov.rabota.ru/vacancy/?query=python&sort=relevance'),
    (habr_career, 'https://career.habr.com/vacancies?city_id=726&q=python&type=all')
)


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


q = get_settings()
u = get_urls(q)

city = City.objects.filter(slug='rostov-na-donu').first()
specialization = Specialization.objects.filter(slug='python').first()

# Проходимся по адресам их функциями, сохраняя ошибки
jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

# Запись вакансий в БД
for job in jobs:
    vacancy = Vacancy(**job, city=city, specialization=specialization)
    try:
        vacancy.save()
    except DatabaseError:
        pass

if errors:
    er = Error(data=errors).save()
