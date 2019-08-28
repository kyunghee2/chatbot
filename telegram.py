"""
python으로 telegram message 보내기

"""
import requests

base_url ='https://api.telegram.org'
token ='bot...'
method = 'getUpdates'

#(1) getUpdates을 통해 chat_id를 가져오기
url = f'{base_url}/{token}/{method}'
response = requests.get(url)
res_dict = response.json()

data = res_dict['result'][0]
chat_id = data['message']['chat']['id']

#(2) url을 조합하여 requests로 요청 보내기
msg ='오늘 수업 잘 들었습니다.'
method = 'sendMessage'

url = f'{base_url}/{token}/{method}?chat_id={chat_id}&text={msg}'
print(url)
requests.get(url)

