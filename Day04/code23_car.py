import os
import code

# 자동차 클래스
class Car:
    __number = '12나 1234'

    def get_number(self):
        return self.__number

    def __init__(self, number = '12나 1234') -> None:
        self.__number = number
        print('__init__')

    # def __new__(cls):
    #     print('__new__')
    #     return super().__new__(cls)

    # 클래스 외부에선 변경불가, 멤버함수로는 내부조작 가능
    def set_number(self, number):
        self.__number = number
        
    def __str__(self) -> str:
        return f'내 차번호는 {self.__number} 입니다.'

yourcar = Car(number = '88호 8888')
print(yourcar)
yourcar.__number = '바뀐번호 1111' #외부에서는 값을 바꿀 수 없음
print(yourcar)
yourcar.set_number = '셋넘버로 바꿈 2222'
print(yourcar)

# mycar = Car()
# print(mycar)
# print(f'제 차는요 아반떼고 번호가 {mycar.get_number()} 입니다.')

# mycar.number = '34나 3456'
# print(mycar)
