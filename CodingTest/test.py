# import math

# def solution(radius):
#     return math.pi*radius**2

# input = int(input('반지름을 입력하세요 > '))
# print(f'원의 넓이는 {solution(input)} 입니다.')

#====================================

# def solution(name):
#     if name == 'Mercury':
#         return '한글 명칭은 수성 입니다.'
#     elif name == 'Venus':
#         return '한글 명칭은 금성 입니다.'
#     elif name == 'Earth':
#         return '한글 명칭은 지구 입니다.'
#     elif name == 'Mars':
#         return '한글 명칭은 화성 입니다.'
#     elif name == 'Jupiter':
#         return '한글 명칭은 목성 입니다.'
#     elif name == 'Saturn':
#         return '한글 명칭은 토성 입니다.'
#     elif name == 'Uranus':
#         return '한글 명칭은 천왕성 입니다.'
#     elif name == 'Neptune':
#         return '한글 명칭은 해왕성 입니다.'
#     else:
#         return '잘못된 입력입니다. 다시 입력해주세요'

# input = str(input('행성 이름을 영어로 입력하세요 > '))
# print(solution(input))

#====================================

# def solution(data):
#     a = data.split(' ')
#     for i in range(len(a)):
#         if i % 2 == 1:
#             a[i] = a[i].upper()
#     return a

# input = str(input('영어문장을 입력하세요 > '))
# print(f'{solution(input)} / {len(solution(input))}')

#====================================
def solution(data):
    a = data.split(' ')
    a.sort(reverse=True)
    b = ' '.join(s for s in a)
    return b

input = str(input('숫자를 입력하세요(예시: 2 3 1 4) > '))
print(solution(input))

#====================================

# def solution(data):
#     a = ('')
#     for i in range(1, 10):
#         a = a + str(i * data) + ' '
#     return a

# input = int(input('구구단 단 번호를 입력하세요 > '))
# print(solution(input))





