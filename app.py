from flask import Flask, request
import requests
from decouple import config
import pprint
import random

token = config('TELEGRAM_TOKEN')
app = Flask(__name__)
print(token)
#telegram이 url로 POST 요청을 보냄.
@app.route(f'/{token}', methods=['POST'])
def telegram():
    # message 변수에 텔레그램이 보내준 정보가 담김
    message = request.get_json()
   
    pprint.pprint(message)
    text = message.get('message').get('text')

    # 로직
    if text == '로또':
        text = random.sample(range(1,46), 6)
    elif '비트코인' in text:
        url = 'https://api.bithumb.com/public/ticker/btc'
        response = requests.get(url).json()
        text = response['data']['max_price']
    
    #답장
    base_url = f'https://api.telegram.org/bot{token}'

    #1. url 설정
    chat_id = 881541871
    url = f'{base_url}/sendMessage?text={text}&chat_id={chat_id}'

    #2. api 요청(메세지 전송)
    requests.get(url) 
    # 최종적으로 텔레그램한테 HTTP 상태코드 200(잘 완료됨)을 전송
    return '', 200

@app.route('/')
def index():
    a = 3 + 5
    return 'welcome chatbot!' + str(a)

if __name__ == '__main__':
    print(__name__)
    import os
    port = int(os.getenv('PORT', 5000))
    app.run(host = '0.0.0.0', port=port ,debug=True)


#https://api.telegram.org/bot956873054:AAF6v0VfOcmfX-B_Knkszy5UyjNIGlxtyNo/setWebhook?url=https://bfa0ee75.ngrok.io/956873054:AAF6v0VfOcmfX-B_Knkszy5UyjNIGlxtyNo