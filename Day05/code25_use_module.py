# 모듈 사용
import random

numbers = [i for i in range(1, 46)]
lottery = []

for i in range(6):
    lottery.append(random.choice(numbers))

print(lottery)