from bs4 import BeautifulSoup
import requests
import pymongo
from random import choice
import time

myDB = pymongo.MongoClient('localhost', 27017)
ganji = myDB['ganji']
item_url = ganji['item_url']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
}

proxies_list = [
    'http://117.177.250.151:8081',
    'http://111.85.219.250:3129',
    'http://122.70.183.138:8118',
                ]

cookies = dict(cookies_are='ganji_uuid=4195054900852911468988; ganji_xuuid=d47ef0b3-67b3-4644-eb6d-ecfe63e02a9c.1459357350596; citydomain=xm; statistics_clientid=me; GANJISESSID=0e1e2107f36df1c9039dabe47f0759b8; hotPriceTip=1; crawler_uuid=145943457096518146908945; STA_DS=1; lg=1; __utma=32156897.984823410.1459357350.1459432148.1459434589.3; __utmb=32156897.6.10.1459434589; __utmc=32156897; __utmz=32156897.1459434589.3.3.utmcsr=ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/sorry/confirm.php; _gl_tracker=%7B%22ca_source%22%3A%22www.baidu.com%22%2C%22ca_name%22%3A%22se%22%2C%22ca_kw%22%3A%22%25E8%25B5%25B6%25E9%259B%2586%25E7%25BD%2591%7Cutf8%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A78547241241%7D')
proxies = {'http': choice(proxies_list)}


def get_item_url(channel, page, who_sells='o'):
    list_view = '{}{}{}'.format(channel, who_sells, str(page))
    web_data = requests.get(list_view, headers=headers, proxies=proxies, cookies=cookies, timeout=10)
    time.sleep(5)
    if web_data.status_code == 404:
        pass
    else:
        soup = BeautifulSoup(web_data.text, 'lxml')
        items = soup.select('dd.feature li > a')
        for item in items:
            url = item.get('href')
            print(url)
            item_url.insert_one({'item_url': url})
