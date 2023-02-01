# 복잡한 계산기 만들기

def calc (option, *args):
    result = 0
    if option == 'add':
        for i in args:
            result += i
    elif option =='sub':
        result = args[0]
        for i in args[1:]:
            result -= i
    elif option == 'mul':
        result = 1
        for i in args:
            result *= i
    elif option == 'div':
        result = args[0]
        for i in args[1:]:
            result /= i
    return result
    

print(calc('add', 4, 3, 7))
print(calc('mul', 42, 128))
print(calc('sub', 8, 7, 17))
print(calc('div', 5, 32))


# 여러값을 리턴할 때는 튜플을 사용한다.
def new_calc(x,y):
    return (x * y , x / y, x+y, x-y)


# 받을 때는 튜플(소괄호)를 생략가능
res1, res2, res3, res4 = new_calc(42,128)
print(res1,res2, res3, res4)    

# elif option == 'mod':
#     for i in args:
#         result %= i
# elif option == 'pow':
#     for i in args:
#         result **= i
# elif option == 'sqrt':
#     for i in args:
#         result **= 0.5
# elif option == 'exp':
#     for i in args:
#         result **= i
# elif option == 'log':
#     for i in args:
#         result **= 1/i
# elif option == 'sin':
#     for i in args:
#         result = math.sin(i)
# elif option == 'cos':
#     for i in args:
#         result = math.cos(i)
# elif option == 'tan':
#     for i in args:
#         result = math.tan(i)
# elif option == 'asin':
#     for i in args:
#         result = math.asin(i)
