import requests
import codecs
from bs4 import BeautifulSoup as bs

# Hack time
headers = {'User-Agent': 'Mozilla/5.0 (Windows WorkS 13.37228; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*,q=0.8'
           }

url = 'https://rostov.hh.ru/search/vacancy?text=python&from=suggest_post&fromSearchLine=true&area=76'
resp = requests.get(url, headers=headers)
jobs = []
errors = []
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
            content_part_2 = div_two_span.find('div', attrs={'class': 'bloko-text bloko-text_no-top-indent'}).text
            content = content_part_1 + content_part_2
            company = 'No name'
            cname_1 = div.find('div', attrs={'class': 'vacancy-serp-item__meta-info-company'})
            if cname_1:
                company = cname_1.a.text
            jobs.append({'title': title.text,
                         'url': href,
                         'description': content,
                         'company': company})
    else:
        errors.append({'url': url, 'title': 'Div does not exists'})
else:
    errors.append({'url': url, 'title': 'Page do not response'})

h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()
