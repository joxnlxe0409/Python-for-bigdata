#2025-11-28
# 이름: 이준영
# 학과: 컴퓨터소프트웨어공학과
# 학년: 2학년
# 파일: py11w_c4
 
# matplotlib 시각화 도구 -> 간단한 막대 그래프, 선 그래프, 산포도
import matplotlib.pyplot as plt

x = [x for x in range(-20, 20)]
y1 = [2*t for t in x]
y2 = [t**2 + 5 for t in x]
y3 = [-t**2 - 5 for t in x]

plt.plot(x, y1,'r--', x, y2, 'g^-', x, y3, 'b*:')
plt.axis([-30, 30, -30, 30])
plt.show()