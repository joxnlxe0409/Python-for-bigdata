import pandas as pd
import csv

# 파일을 열기
f = open('EXC.csv', encoding='UTF-8')
data = csv.reader(f)
header = next(data)  # 헤더 읽기

# 최고 점수를 기록할 변수
max_score = 0
max_name = ''

# 데이터 읽기
for row in data:
    if float(row[2]) > max_score:  # 점수를 비교하여 최고 점수 찾기
        max_score = float(row[2])
        max_name = row[1]

# 파일을 다 읽고 난 후에 닫기
f.close()

# 최고 점수와 이름 출력
print(max_name, max_score)
