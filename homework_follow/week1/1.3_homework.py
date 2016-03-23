import requests
import time
from bs4 import BeautifulSoup
import urllib.request

# url = 'http://xm.xiaozhu.com/fangzi/1639603035.html'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Request Method': 'GET',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}

# req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.text, 'lxml')
#
# title = soup.select('h4 > em')[0].text
# price = soup.select('#pricePart > div.day_l > span')[0].text
# address = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')[0].text.strip()
# house_image = soup.select('#curBigImage')[0].get('src')
# gender = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
# mark = gender[0].get('class')
# landlord_image = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')[0].get('src')
# landlord_name = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')[0].text


def get_gender(marks):
    if marks[0] == 'member_ico1':
        return '女'
    elif marks[0] == 'member_ico':
        return '男'
    return 'Gender not found.'


# data = {
#     'title': title,
#     'address': address,
#     'price': price,
#     'house_image': house_image,
#     'landlord_name': landlord_name,
#     'landlord_image': landlord_image,
#     'gender': get_gender(mark),
# }


# Get detailed page addresses from main pages, return a list of detailed page addresses
def get_link(page):
    inner_links = []
    for i in range(1, page+1):
        full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i)
        req2 = requests.get(full_url, headers=headers)
        # time.sleep(1)
        soup2 = BeautifulSoup(req2.text, 'lxml')
        for j in soup2.select('#page_list > ul > li > a'):
            inner_links.append(j.get('href'))
    return inner_links


# Get house information in detailed pages
def get_houseinfo(links):
    houseinfo_list = []
    for link in links:
        req = requests.get(link, headers=headers)
        time.sleep(1)
        soup = BeautifulSoup(req.text, 'lxml')

        title = soup.select('h4 > em')[0].text
        price = soup.select('#pricePart > div.day_l > span')[0].text
        address = soup.select('div.pho_info > p')[0].get('title')

        '''body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5'''

        house_image = soup.select('#curBigImage')[0].get('src')
        gender = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
        mark = gender[0].get('class')
        landlord_image = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')[0].get('src')
        landlord_name = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')[0].text

        data = {
            'title': title,
            'address': address,
            'price': price,
            'house_image': house_image,
            'landlord_name': landlord_name,
            'landlord_image': landlord_image,
            'gender': get_gender(mark),
        }

        houseinfo_list.append(data)
        print(data)
    return houseinfo_list


# get_houseinfo(get_link(1))


folder_path = 'C:/Users/Model-2/Desktop/projects/week1/web_spider/1.3/landlord_image/'
for i in get_houseinfo(get_link(10)):
    if i['gender'] == '女':
        urllib.request.urlretrieve(i['landlord_image'], folder_path+i['landlord_image'][-10:])


