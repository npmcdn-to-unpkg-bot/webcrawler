import requests
from bs4 import BeautifulSoup
import time
import pymongo

azdb = pymongo.MongoClient('localhost', 27017)
az = azdb['az']
azseller = az['azseller']

def get_data(asin):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
    }

    cookies = {
        'Cookie': 'x-wl-uid=1gCWZbFgHql1/dZnB2DrFZNuprGhADWOCJ1SjdjsJ4ZEtxXGc0ojq6XnDhYfC5WMbNfUlmelP7lg=; session-token=HTdvXx19aJwdOG+h5LdS+6NuENW5nG2nIEgx4lTCWcAWrvbPvCtk8JkEnsUPFW71Pq9kG3ovBbLUvdrXOqUghObpkH1iWivc/XGd8fk6IkKQF43AXbw+lnpzIcQU6/c7I8KLya10OVFTS+U4c/xYuI/cVmaQV2eyLMyDW77Dl2UaOsVGXgwvBaNrfdB2HClwQWRLeaJlhqbOz750bztZ82OsaOSUIfK6W145RR1dOjK3zpapo9CrO8+egWWWmTz4; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3D%3B; aws-session-id=190-6932906-5934804; aws-session-id-time=2091145469l; aws-ubid-main=192-8315411-7690260; s_cc=true; s_vnum=1892425582405%26vn%3D1; s_ppv=59; s_nr=1460425921862-Repeat; s_dslv=1460425921865; s_sq=acsus-prod%3D%2526pid%253D200414280%2526pidt%253D1%2526oid%253DGo%2526oidt%253D3%2526ot%253DSUBMIT; pN=22; s_pers=%20s_vnum%3D1892338774771%2526vn%253D2%7C1892338774771%3B%20s_invisit%3Dtrue%7C1460429257291%3B; skin=noskin; session-id-time=2082787201l; session-id=183-5267607-0063530; csm-hit=SCRGWRTVXA4BFWRPRFV7+s-SCRGWRTVXA4BFWRPRFV7|1460465160573; ubid-main=178-8395338-6824722'
    }

    url = 'http://www.amazon.com/dp/' + asin
    web_data = requests.get(url, headers=headers, cookies=cookies)
    # print('get_data web_data finished')
    time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    # print('get_data soup finished')
    # third_party_golden_cart_seller = soup.select('#soldByThirdParty b')[0].text\
    #     if soup.find_all(id='soldByThirdParty') else None
    cart_sellers = list(i.text.strip() for i in soup.select('#mbc span.a-size-small.mbcMerchantName'))\
        if soup.find(class_='a-size-small mbcMerchantName') else []
    golden_cart_seller = soup.select('#merchant-info a')[0].text if len(soup.select('#merchant-info a')) != 0 else []
    # print(len(soup.select('#merchant-info a')))
    fulfilled_by_amazon = True if len(soup.select('#merchant-info a')) == 2 else False
    no_buybox_list = True if soup.find_all(id='unqualifiedBuyBox') else False
    ASIN = url.split('?')[0].split('/')[-2]


    # Detailed sellers for listings with buybox: new...(more than 1 seller)
    def get_detail_sellers():
        if not no_buybox_list:
            if len(soup.find_all('h5')) == 4:
                detail = soup.select('#mbc > div > div > span > a')[0]
                # if int(detail.text.split()[0]) > len(cart_sellers) + 1:
                # print(detail.get('href'))
                detail_data = requests.get('http://www.amazon.com'+detail.get('href'), headers=headers)
                soup2 = BeautifulSoup(detail_data.text, 'lxml')
                sellers1 = [i.text.strip() for i in soup2.select('h3 > span')]
                # print('seller1:', sellers1)
                sellers2 = [j.get('alt').strip() for j in soup2.select('h3 > a > img')]
                # print('seller2:', sellers2)
                detail_sellers = sellers1 + sellers2
                print('detail_selelrs:', detail_sellers)
                gcs = list()
                gcs.append(golden_cart_seller)
                no_cart_sellers = list(set(detail_sellers) - set(cart_sellers) - set(gcs))
                # print('no_cart_sellers:', no_cart_sellers)
                # seller_url = soup.select('h3 a')
                # print('no cart sellers:', no_cart_sellers)
                # print('detailsellser:{} cartseller:{} goldenseller:{}'.format(set(detail_sellers), set(cart_sellers), set(gcs)))
                if no_cart_sellers == []:
                    return []
                else:
                    return no_cart_sellers
                # return []
            return []
        return []
    ncs = get_detail_sellers()
    seller_list = list()
    seller_list.append(golden_cart_seller)
    seller_list.extend(cart_sellers)
    data = {
        'Golden cart fulfilled by Amazon': fulfilled_by_amazon,
        'Golden Cart seller': golden_cart_seller,
        'Ordinary cart holder sellers': cart_sellers,
        'No buybox list': no_buybox_list,
        'No buybox sellers': ncs,
        'ASIN': asin,
        'All sellers': seller_list + list(ncs),
    }
    print(data)
    azseller.insert_one(data)
    # print(data)
    # return data
# print(third_party_golden_cart_seller)
# print(cart_sellers)
##########################################################################
# Detailed sellers for listings without buybox: new...
# if no_buybox_list:
#     new_url = 'http://www.amazon.com' + soup.select('#unqualifiedBuyBox .a-text-center.a-spacing-mini > a')[0].get('href')
#     new_data = requests.get(new_url, headers=headers)
#     new_soup = BeautifulSoup(new_data.text, 'lxml')
#     print(new_soup)

if __name__ == '__main__':
    asin_list = ['B010HWVOK0', 'B013DOOB7M', 'B0107Y31UE']
    while True:
        for i in asin_list:
            get_data(i)
            time.sleep(10)
        time.sleep(900)



