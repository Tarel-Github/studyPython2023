# urllib 패키지 가져오기
from urllib.request import Request, urlopen

req = Request('https://www.naver.com')
res = urlopen(req)
print(res.status)