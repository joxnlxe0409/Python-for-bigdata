import random

while True:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = num1 + num2

    print(num1, "+", num2)
    ans = int(input("답 입력:"))

    if ans == result:
        print("정답입니다.")
    else:
        print("정답은: ", result, "입니다. 다음번엔 잘할 수 있죠?")

