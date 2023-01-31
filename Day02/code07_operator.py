# 연산자
# 할당연산 assignment
# 2 = 1 (X)

val = 1

# equal 연산자
print(val == 1)

# 사칙연산
print(1 + 1)
print(1 - 1)
print(10 * 10)
print(1024 / 3) #소수 나누기
print(1024 // 3) #정수 나누기
print(17 % 3)
print(2**10)    #2의 10승

# 문자열 연산
first = 'Hello'
second = 'World'
print(first + ' ' + second)
print(first * 4)

# 문자열 길이
print(len(first))
print(first[0])
print(first[-1])


current = '2023-01-31 15:14:02' # 현 시간
print(len(current))
print(current[0:4])
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

print(current[0:4]+'년'+current[5:7]+'월'+current[8:10]+'일'+current[11:13]+'시'+current[14:16]+'분'+current[17:]+'초')

# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7
print(que)

que.append(6)
print(que)

que.insert(0, 0)
print(que)

que.remove(5)
print(que)


