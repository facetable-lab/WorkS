import os
import django
from django.db import DatabaseError

# Связка джанго со скриптом
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'work_search.settings')
django.setup()

from works_core.parser import *
from works_core.models import *

# Адреса и их функции-парсеры
parsers = (
    (hh_ru, 'https://rostov.hh.ru/search/vacancy?text=python&from=suggest_post&fromSearchLine=true&area=76'),
    (rabota_ru, 'https://rostov.rabota.ru/vacancy/?query=python&sort=relevance'),
    (habr_career, 'https://career.habr.com/vacancies?q=python&l=1&type=all')
)

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
