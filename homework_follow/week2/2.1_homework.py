import requests
from bs4 import BeautifulSoup
import pymongo
import urllib.request

client = pymongo.MongoClient('localhost', 27017)
houseInfo = client['houseInfo']
tabs = houseInfo['tabs']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Request Method': 'GET',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}


def get_page_links(start, stop):
    urls = []
    for p in range(start, stop+1):
        url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(p)
        urls.append(url)
    return urls


# links = get_page_links(1, 3)


def get_detailed_pages(urls):
    detailurl = []
    for url in urls:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        detailed_urls = soup.select('#page_list div.result_btm_con.lodgeunitname')
        for i in detailed_urls:
            detailurl.append(i.get('detailurl'))
    return detailurl

# detailurls = get_detailed_pages(links)


def get_detail_info(urls):
    for i in urls:
        r = requests.get(i, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        title = soup.title.text.split('|')[0].split('-')[0]
        address = soup.select('span.pr5')[0].text.strip()
        price = soup.select('#pricePart span')[0].text
        pic = soup.select('#floatRightBox a > img')[0].get('src')
        gender = get_gender(soup.select('#floatRightBox div.member_pic > div')[0].get('class')[0])
        name = soup.select('#floatRightBox h6 > a')[0].text
        data = {
            'title': title,
            'address': address,
            'price': int(price),
            'pic': pic,
            'name': name,
            'gender': gender,
        }
        tabs.insert_one(data)


def get_gender(gender):
    if gender == 'member_ico':
        return '男'
    elif gender == 'member_ico1':
        return '女'

# get_detail_info(detailurls)

# path = 'C:/Users/Model-2/Desktop/web_crawler/webcrawler/homework_follow/week2/img/'

for item in tabs.find({'price': {'$gt': 500}}):
    print(item)



