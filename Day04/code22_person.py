# 클래스 생성
class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    def walk(self):
        print('걷기')
    def run(self, option):
        if option == 'Fast':
            print(f'{self.name}은 전속력으로 달립니다!')
        else:
            print(f'{self.name}은 천천히 달립니다!')
    def stop():
        print('멈춰!')


Tarel = Person()
Tarel.name = '민성'
Tarel.height = 170
Tarel.gender = 'male'
Tarel.blood_type = 'B'


print(f'{Tarel.name}의 혈액형은 {Tarel.blood_type} 입니다.')

Tarel.walk()
Tarel.run('Fast')


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



