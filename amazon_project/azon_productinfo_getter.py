# Get search bar result
import requests
from bs4 import BeautifulSoup
import pymongo

azdb = pymongo.MongoClient('localhost', 27017)
az = azdb['az']
az_asin = az['az_asin']

headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) \
        AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
    }


def get_page(p):
    url = 'http://www.amazon.com/gp/aw/s/\
    ref=is_pn_1?rh=i%3Aaps%2Ck%3Awrap+bracelet&page={}&keywords=pendant+necklace'.format(p)
    return url


def get_asin(url):
    web_data = requests.get(url, headers=headers)
    # print(web_data.text)
    soup = BeautifulSoup(web_data.text, 'lxml')
    asins = soup.select('#resultItems li > a')
    # asin_list = []
    for i in asins:
        asin = i.get('data-asin')
        if asin not in list(i['asin'] for i in az_asin.find()):
            az_asin.insert_one({'asin': asin})
            print(asin)
        # asin_list.append(i.get('data-asin'))
    # return asin_list



if __name__ == '__main__':
    pass
    # for p in range(1, 10):
    #     get_asin(get_page(p))
    # get_asin('http://www.amazon.com/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Asaae+bracelet&page=2&keywords=saae+bracelet&ie=UTF8&qid=1460537937')