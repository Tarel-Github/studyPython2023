#자료형
None #None은 값이 없다. 즉, 다른 언어들의 Null과 같다.

print(0 == None)        #None은 값이 없는거지 0이 아니다. 고로 false
print(None)

#숫자형
#정수       3, 10, 0, -5 등등
#실수       
#2진수(8, 16 등등)


val = 3
print(type(val))

val = 3.14
print(type(val))

val = "Hello"
print(type(val))

val = 0b1010        #2진수도 int로 분류
print(val)          #출력은 10진수로
print(type(val))

val = 12_111_444    #숫자를 3자리당 언더바로 구분지을 수 있다.
print(val)
print(type(val))


#print(type(값))을 사용하여 값의 자료형(타입)을 알 수 있다.

#문자열
val = "Life is short, You need Python."
print(val)
print(type(val))

val = 'Hello \n World!'     # \n은 줄바꿈
print(val)
print(type(val))

val = 'Hello\tWorld!'     # \t는 탭(공백 4개)
print(val)

val = 'Hello\bWorld!'     # \b는 한 칸 지우기
print(val)

val = '''삶은 짧으니 파이썬을 배우거라
배우거라 배우거라'''        # 따옴표를 3번하면 여러줄 작성이 가능

#불린
참 = True
거짓 = False
print(type(참))

print(거짓 == True)
print(거짓 == False)
print(거짓 == True)

print(bool(1))      #1은 True, 0이 아닌 수는 true
print(bool(0))      #0은 False