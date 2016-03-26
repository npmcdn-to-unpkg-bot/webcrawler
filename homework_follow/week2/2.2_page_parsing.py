import requests
from bs4 import BeautifulSoup
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
item_list = tongcheng['item_list']
item_info = tongcheng['item_info']


def get_link_from(channel, pages, who_sells=0):
    list_view = '{}{}/pn{}/'.format(channel, who_sells, pages)
    web_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    if soup.find('td', 't'):
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            if 'zhuanzhuan' not in item_link.split('.'):
                item_list.insert_one({'url': item_link})
                print(item_link)
    else:
        pass


def get_item_info(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    no_longer_exist = '404' in soup.find('script', type='text/javascript').get('src').split('/')
    if no_longer_exist:
        pass
    else:
        title = soup.title.text
        price = soup.select('span.price')[0].text
        area = list(soup.select('.c_25d')[1].stripped_strings) if soup.find_all('span', 'c_25d') else None
        date = soup.select('.time')[0].text
        data = {
            'title': title,
            'price': price,
            'area': area,
            'date': date
        }
        item_info.insert_one(data)
        print(data)

# get_link_from('http://xm.58.com/tushubook/', 3)

# get_item_info('http://xm.58.com/bijibendiannao/25457681070796x.shtml')


