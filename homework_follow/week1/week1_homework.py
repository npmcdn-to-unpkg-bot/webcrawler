from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/49.0.2623.87 Safari/537.36'
}
start_url = 'http://bj.58.com/pbdn/0/'


def get_item_link(url):
    item_links = []
    web_data = requests.get(url, headers=headers)
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


def get_item_info(item_links):
    for link in item_links:
        web_data = requests.get(link, headers=headers)
        time.sleep(1)
        soup = BeautifulSoup(web_data.text, 'lxml')
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
            'views': get_views(link)
        }
        print(data)


def get_views(link):
    url = 'http://jst1.58.com/counter?infoid={}'.format(link.strip('x.shtml').split('/')[-1])
    web_data = requests.get(url)
    return web_data.text.split('=')[-1]


item_urls = get_item_link(start_url)
get_item_info(item_urls)

# print(get_views('http://bj.58.com/pingbandiannao/25481834511792x.shtml'))

