# seller detail page product asin getter
import requests
import json
import time
from bs4 import BeautifulSoup

url = 'http://www.amazon.com/sp?_encoding=UTF8&asin=&isAmazonFulfilled=1&isCBA=&marketplaceID=ATVPDKIKX0DER&orderID=&seller=A2NOJB13WPUTQ6&tab=&vasStoreID=#products'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
           'Referer': 'http://www.amazon.com/sp?_encoding=UTF8&asin=&isAmazonFulfilled\
           =\&isCBA=&marketplaceID=ATVPDKIKX0DER&orderID=&seller=A3O0HAV57EWUQU&tab=&vasStoreID=',
           'Origin': 'http://www.amazon.com',
           'X-Requested-With': 'XMLHttpRequest'}

cookies = {'Cookie': 'x-wl-uid=1gCWZbFgHql1/dZnB2DrFZNuprGhADWOCJ1SjdjsJ4ZEtxXGc0ojq6XnDhYfC5WMbNfUlmelP7lg=;\
 session-token=HTdvXx19aJwdOG+h5LdS+6NuENW5nG2nIEgx4lTCWcAWrvbPvCtk8JkEnsUPFW71Pq9kG3ovBbLUvdrXOqUghObpkH1iWivc\
 /XGd8fk6IkKQF43AXbw+lnpzIcQU6/c7I8KLya10OVFTS+U4c/xYuI/cVmaQV2eyLMyDW77Dl2UaOsVGXgwvBaNrfdB2HClwQWRLeaJlhqbOz\
 750bztZ82OsaOSUIfK6W145RR1dOjK3zpapo9CrO8+egWWWmTz4; s_nr=1460338774771-New; s_vnum=1892338774771%26vn%3D1; \
 s_dslv=1460338774772; skin=noskin; ubid-main=178-8395338-6824722; session-id-time=2082787201l; session-id=183-\
 5267607-0063530; csm-hit=0B1ASWCX4GT9GBHMP0ZR+s-13068SNBVZZEEKTW2263|1460605179175'}
request_url = 'http://www.amazon.com/sp/ajax/products'

base_url = 'http://www.amazon.com/dp/'

# page_data = requests.get(url, headers=headers, cookies=cookies)
# soup = BeautifulSoup(page_data.text, 'lxml')
# last_page = soup.select('#products-list')
# print(last_page)


def get_products_asin(store_link, page):
    info = store_link.split('=')
    seller = info[-3].replace('&tab', '')
    marketplace = info[-5].replace('&orderID', '')
    # print(marketplace)
    # print(seller)
    psr = {'marketplace': marketplace, 'seller': seller, 'url': '/sp/ajax/products',
           'pageSize': 12, "searchKeyword": "",
           "extraRestrictions": {}, "pageNumber": page}
    # 要传的参数中如果有字典，要将字典转为JSON格式
    payload = {'marketplaceID': marketplace,
               'seller': seller,
               'productSearchRequestData': json.dumps(psr)}

    web_data = requests.post(request_url, data=payload, headers=headers, cookies=cookies)
    time.sleep(1)
    # print(web_data.text)
    # products_asins = []
    for i in json.loads(web_data.text)['products']:
        # print(i)
        # products_asins.append(i['productUrlsMap']['products_tab'].split('/')[2].split('?')[0])
    # return products_asins
        yield i['productUrlsMap']['products_tab'].split('/')[2].split('?')[0]

# for j in get_products_asin(url, 201):
#     print(j)


def yes_or_no(asin):
    item_url = base_url + asin
    web_data = requests.get(item_url, headers=headers, cookies=cookies, timeout=10)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    if soup.find_all(id='unqualifiedBuyBox'):
        if int(soup.select('#unqualifiedBuyBox > div > div > a')[0].text.split()[0]) > 1:
            # price = soup.select('#unqualifiedBuyBox > div > div > span')[0].text
            print(asin)
        else:
            print('No...')
    elif len(soup.find_all('h5')) == 4:
        seller_number = int(soup.select('#mbc > div > div > span > a')[0].text.split()[0])
        if len(soup.select('#merchant-info a')) == 2:
            if seller_number > 2:
                print(asin)
            else:
                print('No...')
        elif seller_number > 1:
            print(asin)
        else:
            print('No...')
    else:
        print('No...')

if __name__ == '__main__':
    for i in range(1, 20):
        for j in get_products_asin(url, i):
            try:
                yes_or_no(j)
            except requests.exceptions.Timeout:
                print('timeout passed')
                pass
