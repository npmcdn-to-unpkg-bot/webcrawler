import requests
from bs4 import BeautifulSoup
import re
import pymongo

client = pymongo.MongoClient('localhost', 27017)
proxy = client['proxy']
proxy1 = proxy['proxy1']

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
}

proxies = {
    'http': 'http://107.151.136.210:80'
}
# web_data = requests.get('http://www.youdaili.net/', headers=headers)
# soup = BeautifulSoup(web_data.text, 'lxml')
# today_proxy_link = soup.select('div.zxzx ul > li > a')[0].get('href')
#
# proxies_page = requests.get(today_proxy_link, headers=headers, proxies=proxies)
# soup = BeautifulSoup(proxies_page.text, 'lxml')
# p_info = soup.select('.content span')[0].text
# p2 = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,4}')
# new_proxies = p2.findall(p_info)
# for i in new_proxies:
#     proxy1.insert_one({'http': 'http://'+i})
