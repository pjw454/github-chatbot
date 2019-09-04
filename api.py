import requests

#1. url 설정
url = 'https://api.bithumb.com/public/ticker/btc'
#2. 요청
response = requests.get(url).json()
#3. 응답처리
print(response['data']['max_price'])