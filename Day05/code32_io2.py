# 다중입력
# a, b= input('두 영단어를 입력하세요 > ').split()

# print(a)
# print(b)

# 완전 다중입력(개수가 몇개든 상관없이)

inputs = list(map(str, input('뭐든지 입력해보거라 > ').split()))

print(inputs)

inputs = list(map(int, input('정수를 입력해보거라 > ').split()))

print(inputs)