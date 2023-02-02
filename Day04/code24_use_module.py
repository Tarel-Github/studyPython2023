#모듈 사용
import math as m        #수학모듈 사용하기, math를 m으로 줄인다.
import code22_person as p
from code23_car import Car


print(m.pi)

print(m.tan(0))
print(m.ceil(3.78))
print(2 ** 10)
print(m.pow(2, 10))

#우리가 만든 모듈 사용
me = p.Person('홍길순', 155, '여자')
print(me)



mycar =Car()
print(mycar)