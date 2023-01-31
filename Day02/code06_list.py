#복합형
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

#리스트 == 배열
#C언어에서는 배열과 리스트가 따로 있지만 파이썬에서는 둘 다 같은 개념이다.
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

arr4 = [] #비어있는 리스트
arr5 = list() #비어있는 리스트
print(arr4)
print(arr5)

arr6 = [1,2,3, [6,7,8,[9,10]]]
print(arr6)

