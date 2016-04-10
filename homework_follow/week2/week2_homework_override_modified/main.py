from channel_extract import channels
from page_parsing import get_item_url, get_item_info
from multiprocessing import Pool
import pymongo

myDB = pymongo.MongoClient('localhost', 27017)
ganji2 = myDB['ganji2']
item_url2 = ganji2['item_url2']
item_info2 = ganji2['item_info']


# def get_urls(db, url_list):
#     for i in db.find():
#         url_list.append(i['item_url'])


# def get_already_own_urls(db, own_url_list):
#     for i in db.find():
#         own_url_list.append(i['index_url'])
#
#
def get_item_urls(channels):
    for i in range(1, 150):
        get_item_url(channels, i)
        print(channels+' 第'+str(i)+'页完成')

if __name__ == '__main__':

    # p1 = Pool()
    # p1.map(get_item_urls, channels)
    # p1.close()
    # p1.join()

    own_urls = set(i['url'] for i in item_info2.find())
    all_urls = set(i['item_url'] for i in item_url2.find())
    rest_urls = all_urls - own_urls
    p2 = Pool()
    p2.map(get_item_info, rest_urls)
    p2.close()
    p2.join()

