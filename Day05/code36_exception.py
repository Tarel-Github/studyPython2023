# 예외처리
def add(a, b):
    return a + b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

x, y = input('두 수를 입력하세요 > ').split()
x = int(x)
y = int(y)

try:
    print(div(x, y))
# except ZeroDivisionError as e:
#     print('0으로 나눌 수 없음')
except Exception as e:
    print(e)
    #exit()
finally:
    print("계산이 완료되었습니다.")


# print(add(x, y))
# print(mul(x, y))
