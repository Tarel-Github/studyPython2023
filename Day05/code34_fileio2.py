# 파일 읽어오기
file = open('./Day04/sample05.txt', 'r', encoding='utf-8')

text = file.readline()
print(text)

while True:
    text = file.read()
    if not text: break
    print(text)

file.close()