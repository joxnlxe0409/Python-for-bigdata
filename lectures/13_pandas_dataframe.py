import pandas as pd
import csv

# DataFrame 생성
df1 = pd.DataFrame([[93, 92, 95], [80, 90, 92], [96, 95, 93]], 
                   columns=["국어", "수학", "영어"], 
                   index=["홍길동", "강감찬", "이순신"])

# '국어' 열을 선택
s1 = df1['국어']

# 출력
print(df1)
print(s1)

# 95보다 큰 값인지 확인
print(df1 > 95)

df1.to_csv("score.csv")
