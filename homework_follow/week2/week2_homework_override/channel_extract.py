from bs4 import BeautifulSoup
import requests

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


# print(get_channels(start_url))

channels = ['http://bj.ganji.com/jiaju/', 'http://bj.ganji.com/rirongbaihuo/',
            'http://bj.ganji.com/shouji/', 'http://bj.ganji.com/shoujihaoma/',
            'http://bj.ganji.com/bangong/', 'http://bj.ganji.com/nongyongpin/',
            'http://bj.ganji.com/jiadian/', 'http://bj.ganji.com/ershoubijibendiannao/',
            'http://bj.ganji.com/ruanjiantushu/', 'http://bj.ganji.com/yingyouyunfu/',
            'http://bj.ganji.com/diannao/', 'http://bj.ganji.com/xianzhilipin/',
            'http://bj.ganji.com/fushixiaobaxuemao/', 'http://bj.ganji.com/meironghuazhuang/',
            'http://bj.ganji.com/shuma/', 'http://bj.ganji.com/laonianyongpin/',
            'http://bj.ganji.com/xuniwupin/', 'http://bj.ganji.com/qitawupin/',
            'http://bj.ganji.com/ershoufree/', 'http://bj.ganji.com/wupinjiaohuan/']
