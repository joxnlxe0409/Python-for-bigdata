#2025-10-10
# 이름: 이준영
# 학과: 컴퓨터소프트웨어공학과
# 학년: 2학년
# 파일: py5w_c4

for i in "Hello":
    print("i = ", i)

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("9 x", i, " =", 9 * i)

for i in range(5):
    print("반복해요.")
    print("이 일도 반복해요.")

for i in range(3):
    print("파이썬 주식회사의")
    print("방문을 환영합니다!")

# range() 함수에 list() 함수를 적용
print(list(range(10)))

# range(스타트값, 스탑값, 건너뛰기값)
for i in range(0, 4, 2): # 0-> 스타트, 4-> 스탑, 2씩 건너뛰기
    print("Hello")

for i in range(1, 6, 1):
    print(i, end = " ") # end = " "로 지정하면 가로 공백으로 나열한다. 줄바꿈 X

# 10부터 1까지 -1씩 감소하기
for i in range(10, 0, -1):
    print(i)

# 팩토리얼 값 구하기
n = int(input("정수를 입력하세요:"))
fact = 1
for i in range(1, n + 1):
    fact = fact * i

print(n, "팩토리얼은", fact)

# While 반복문
count = 1
s = 0

while count <= 10:
    s = s + count
    count = count + 1

print("합계는: ", s)

# for문으로 바꿔보기
sum = 0
for i in range(1, 11):
    sum = sum + i

print("합계는: ", sum)

# Continue
st = 'I love Python'
for ch in st:
    if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        continue
    print(ch, end = ' ')

# format() 함수
name = "Joon"
age = 22
print("My name is {} and I am {} years old".format(name, age))
print("My name is {0} and I am {1} years old. {0}'s age is {1}".format(name, age))

pi = 3.141592
print("The value of pi is {:.1f}.".format(pi))
print("The value of pi is {:.2f}.".format(pi))
print("The value of pi is {:.3f}.".format(pi))
print("The value of pi is {:.4f}.".format(pi))
print("The value of pi is {:.5f}.".format(pi))
print("The value of pi is {:.6f}.".format(pi))

number = 12345
print("The number is {:d}.".format(number))

for i in range(2, 11, 2):
    print("{0:3d} {1:4d} {2:5d}".format(i, i*i, i*i*i))

print("위도: {lat}, 경도: {long}".format(lat = '35.17N', long = '129.07E'))

# 큰 수를 추력하는 경우 1000 단위 쉼표 출력
print('{:,}'.format(123456789))