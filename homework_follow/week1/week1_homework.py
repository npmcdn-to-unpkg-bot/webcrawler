from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/49.0.2623.87 Safari/537.36'
}


def get_item_link(who_sells):
    start_url = 'http://bj.58.com/pbdn/{}/'.format(who_sells)
    item_links = []
    web_data = requests.get(start_url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    time.sleep(1)
    links = soup.select('td.t a.t')
    for link in links:
        item_url = link.get('href').split('?')[0]
        # if 'jump' and 'jing' and 'zhuanzhuan' not in item_url:
        if 'jump' not in item_url and 'jing' not in item_url and 'zhuanzhuan' not in item_url:
            # print(item_url)
            item_links.append(item_url)
    return item_links


def get_item_info(who_sells=0):
    item_links = get_item_link(who_sells)
    for link in item_links:
        web_data = requests.get(link, headers=headers)
        time.sleep(1)
        soup = BeautifulSoup(web_data.text, 'lxml')
        # seller_mark = link.split('/')[-1]
        cate = soup.select('.crb_i a')[1].text
        title = soup.select('#content h1')[0].text
        date = soup.select('li.time')[0].text
        price = soup.select('span.price')[0].text
        position = list(soup.select('span.c_25d')[0].stripped_strings) if soup.find_all('span', 'c_25d') else None
        data = {
            'cate': cate,
            'title': title,
            'date': date,
            'price': price,
            'position': position,
            'views': get_views(link),
            'seller': '个人' if who_sells == 0 else '商家'
        }
        print(data)


def get_views(link):
    url = 'http://jst1.58.com/counter?infoid={}'.format(link.strip('x.shtml').split('/')[-1])
    web_data = requests.get(url)
    return web_data.text.split('=')[-1]


get_item_info()

# print(get_views('http://bj.58.com/pingbandiannao/25481834511792x.shtml'))

