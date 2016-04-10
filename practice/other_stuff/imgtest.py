import requests
from bs4 import BeautifulSoup
import re
import json

headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
url = 'http://m.topit.me/mt/?method=uranus.items.get&appVersion=502&offset=0'
cookie = {'Cookie':'PHPSESSID=5hk8a0t94nsnq340e23dkfhi31; request_url=%2F; is_click=1; __utmt=1; Hm_lvt_5256b9d21d9d68644fca1a0db29ba277=1460300799; Hm_lpvt_5256b9d21d9d68644fca1a0db29ba277=1460300804; __utma=137188917.543652147.1460300799.1460300799.1460300799.1; __utmb=137188917.2.10.1460300799; __utmc=137188917; __utmz=137188917.1460300799.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'}
web_data = requests.get(url, headers=headers, cookies=cookie).text
# soup = BeautifulSoup(web_data.text, 'lxml')
data = json.loads(web_data)
# print(data['item'][1]['icon']['url'])
for i in data['item']:
    print(i['icon']['url'])