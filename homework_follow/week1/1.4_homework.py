import requests
from bs4 import BeautifulSoup
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/\
    537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
}
proxies = {"http": "http://72.216.236.2:3128"}


def get_link(start, end):
    url = []
    for num in range(start, end):
        url.append('http://weheartit.com/inspirations/taylorswift?scrolling=true&page={}&before=183371082'.format(num))
    return url


file_path = 'C:/Users/Model-2/Desktop/projects/week1/web_spider/1_4/tay_images/'


def get_images(links, path):
    for link in links:
        req = requests.get(link, headers=headers, proxies=proxies)
        soup = BeautifulSoup(req.text, 'lxml')
        images = soup.select('img.entry_thumbnail')
        for i in images:
            print(i.get('src'))
            urllib.request.urlretrieve(i.get('src'), path+i.get('src').split('/')[-2]+i.get('src').split('/')[-1])

get_images(get_link(11, 20), file_path)


