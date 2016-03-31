import requests

r = requests.get('http://xm.ganji.com/rirongbaihuo/17736671194x.htm')
print(type(r.status_code))