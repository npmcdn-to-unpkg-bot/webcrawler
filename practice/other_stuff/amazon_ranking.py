import requests
from random import choice
import time
from bs4 import BeautifulSoup
from get_proxy import proxy1
from multiprocessing import Pool

headers_list = [{'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}, {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)\
AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/\
27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36'}, {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'}, {'user-agent': 'Mozilla/5.0\
(Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0'}, {'user-agent': 'Mozilla/5.0 (Windows\
NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'}]

url = 'http://www.amazon.com/Romantic-Time-Butterfly-Zirconia-Earrings/dp/B011BJ0ZK8/' \
      'ref=sr_1_1?ie=UTF8&keywords=butterfly+stud+earrings'

proxy_list = []
for i in proxy1.find():
    proxy_list.append(i['http'])


def visit_page(p):
    j = 0
    proxies = {
        'http': choice(p)
    }
    while True:
        try:
            s = requests.Session()
            web_data = s.get(url, headers=choice(headers_list), proxies=proxies)
            soup = BeautifulSoup(web_data.text, 'lxml')
            time.sleep(1)
            price = soup.select('#priceblock_ourprice')[0]
            j += 1
            print(str(j) + ' ' + price.text)
        except ConnectionError as err:
            pass
        except ValueError as err:
            pass


if __name__ == '__main__':
    pool = Pool()
    pool.map(visit_page, proxy_list)


