# 구구단 프로그램
for x in range(1, 10):
    for y in range(1, 10):
        print(f'{y} x {x} = {x * y :>2}', end ='    ')    
    print()
    