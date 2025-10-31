import random

print(random.random()) # 0 이상 1 미만의 실수를 반환
print(random.randint(1, 7)) # 1 이상 7 이하의 정수를 반환
print(random.randrange(7)) # 0 이상 7 미만의 정수를 반환
print(random.randrange(1, 7)) # 1 이상 7 미만의 정수를 반환
print(random.randrange(0, 10, 2)) # 0, 2, 4, 6, 8 중 하나 반환

a = [10, 20, 30, 40, 50]
random.shuffle(a) # a의 리스트 순서를 무작위로 섞음
print(a)
print(random.choice(a)) # a의 리스트 원소 중 하나를 고름

