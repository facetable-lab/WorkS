import requests
import codecs
from bs4 import BeautifulSoup as bs
from random import randint

__all__ = ('hh_ru', 'rabota_ru', 'habr_career')

# Hack time
headers = [{'User-Agent': 'Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*,q=0.8'
            },
           {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*,q=0.8'
            },
           {'User-Agent': 'Chrome/51.0.2704.103 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*,q=0.8'
            },
           {'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*,q=0.8'
            },
           ]


def hh_ru(url, city=None, specialization=None):
    jobs = []
    errors = []
    if url:
        resp = requests.get(url, headers=headers[randint(0, len(headers) - 1)])
        if resp.status_code == 200:
            soup = bs(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'vacancy-serp-content'})  # class_={"class": "style"}
            if main_div:
                div_list = main_div.find_all('div', attrs={'class': 'vacancy-serp-item'})
                for div in div_list:
                    title = div.find('h3')
                    href = title.a['href']
                    div_two_span = div.find('div', attrs={'class': 'g-user-content'})
                    content_part_1 = div_two_span.find('div', attrs={'class': 'bloko-text'}).text
                    content_part_2 = div_two_span.find('div',
                                                       attrs={'class': 'bloko-text bloko-text_no-top-indent'}).text
                    content = content_part_1 + content_part_2
                    company = 'No name'
                    cname_1 = div.find('div', attrs={'class': 'vacancy-serp-item__meta-info-company'})
                    if cname_1:
                        company = cname_1.a.text
                    jobs.append({'title': title.text,
                                 'url': href,
                                 'description': content,
                                 'company': company,
                                 'city_id': city,
                                 'specialization_id': specialization})
            else:
                errors.append({'url': url, 'title': 'Div does not exists'})
        else:
            errors.append({'url': url, 'title': 'Page do not response'})

    return jobs, errors


def rabota_ru(url, city=None, specialization=None):
    domain = 'https://rostov.rabota.ru'
    jobs = []
    errors = []
    if url:
        resp = requests.get(url, headers=headers[randint(0, len(headers) - 1)])
        if resp.status_code == 200:
            soup = bs(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'infinity-scroll r-serp__infinity-list'})
            if main_div:
                article_list = main_div.find_all('article', attrs={'class': 'vacancy-preview-card'})
                for div in article_list:
                    card_div = div.find('div', attrs={'class': 'vacancy-preview-card__top'})
                    if card_div:
                        title = card_div.find('h3', attrs={'class': 'vacancy-preview-card__title'})
                        href = domain + title.a['href']
                        company = 'No name'
                        cname_1 = card_div.find('span', attrs={'class': 'vacancy-preview-card__company-name'})
                        if cname_1:
                            company = cname_1.text

                        content = card_div.find('div', attrs={'class': 'vacancy-preview-card__short-description'}).text

                        jobs.append({'title': title.text.replace('\n            ', ''),
                                     'url': href,
                                     'description': content,
                                     'company': company,
                                     'city_id': city,
                                     'specialization_id': specialization})
            else:
                errors.append({'url': url, 'title': 'Div does not exists'})
        else:
            errors.append({'url': url, 'title': 'Page is empty'})

    return jobs, errors


def habr_career(url, city=None, specialization=None):
    domain = 'https://career.habr.com/'
    jobs = []
    errors = []
    if url:
        resp = requests.get(url, headers=headers[randint(0, len(headers) - 1)])
        if resp.status_code == 200:
            soup = bs(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'section-group section-group--gap-medium'})
            if main_div:
                div_list = main_div.find_all('div', attrs={'class': 'vacancy-card__info'})
                for div in div_list:
                    company = 'No name'
                    cname_1 = div.find('div', attrs={'class': 'vacancy-card__company-title'})
                    if cname_1:
                        company = cname_1.a.text
                    title = div.find('div', attrs={'class': 'vacancy-card__title'}).a
                    href = domain + title['href']
                    content = div.find('div', attrs={'class': 'vacancy-card__skills'}).text

                    jobs.append({'title': title.text,
                                 'url': href,
                                 'description': content,
                                 'company': company,
                                 'city_id': city,
                                 'specialization_id': specialization})
            else:
                errors.append({'url': url, 'title': 'Div does not exists'})
        else:
            errors.append({'url': url, 'title': 'Page do not response'})

    return jobs, errors


if __name__ == '__main__':
    # HH url = 'https://rostov.hh.ru/search/vacancy?text=python&from=suggest_post&fromSearchLine=true&area=76'
    url = 'https://rostov.rabota.ru/vacancy/?query=python&sort=relevance'
    # url = 'https://career.habr.com/vacancies?city_id=726&q=python&type=all'
    jobs, errors = rabota_ru(url)
    h = codecs.open('work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()
