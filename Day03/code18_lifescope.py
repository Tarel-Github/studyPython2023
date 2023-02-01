# 라이프 스코프
a = 1

def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

# global 키워드

a = 1
def vartest():
    global a
    a = a + 1
    return a

a = vartest()
print(a)