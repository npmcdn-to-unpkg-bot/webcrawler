from bs4 import BeautifulSoup
import requests
import time

start_url = 'http://bj.ganji.com/wu'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
}


def get_channels(url):
    host_url = 'http://bj.ganji.com'
    channel_urls = []
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    links = soup.select('dl.fenlei dt > a')
    for link in links:
        channel_urls.append(host_url+link.get('href'))
    return channel_urls


def get_channel_pages(channel_urls, stop_page, start_page=1):
    channel_pages = []
    for channel_url in channel_urls:
        for page in range(start_page, stop_page+1):
            channel_pages.append(channel_url+'o{}'.format(page))
            return channel_pages


def get_item_pages(pages):
    item_pages = []
    for page_url in pages:
        web_data = requests.get(page_url, headers=headers)
        soup = BeautifulSoup(web_data.text, 'lxml')
        items = soup.select('dd.feature li > a')
        for item in items:
            item_pages.append(item.get('href'))
    return item_pages


def get_item_info(item_pages):
    for one_page in item_pages:
        web_data = requests.get(one_page, headers=headers)
        time.sleep(2)
        soup = BeautifulSoup(web_data.text, 'lxml')
        title = soup.select('h1.title-name')[0].text
        price = soup.select('i.f22')[0].text
        date = soup.select('i.pr-5')[0].text.strip()[0:5]
        type = soup.select('.det-infor li > span > a')[0].text
        place = list(i.text for i in soup.select('.det-infor li > a')[1:])
        condition = list(soup.select('.second-det-infor li')
                         [0].stripped_strings)[1] if soup.find_all('ul', 'second-det-infor') else None
        data = {
            'title': title,
            'price': price,
            'date': date,
            'type': type,
            'place': place,
            'condition': condition
        }
        print(data)


channels = get_channels(start_url)
pages = get_channel_pages(channels, 2)
item_pages = get_item_pages(pages)
get_item_info(item_pages)


# get_item_info(['http://bj.ganji.com/jiaju/1802057617x.htm'])