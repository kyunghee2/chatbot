"""
requests를 통해 동행복권 API 요청을 보내어,
1등 번호를 가져와 python list로 만듬
"""
import requests

# 1. request 통해 요청 보내기
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'
response = requests.get(url)
# print(response.text)

res_dict = response.json() #dict 리턴됨
# print(res_dict)
# print(res_dict['drwtNo1'])

#1등 번호 6개가 담긴 result라는 list 출력
result =[]
for i in range(1,7):
    result.append(res_dict[f'drwtNo{i}'])
    #result.append(res_dict['drwtNo'+ str(i)])

print(result)

### 실습과제
#1) 1등 번호 6개가 담긴 result라는 list 출력

#2) 해당 코드를 Flask 서버(app.py) /lotto함수에 적용

#3) [해커] Bithumb open API활용하여 실시간 BTC(Bitcoin) 현재가를 출력하는 crypto.py
