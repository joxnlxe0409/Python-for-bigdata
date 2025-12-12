#2025-12-12
# 이름: 이준영
# 학과: 컴퓨터소프트웨어공학과
# 학년: 2학년
# 파일: py13w_c4

#엑셀보다 빠른 일처리는 판다스로..
import pandas as pd

df = pd.read_excel('EXC.xlsx') # 엑셀 불러오기
print(df.head(3)) # 상위 3개 행만 출력한다.
print(df) # 전체 행이 모두 출력된다.

df.to_csv('EXC.csv')
df1 = pd.read_csv('EXC.csv')
print(df1.head(2))