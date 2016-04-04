import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/\
    537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
}

cookies = {
    'Cookie': '_T_WM=4d99873d6b0fd6b29e8c98e89b1dfe76; H5_wentry=H5; \
    gsid_CTandWM=4uNe6bef1UKoksUKA6G4I8evD4R; SUB=_2A257-uFRDeRxGedH7VAV8C\
    _Pyz2IHXVZBI8ZrDV6PUJbrdAKLUbjkW1LHeuVbVpqEaA_dhYpHU2VQvs7mmjTog..; \
    M_WEIBOCN_PARAMS=featurecode%3D20000181%26luicode%3D10000012%26lfid%3\
    D1005051647439613_-_WEIBO_SECOND_PROFILE_WEIBO%26fid%3D10050516474396\
    13%26uicode%3D10000011'
}

base_url = 'http://weibo.cn'



