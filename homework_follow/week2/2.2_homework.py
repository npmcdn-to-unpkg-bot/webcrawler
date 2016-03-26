import requests
from bs4 import BeautifulSoup
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
mobile_number_list = tongcheng['mobile_number']


def page_mobile_info(page):
    for i in range(1, page+1):
        url = 'http://xm.58.com/shoujihao/1/pn{}/'.format(page)
        web_data = requests.get(url)
        soup = BeautifulSoup(web_data.text, 'lxml')
        titles = soup.select('strong.number')
        # print(titles)
        links = soup.select('a.t')
        # print(links)
        prices = soup.select('b.price')
        # print(prices)
        for title, price, link in zip(titles, prices, links):
            data = {
                'title': title.get_text(),
                'price': int(price.get_text()[:-1]),
                # 'price': int(price.get_text().replace('元',''),
                'link': link.get('href'),
            }
            # print(data)
            # mobile_number_list.drop()
            # mobile_number_list.insert_one(data)

# page_mobile_info(1)
for item in mobile_number_list.find({'price': {'$gt': 10000}}):
    print(item)
    # if item['price'] == '面议':
    #     print(item)

