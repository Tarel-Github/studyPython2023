# for문
arr = [1,2,3,4,5]

for item in arr:
    print(f'{item: 2.2f}')

arr = [1,2,3,4,5]
sum = 0

for item in arr:
    sum += item
    print(sum)

# 긴 리스트를 편하게 만들기
vals = [1,2,3,4,5,6,7,8,9,10]
vals = [i for i in range(1,11)]
print(vals)
valsLong = [i for i in range(1,1001)]
print(valsLong)

num = 0
for item in vals:
    num += item
    if num % 2 == 0:
        continue # 이후의 것을 수행하지 않고 다시 for문 첫부분으로 간다.
    else:
        print(num, '번 수는', item, '입니다.')

num = 0
for item in vals:
    num += item
    if num % 2 == 0:
        print('반복문을 중단합니다!')
        break
    else:
        print(num, '번 수는', item, '입니다.')

