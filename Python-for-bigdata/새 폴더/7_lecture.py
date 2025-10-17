#2025-10-17
# 이름: 이준영
# 학과: 컴퓨터소프트웨어공학과
# 학년: 2학년
# 파일: py7w_c4

# 리스트란? 여러 개의 데이터를 하나로 묶어서 저장하는 것
heights = [170, 188, 155, 167, 175]
print(heights)

bts = ["V", "Jin", "Suga", "JungKook"]
bts = bts + ["RM"]
print(bts)

countries = ["USA", "CANADA"] + ["KOREA", "JAPAN", "CHINA"]
print(countries)

num_list = [0, 1, 2] * 3
print(num_list)

numbers = [1, 2, 3] + [4, 5, 6]
print(numbers)

foods = ["Beef", "Pork", "Chicken"]
print("Beef" in foods)
print("Beef" not in foods)

n_list = [100, 200, 300, 400, 500]
print(len(n_list))
print(min(n_list))
print(max(n_list))
print(sum(n_list))
print(sum(n_list)/len(n_list))

t_list = list((10, 20, 30))
print(t_list)
t_list.append(40)
print(t_list)