#원리금 합계를 복리로 계산하는 식
#원금이 price, 시간은 year, 이자율이 fee이면, 원리금 합계는 = a(1 + r)^n

price = float(input("원금을 입력하세요: "))
fee = float(input("이자율(%)을 입력하세요: ")) / 100  
year = int(input("몇 년 뒤 상환 예정? "))

total = price * (1 + fee) ** year

print("원리금 합계: ", round(total, 2), "원")

#화씨온도 -> 섭씨온도로 변환하기
temp = int(input("화씨온도를 입력하세요: "))
temp1 = (temp - 32) * 5 / 9

print(temp1, "도")

#평균값 구하기 - 세개의 수를 입력 받자
num1 = int(input("1번째 수: "))
num2 = int(input("2번째 수: "))
num3 = int(input("3번째 수: "))

avg = (num1 + num2 + num3) / 3

print("1번째 수:", num1, "2번째 수:", num2, "3번째 수:", num3, "도합 평균:", avg)
