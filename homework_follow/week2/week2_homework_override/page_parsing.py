from bs4 import BeautifulSoup
import requests
import pymongo
import time

myDB = pymongo.MongoClient('localhost', 27017)
ganji = myDB['ganji']
item_url = ganji['item_url']
item_info = ganji['item_info']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
}


def get_item_url(channel, page, who_sells='o'):
    list_view = '{}{}{}'.format(channel, who_sells, str(page))
    web_data = requests.get(list_view, headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text, 'lxml')
    if soup.find_all('ul', 'pageLink'):
        items = soup.select('dd.feature li > a')
        for item in items:
            # Get short link
            url = requests.get(item.get('href'), headers=headers).url
            time.sleep(2)
            # Check duplicates before data is inserted
            if url not in list(i['item_url'] for i in item_url.find()):
                # Exclude Zhuanzhuan items
                if 'zhuanzhuan' and 'sorry' not in url.split('/'):
                    print(url)
                    item_url.insert_one({'item_url': url})
    else:
        pass
    # print(list(item_url.find()))


def get_item_info(one_page):
    web_data = requests.get(one_page, headers=headers)
    if web_data.status_code == 404:
        pass
    else:
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
            'condition': condition,
            'url': one_page
        }
        print(data)

# for i in item_url.find():
#     print(i['item_url'])

