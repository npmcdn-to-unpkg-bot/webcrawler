import requests
from bs4 import BeautifulSoup

start_url = 'http://xm.58.com/sale.shtml'
url_host = 'http://xm.58.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Request Method': 'GET',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}


def get_channel_urls(url):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    # print(links)
    # page_urls = [url_host+i.get('href') for i in links]
    # print(page_urls)
    for link in links:
        page_url = url_host + link.get('href')
        print(page_url)

get_channel_urls(start_url)

