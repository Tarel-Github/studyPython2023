# 외부모듈 사용
import requests

res = requests.get('http://www.naver.com')
print(res.status_code)
print('==================')
print(res.content)

