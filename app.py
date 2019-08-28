from flask import Flask
import random
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

# 1. 주문서 만들고,
# 2. 해당 주문이 들어왔을때 무엇을 할지 정의

@app.route('/name')
def name():
    return '홍길동'

#variable
@app.route('/hello/<name>')
def hello(name):
    #return 'hello' + name
    return f'hello {name}'
    
#/square/숫자
#입력된 숫자를 제곱한 결과를 보여줌
@app.route('/square/<int:number>')
def square(number):
    #return str(int(number) ** 2)
    return str(number ** 2)

#점심메뉴 추천
@app.route('/menu')
def menu():
    foods = ['바스버거','대우식당','진가와','고갯마루']
    food = random.choice(foods)
    return food

#lotto 로또번호 추천
@app.route('/lotto')
def lotto():
    winner =[]
    #winner = [3,5,12,13,33,39]
    result = random.sample(range(1,46),6)
    #result = [3,5,12,43,23,19]
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'
    response = requests.get(url)
    res_dict = response.json() #dict 리턴됨

    #1등 번호 6개가 담긴 result라는 list 출력    
    for i in range(1,7):
        winner.append(res_dict['drwtNo'+ str(i)])

    #만약에 6개가 모두 일치하면 1등
    #만약 5개가 일치하면 3등
    #만약 4개가 일치하면 4등
    #만약 3개가 일치하면 5등    
    num = "꽝"
    cnt = 0

    cnt = len(set(winner) & set(result))

    if cnt == 6:
        num = "1등"
    elif cnt == 5:
        num = "3등"
    elif cnt == 4:
        num = "4등"
    elif cnt == 3:
        num = "5등"

    return str(sorted(result)) +" "+ num
