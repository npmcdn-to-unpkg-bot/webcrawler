from bs4 import BeautifulSoup
import requests
import time

start_url = 'http://bj.ganji.com/wu/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
}


def get_channels(url):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data, 'lxml')