#[해커] Bithumb open API활용하여 실시간 BTC(Bitcoin) 현재가를 출력하는 crypto.py
#https://apidocs.bithumb.com/docs/ticker

import requests

# 1. request 통해 요청 보내기
url = 'https://api.bithumb.com/public/ticker/BTC'
response = requests.get(url)
# print(response.text)

res_dict = response.json() #dict 리턴됨
#data = res_dict['data']
opening_price = res_dict['data']['opening_price']
print(opening_price)
