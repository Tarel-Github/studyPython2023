# 복합형
val1 = 1
val2 = 2
val3 = 3
val4 = 4
val5 = 5
val6 = 6
val7 = 7
val8 = 8
val9 = 9
val10 = 10

print(val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8 + val9 + val10)

#위와같은 형태를 방지하기 위해서 아래 자료형을 사용

# 리스트 == 배열
# C언어에서는 배열과 리스트가 따로 있지만 파이썬에서는 둘 다 같은 개념이다.
a= [1,2,3,4,5,6,7,8,9,10]
sum = 0

for i in a:
    sum += i

print(sum)

arr1 = [1,2,3]
arr2 = [1.1, 2.2, 3.3]
arr3 = ['Hello', 13, 'World', True]
#파이썬에서는 리스트 안에 아무 값이나 넣어줄 수 있다.

print(arr3)
print(type(arr3))

#비어있는 리스트
arr4 = []
arr5 = list()
print(arr4)
print(arr5)

#아래는 다소 복잡한 형태의 리스트
arr6 = [1,2,3, [6,7,8,[9,10]]]
print(arr6)

#리스트에 값 넣기
arr4.append(4) #arr4에 4를 넣는다.
print(arr4)

# 튜플
#튜플은 소괄호를 사용
tuple1 = (1,2,3,4)
print(tuple1)
#튜플은 리스트와 다르게 값을 넣고 뺄 수 없다.


# 딕셔너리
spiderman = {'name' : 'Peter Parker',
              'age' : 18,
           'weapon' : 'Web Shooter',
          'deserter': '탈영병'}

print(spiderman)
print(spiderman['weapon'])
print(spiderman['age'])
print(type(spiderman))

#집합
set1 = set([1,2,3,4])
print(set1)

set2 = set("Hello World")
print(set2)


