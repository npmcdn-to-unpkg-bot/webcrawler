import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
}

url = 'http://www.amazon.com/gp/product/B014IIOOYC/ref=olp_product_details?ie=UTF8&me='
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


data = {
    'Golden cart fulfilled by Amazon': fulfilled_by_amazon,
    'Golden Cart seller': golden_cart_seller,
    'Ordinary cart holder sellers': cart_sellers,
    'No buybox list': no_buybox_list,
    'No buybox sellers': '',
    'ASIN': ASIN
}

print(data)
# print(third_party_golden_cart_seller)
# print(cart_sellers)
##########################################################################
if no_buybox_list:
    new_url = 'http://www.amazon.com' + soup.select('#unqualifiedBuyBox .a-text-center.a-spacing-mini > a')[0].get('href')
    new_data = requests.get(new_url, headers=headers)
    new_soup = BeautifulSoup(new_data.text, 'lxml')
    print(new_soup.select(''))



