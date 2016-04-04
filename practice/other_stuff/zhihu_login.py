import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
}
s = requests.Session()
login_data = {'email': '*', 'password': '*'}
s.post('http://www.zhihu.com/login/email', login_data, headers=headers)
r = s.get('https://www.zhihu.com', headers=headers)
print(r.text)
