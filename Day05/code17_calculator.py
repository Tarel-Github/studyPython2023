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
    
def new_calc(x,y):
    return (x * y , x / y, x+y, x-y)
