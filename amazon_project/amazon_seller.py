import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
}

url = 'http://www.amazon.com/Dreamhigh-Genuine-Leather-Bracelet-Bracelete/dp/B01DU635FC/ref=sr_1_50?ie=UTF8&qid=1460445967&sr=8-50&keywords=real+spark'
web_data = requests.get(url, headers=headers)
time.sleep(1)
soup = BeautifulSoup(web_data.text, 'lxml')

# third_party_golden_cart_seller = soup.select('#soldByThirdParty b')[0].text\
#     if soup.find_all(id='soldByThirdParty') else None
cart_sellers = list(i.text.strip() for i in soup.select('#mbc span.a-size-small.mbcMerchantName'))\
    if soup.find(class_='a-size-small mbcMerchantName') else None
golden_cart_seller = soup.select('#merchant-info a')[0].text if len(soup.select('#merchant-info a')) != 0 else None
# print(len(soup.select('#merchant-info a')))
fulfilled_by_amazon = True if len(soup.select('#merchant-info a')) == 2 else False
no_buybox_list = True if soup.find_all(id='unqualifiedBuyBox') else False
ASIN = url.split('?')[0].split('/')[-2]


# Detailed sellers for listings with buybox: new...(more than 1 seller)
def get_detail_sellers():
    if not no_buybox_list:
        if len(soup.find_all('h5')) == 4:
            detail = soup.select('#mbc > div > div > span > a')[0]
            if int(detail.text.split()[0]) > len(cart_sellers) + 1:
                # print(detail.get('href'))
                detail_data = requests.get('http://www.amazon.com'+detail.get('href'), headers=headers)
                soup2 = BeautifulSoup(detail_data.text, 'lxml')
                sellers1 = [i.text.strip() for i in soup2.select('h3 > span')]
                # print(sellers1)
                sellers2 = [j.get('alt').strip() for j in soup2.select('h3 > a > img')]
                # print(sellers2)
                detail_sellers = sellers1 + sellers2
                # print(detail_sellers)
                gcs = list()
                gcs.append(golden_cart_seller)
                no_cart_sellers = set(detail_sellers) - set(cart_sellers) - set(gcs)
                # print('no cart sellers:', no_cart_sellers)
                # print('detailsellser:{} cartseller:{} goldenseller:{}'.format(set(detail_sellers), set(cart_sellers), set(gcs)))
                if no_cart_sellers == set():
                    return None
                else:
                    return no_cart_sellers
            return None
        return None
    return None


data = {
    'Golden cart fulfilled by Amazon': fulfilled_by_amazon,
    'Golden Cart seller': golden_cart_seller,
    'Ordinary cart holder sellers': cart_sellers,
    'No buybox list': no_buybox_list,
    'No buybox sellers': get_detail_sellers(),
    'ASIN': ASIN
}

print(data)
# print(third_party_golden_cart_seller)
# print(cart_sellers)
##########################################################################
# Detailed sellers for listings without buybox: new...
# if no_buybox_list:
#     new_url = 'http://www.amazon.com' + soup.select('#unqualifiedBuyBox .a-text-center.a-spacing-mini > a')[0].get('href')
#     new_data = requests.get(new_url, headers=headers)
#     new_soup = BeautifulSoup(new_data.text, 'lxml')
#     print(new_soup)





