# 콘솔출력 다시
# 이스케이프 캐릭터(탈출 문자)
print('1. Hello.\r\nWorld')
print('2. Hello.\nWorld')       #위와 같지만 주로 이걸 사용
print('3. Hello.\n\tWorld')
print('4. Hello.\n\t\bWorld')
print('5. Hello.\n\'World\'')   #문자열 안에 작은따옴표를 넣는 기능
print('6. Hello. "World"')
print('7. Hello.\"World\"')     #위와 같지만 밖에 사용한 따옴표가 작은 따옴표가 아닌 큰 따옴표면 사용함
print('7. Hello.\\World')        #역슬레시를 문자열에 넣기위한 것으로 파이썬은 역슬레시를 하나만 적어도 나옴

print('8. Hello\0')             #널문자 표현

# 문자열포맷팅 - 옛방식
# %로 포멧코드를 시작
me = '저'
name = 'Tarel'
age = 20
print('%s는 %s입니다. %d대 입니다.'%(me, name, age))

print(f'{254.112233:.2f}')
print('%9.2f' %(254.112233))





