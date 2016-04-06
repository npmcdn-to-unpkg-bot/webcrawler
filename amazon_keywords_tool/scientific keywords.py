import requests
import re
import time

keywords = []
single_words = []

seeds = ['fashion bracelets','bracelets']
headers = {
    'Host': 'completion.amazon.com',
    'Referer': 'http://app.scientificseller.com/keywordtool',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleW\
ebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    }
proxies = {}
url1 = 'http://completion.amazon.com/search/complete?method=completion&q='
url2 = '&search-alias=aps&client=amazon-search-ui&mkt=1&fb=1&xcat=0&x=angular\
.callbacks._13&sc=1'
try:
    for seed in seeds:
        url = url1 + seed + url2
        r = requests.get(url, headers=headers, proxies=proxies)
        response = r.text
        s = re.findall('\"(.*?)\"', response)
        keywords.extend(s)
        # print(s)
    
    for seed in seeds:
        for i in range(97, 123):
            url = url1 + seed + '%20' + chr(i) + url2
            r = requests.get(url, headers=headers, proxies=proxies)
            response = r.text
            s = re.findall('\"(.*?)\"', response)
            s.pop(0)
            print(s)
            keywords.extend(s)
            time.sleep(2)
except TimeoutError as err:
    print('Timeout Error', str(err))
    pass
for word in keywords:
    single_words.extend(word.split())
diff_keywords = list(set(single_words))
diff_keywords.sort(key=single_words.index)
print(diff_keywords)

