# 자동차 클래스
class Car:
    number = '15나 1234'

    def get_number(self) -> str:
        return self.number

    def __init__(self) -> None:
        return ('__init__')
    def __new__(cls):
        print('__new__')
        return super().__new__(cls)
    def __str__(self) -> str:
        return f'차번호는 {self.number()} 입니다.'

        