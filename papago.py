import requests
from decouple import config

NAVER_CLIENT_ID = config('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
#1. url 설정
url = 'https://openapi.naver.com/v1/papago/n2mt'

#2. 요청 설정
headers = {
    'X-Naver-Client-Id' : NAVER_CLIENT_ID ,
    'X-Naver-Client-Secret' : NAVER_CLIENT_SECRET
}

data = {
    'source' : 'ko',
    'target' : 'en',
    'text' : '띵작'
}

response = requests.post(url, headers=headers, data=data).json()
print(response)
