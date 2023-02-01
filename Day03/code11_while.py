# while문
hit = 0 #변수 초기화

while hit < 1000:
    hit += 1
    print(f"나무를 {hit}번 찍었습니다")
    if hit == 10:
        print('나무가 박살났습니다!')
        break
    else: 
        print("도끼의 내구도가 감소하였습니다.")
print("목재를 흭득하였습니다.")
