import pymongo

myDB = pymongo.MongoClient('localhost', 27017)
ganji = myDB['ganji']
item_url = ganji['item_url']
item_info = ganji['item_info']

for item in item_url.find({"item_url" : "http://bj.ganji.com/bangong/2046507469x.htm"}):
    print(item)