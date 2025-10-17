#2025-09-19
# 이름: 이준영
# 학과: 컴퓨터소프트웨어공학과
# 학년: 2학년
# 파일: py3w_c4

x = y = 100
n1, n2 = 100, 200

print(x)
print(y)
print(n1)
print(n2)

# 몫과 나머지 연산하기
#p = int(input("나누어질 숫자를 입력하세요: "))
#q = int(input("나눌 숫자를 입력하세요: "))

#print("몫:", p // q)
#print("나머지:", p % q)

# 거듭제곱
print(2**2) # 4
print((2**2)**3) # 64

# 복합 할당 연산자 +=, -=, *=, /=, %=, //=, **= 
num = 200
num += 100
print(num)

num -= 100
print(num)

num *= 20
print(num)

num /= 2
print(num)

num //= 2
print(num)

num %= 300
print(num)

num **= 2
print(num)

# 비교 연산자 <, >, <=, >=, ==, !=
m = 1
n = 2

print(m < n)
print(m > n)
print(m <= n)
print(m >= n)
print(m == n)
print(m != n)

# 논리 연산자 and, or, not
o = 10
u = 20

print(o < u and o < 11)   # True  (둘 다 참)
print(o > u or o == 1)    # False (둘 다 거짓)
print(not (o == 10))      # False (o == 10 이 참이므로 not → False)
