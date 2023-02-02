# 클래스 생성
class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'


    # 1. 초기화 추가
    def __init__(self, name, height, gender, blood_type):
        self.name = '홍길동'
        self.height = '170'
        self.gender = 'male'
        self.blood_type = 'A'

    def walk(self):
        print('걷기')
    def run(self, option):
        if option == 'Fast':
            print(f'{self.name}은 전속력으로 달립니다!')
        else:
            print(f'{self.name}은 천천히 달립니다!')
    def stop(self):
        print(f'{self.name}멈춰!')

# 2. 생성자외 매직메서드(펑션) __str__
def __str__(self)-> str:
    return f'출력 : 이름은 {self.name}, 성별은 {self.gender}, {self.height}'

Tarel = Person()
# Tarel.name = 'Tarel'
Tarel.height = 170
Tarel.gender = 'male'
Tarel.blood_type = 'B'


print(f'{Tarel.name}의 혈액형은 {Tarel.blood_type} 입니다.')

Tarel.run('Fast')

# 1. 초기화 후 객체생성
hong = Person()
hong.run('Slow')
print(hong)


# 2. 파라미터를 받는 생성자
hong = Person('홍길동', 170, 'female', 'A')
print(f'{hong.name}의 혈액형은 {hong.blood_type} 입니다.')

print(hong.name)
print(hong.height)
print(hong.gender)
print(hong)

# 3. 메소드
hong = Person(f'self홍길동', 170, 'female')

class character:
    name = ''
    position = ''
    max_hp = 200

    def attack1(self, option):
        print(f'{self.name} 은 {option}을 시전!')
    def attack2(self, option):
        print(f'{self.name} 은 {option}을 시전!')
    def attack3(self, option):
        print(f'{self.name} 은 {option}을 시전!')
    def attack4(self, option):
        print(f'{self.name} 은 {option}을 시전!')
        
Rein = character()
Rein.name = '라인하르트'
Rein.position = ''
Rein.max_hp = 625



