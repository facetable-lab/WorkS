import codecs

from works_core.parser import *

parsers = (
    (hh_ru, 'https://rostov.hh.ru/search/vacancy?text=python&from=suggest_post&fromSearchLine=true&area=76'),
    (rabota_ru, 'https://rostov.rabota.ru/vacancy/?query=python&sort=relevance'),
    (habr_career, 'https://career.habr.com/vacancies?q=python&l=1&type=all')
)

jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()
