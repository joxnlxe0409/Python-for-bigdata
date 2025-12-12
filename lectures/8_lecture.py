#2025-10-24
# 이름: 이준영
# 학과: 컴퓨터소프트웨어공학과
# 학년: 2학년
# 파일: py8w_c4
 

# any() 함수
# 0과 공백 문자열은 False로 간주한다.
a_list = [10, 20, 30] 
b_list = [0, 1, 2, 3, 4] 
c_list = [0, ""] 

print(any(a_list)) # True
print(any(b_list)) # True
print(any(c_list)) # False

# all() 함수
# 모든 원소가 참인 경우에 True를 반환
print(all(a_list)) # True
print(all(b_list)) # False
print(all(c_list)) # False

# Fruit List
fruits = []
for i in range(3):
    ans = input("What is your favourite fruit?")
    fruits.append(ans)

ans = input("Fruit Name:")
if ans in fruits:
    print('The fruit you have selected is your favourite.')
else:
    print('The fruit you have selected is not your favourite.')

# Indexing & Slicing
# Index: Used when getting a data from a list. ex) letters[0], letters[1]
# Slicing: Used when making a new list. ex) letters[start, end, ++ or --]
slist = ['kim', 178.9, 'park', 173.5, 'lee', 180.4 ]
slist[3] = 190.0
print(slist)
slist[2:4] = ['kang', 160.0]
print(slist)

# append(), insert() 함수 
# append(): 리스트의 뒤에 추가
# insert(): 지정된 index 위치에 항목 추가
slist.insert(4, 'Hong')
slist.insert(5, 150.0)
print(slist)

# remove(), pop() 메소드, del 명령
# remove(): 리스트에서 지정된 항목을 삭제
cities = ['Seoul', 'Busan', 'Incheon', 'Daegu', 'Jeju']
print(cities)
cities.remove('Daegu')
print(cities)

# pop(): 리스트의 마지막 항목을 삭제하여 그 값을 반환
cities.pop(1) 
print(cities)
cities_1 = cities.pop()
print(cities, cities_1)

# del 명령어: 인덱스 사용해서 해당 항목을 메모리에서 삭제
del cities[0]
print(cities)

# 특정 항목의 위치를 구해보자
colour = ['red', 'blue', 'black', 'green']
print(colour.index('red'))

# 리스트 모든 항목을 한 번씩 방문
for c in colour:
    print(c) 

# sort(): 항목들을 크기 순으로 나열
numbers = [10, 2, 3, 7, 5, 1, 8, 9, 4, 6]
numbers.sort() # 오름차순
print(numbers)
numbers.sort(reverse=True) # 내림차순
print(numbers)

# sort() 문자열:
bts = ['V', 'J-Hope', 'Suga', 'JungKook']
bts.sort()
print(bts)
# sorted():
new_bts = sorted(bts)
print(new_bts)

# list()
s = 'python'
str_list = list(s)
print(str_list)

print('s[0]=', s[0])
print('s[1]=', s[1])
print('s[-1]=', s[-1])
print('s[0:2]=', s[0:2])
print('s[-2:]=', s[-2:])
print('s[-1:-3:-1]=', s[-1:-3:-1])

# split() 메소드
num_s = '11 12 13 14 15'
num_list = num_s.split()
print(num_list)

heights = [178, 173, 190, 163, 150]
heights.sort()

print("이 중에서 가장 작은 값은: ", heights[0])
print("이 중에서 가장 큰 값은: ", heights[-1])

print("이 중에서 가장 작은 값은: ", min(heights))
print("이 중에서 가장 큰 값은: ", max(heights))

alist = ['Kim', 'Lee', 'Park', 'Hong']
blist = alist
blist[1] = 'Choi'
print(alist)

# 리스트 함축 Comprehension
s = [x**2 for x in [1, 2, 3, 4, 5]]
print(s)
s1 = [x for x in range(10)]
s2 = [x * x for x in range(10)]
print(s1, s2)

st = "Hello World"
st1 = [x.upper() for x in st]
print(st)
print(st1)

ab = [x for x in range(10) if x % 2 == 0]
print(ab)
ab1 = [x ** 2 for x in range(10) if x % 2 == 0]
print(ab1)