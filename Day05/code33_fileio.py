# 파일 만들기
file = open('sample.txt', 'w', encoding='utf-8') #파일을 쓰기로 만듦

file.write('안녕하세요~')
file.write('첫번째 파일!!')

file.close()
print('sample.txt 파일이 만들어졌습니다')

# ASCII -> 한 단어를 표현하는 체계(영어)

# 파일/폴더 경로

file2 = open('C:/DEV/sample01.txt', 'w', encoding='utf-8')

file2.write('안녕하세요~\n')
file2.write('두번째 파일이다.\n')
file2.write('절대경로 파일\n')

file2.close()
print('sample01.txt가 생성되었습니다.')

# 상대경로

file3 = open('./sample05.txt', 'w', encoding='utf-8')

# file3 = open('./Day05/../Day04/sample05', 'w', encoding='utf-8')

file3.write('안녕하세요~\n')
file3.write('두번째 파일이다.\n')
file3.write('상대경로 파일\n')

file3.close()
print('sample05.txt가 생성되었습니다.')


