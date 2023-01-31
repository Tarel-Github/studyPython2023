#변수
val = "Hello World"
print(val)

val = 3.141592
print(val)

val = 10/2.6
print(val)

val = 10//2.6     # /를 두 번 하면 결과값에서 소수가 사라진다.(버림)
print(val)
print(id(val))

a = [1,2,3]
print(a)
print(id(a))

#파이썬은 자료형과 상관없이 값을 넣어줄 수 있다.
#모든 변수는 id값이 있다 print(id(보고자하는 변수))를 통해 확인할 수 있다.
#그러나 이 id값은 실행할 때마다 바뀐다.

#변수이름은 숫자로 시작할 수 없다.
#언더바 외의 특수문자를 사용할 수 없다.
#대소문자를 구분한다.
#한글을 사용할 수 있다.