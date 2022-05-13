import codecs
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'work_search.settings')
django.setup()

from works_core.parser import *
from works_core.models import Vacancy, Specialization, City

parsers = (
    (hh_ru, 'https://rostov.hh.ru/search/vacancy?text=python&from=suggest_post&fromSearchLine=true&area=76'),
    (rabota_ru, 'https://rostov.rabota.ru/vacancy/?query=python&sort=relevance'),
    (habr_career, 'https://career.habr.com/vacancies?q=python&l=1&type=all')
)

city = City.objects.filter(slug='rostov-na-donu')

jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()
