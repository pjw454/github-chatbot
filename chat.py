import requests
from decouple import config

token = config('TELEGRAM_TOKEN')
base_url = f'https://api.telegram.org/bot{token}'

#1. url 설정
chat_id = 956873054
text = '안녕하세요'
url = f'{base_url}/sendMessage?text={text}&chat_id{chat_id}'

#2. api 요청(메세지 전송)
requests.get(url) 
#webhook - 사용자가 있고 (텔레그램)서버가 있으면 현재 파이썬 (서버)코드를 통해 메세지를 보내고 있음
#그 반대 흐름을 webhook이라고 한다.
#파이썬으로 어떻게 서버를 만들 수 있는지를 이번에 실습