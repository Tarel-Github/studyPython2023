# 전역/지역변수
num = 1

for i in range(1,11):
    num = i * num
    print(f'{i + i}번')

    if i % 3 == 0:
        res = '테스트'
        print(res)
print(f'결과는 {num}')
print(res)


