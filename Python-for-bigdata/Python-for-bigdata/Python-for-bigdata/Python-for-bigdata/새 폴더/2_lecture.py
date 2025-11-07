#2025-09-12
# 이름: 이준영
# 학과: 컴퓨터소프트웨어공학과
# 학년: 2학년
# 파일: py2w_c4

weight = 78.2 # '='은 할당 혹은 대입연산자라고 부른다.
print(weight)
weight = 18.2 # 변수의 값은 변경이 가능하다.
print(weight)

x = 100
y = 200
print(x + y)
print(x - y)

n, m = 10, 20
print(n, m)
print(n * m)
print(n / m) # 실수로 출력한다.
print(n // m) # 정수로 출력한다.
print(n % m)

# len() 함수
s1 = 'Hello World!'
print(s1)
print(len(s1)) # s1의 길이를 공백, 특수기호를 포함해서 알려준다.

a1 = 'hello'
a2 = 'world'
print(a1 + a2) # -> helloworld
b1 = '100'
b2 = '200'
print(b1 + b2) # -> 100200

# type() 함수
d1 = 1000
d2 = "hello"
d3 = False
print(type(d1)) # <class 'int'>
print(type(d2)) # <class 'str'>
print(type(d3)) # <class 'bool'>

# 컴퓨터 수치 표현의 한계
print(0.1 + 0.1 == 0.2) # True
print(0.1 + 0.1 + 0.1 == 0.3) # False
print(0.1 + 0.1 + 0.1) # 0.30000000000000004

print("Hello\tWorld!") # Hello   World!
print("Hello".upper()) # HELLO
print("Hello".lower()) # hello

message = '철수가 "안녕하세요"라고 말한다.'
print(message)

print('철수가 \'안녕\'이라고 말했습니다.') # 이스케이프 
print('안녕\n 우리 다시 만나자.') # 줄바꿈 \n
print('안녕\t 우리 다시 만나자.') # 탭 문자 \t

# 100 뒤에 문자열 '원'을 붙여서 출력하면?
print(str(100),'원')
print('100 원')
baek = 100
print(str(baek) + '원')






