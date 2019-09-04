# 파이썬 프로젝트

## 1. 기본 설정

1. 파이썬 가상환경

   python에서 가상환경을 설정하는 이유는 프로젝트마다 독립적인 패키지(pip)를 활용하기

   위해서이다.

   ```bash
   $ python -m venv venv
   ```

   2. 가상환경 실행

      ```bash
      $ source venv/Script/activate
      ```

      - activate : git bash에서 활용
      - activate.bat : cmd에서 활용
      - activate.psl : powershell에서 활용

    3. 가상환경 종료

       ```bash
       $ deactivate
       ```

### 2. Git 설정

git 저장소 초기화와 동시에 항상 .gitignore 파일을 생성하자.

특히, venv 폴더는 반드시 등록해야 한다.



### 3. 환경변수 설정

python-decouple 을 활용하여 관리하자.

```bash 
$ pip install python-decouple
```

1.  .env 파일에 환경 변수 등록

```bash
NAVER_CLIENT_ID ='_nO7lsv6QHWjKpowvePA'
NAVER_CLIENT_SECRET = '2gNXI8798I'xxxxxxxxxx NAVER_ID = NAVER_CLIENT_ID ='_nO7lsv6QHWjKpowvePA'NAVER_CLIENT_SECRET = '2gNXI8798I'bash
```

2. 파이썬에서 활용

```bash
from decouple import config

NAVER_CLIENT_ID = config('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
```

#### 주의!!! 반드시 .env 를 . gitignore에 등록!!!


