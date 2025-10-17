#2025-10-17
# 이름: 이준영
# 학과: 컴퓨터소프트웨어공학과
# 학년: 2학년
# 파일: py6w_c4

# 함수, 객체, 모듈
# 함수 = 일을 수행하는 코드 덩어리, 더 큰 프로그램을 구축하는 데 사용하는 작은 조각

def print_address():
    print("경상북도 울릉군 울릉읍")
    print("독도이사부길 63")

print_address() # 정의된 함수를 호출

# 반지름을 입력받고, 원의 넓이 구하기
radius = int(input("반지름을 입력하세요:"))

def calculate_area():
    area = 3.14 * radius ** 2
    return area

print("원의 넓이는?", calculate_area())

# 두개의 숫자를 입력받고, 더 작은 숫자가 먼저 오도록 정렬하기
n1 = int(input("n1 숫자:"))
n2 = int(input("n2 숫자:"))

def sort_num(n1, n2):
    if n1 < n2:
        return n1, n2
    else:
        return n2, n1

print(sort_num(n1, n2))

# 여러 개의 값을 넘겨주고 여러 개의 값을 돌려받기
def calc(n3, n4):
    return n3 + n4, n3 - n4, n3 * n4, n3 / n4
n3, n4 = 200, 100
t1, t2, t3, t4 = calc(n3, n4)
print(n3, '+', n4, '=', t1)
print(n3, '-', n4, '=', t2)
print(n3, '*', n4, '=', t3)
print(n3, '/', n4, '=', t4)

# 주급 계산
def weeklyPay(rate, hour):
    if hour > 30:
        money = rate * 30 + 1.5 * rate * (hour - 30)
    else:
        money = rate * hour
    return money

rate = int(input("시급을 입력하세요: "))
hour = int(input("근무 시간을 입력하세요: "))

pay = weeklyPay(rate, hour)
print(f"주급은 {pay}원입니다.")



