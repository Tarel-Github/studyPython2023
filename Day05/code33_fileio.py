# 파일 만들기
file = open('sample.txt', 'w') #파일을 쓰기로 만듦

file.write('안녕하세요~')
file.write('첫번째 파일!!')

file.close()
print('sample.txt 파일이 만들어졌습니다')