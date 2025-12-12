#2025-11-28
# 이름: 이준영
# 학과: 컴퓨터소프트웨어공학과
# 학년: 2학년
# 파일: py11w_c4
 
# matplotlib 시각화 도구 -> 간단한 막대 그래프, 선 그래프, 산포도
import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]

# x축 = years 값 
# y축 = gdp 값
plt.plot(years, gdp, color='green', marker = 'o', linestyle='solid')

#제목 설정
plt.title("GDP Per Capita")

# y축에 레이블을 붙인다.
plt.ylabel("dollars")
plt.xlabel("years")
plt.savefig("gdp_per_capita.png", dpi = 600) # png로 저장
plt.show()
