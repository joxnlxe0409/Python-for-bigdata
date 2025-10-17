num = int(input("숫자를 입력하세요: "))
if num == 0:
    print("0")
elif num > 0:
    print("양수입니다.")
else:
    print("음수입니다.")

num1 = int(input("숫자를 입력하세요: "))
if num > 0:
    print("양수입니다.")
    if num % 2 == 0:
        print("짝수입니다.")
    else: 
        print("홀수입니다.")
elif num < 0:
    print("음수입니다.")
else:
    print("0")