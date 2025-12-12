#각 달의 평균 풍속을 구하기 위해 12 개 항목을 가진 리스트 monthly_wind를 만든다.
#각 달마다 측정 데이터가 존재하는 일수를 담을 12개 항목의 리스트 days_counted도 함께 만든다.
#각 행 데이터를 읽어 해당 데이터가 몇 월의 데이터인지 확인하고, 풍속 정보가 있는지 확인한다. 여기서
#첫 열에 있는 2012-01-24와 같은 문자열의 [5:7]을 읽으면 달의 정보가 된다. 풍속이 존재하면
#해당 월의 풍속 정보에 이 데이터를 더하고, 고려된 일 수 days_counted도 해당 월 정보를 증가시킨다.
#마지막으로 누적된 풍속 데이터를 계산된 일수로 나누어 월 평균 풍속을 구한다.

import csv
import matplotlib.pyplot as plt

# CSV 파일 열기
with open('weather.csv', encoding='utf-8') as f:
    data = csv.reader(f)
    header = next(data)  # 헤더 건너뛰기

    # 월별 풍속 누적값과 일수 카운트를 위한 리스트
    monthly_wind = [0 for _ in range(12)]
    days_counted = [0 for _ in range(12)]

    # 각 행에 대해 데이터 처리
    for row in data:
        month = int(row[0][5:7])  # 날짜에서 월 추출 (예: 2012-01-24 -> 01)
        
        if row[3] != '':  # 풍속 데이터가 비어있지 않으면
            wind = float(row[3])  # 풍속 값을 실수로 변환
            monthly_wind[month - 1] += wind  # 해당 월에 풍속 값 추가
            days_counted[month - 1] += 1  # 해당 월의 일 수 증가

    # 월별 평균 풍속 계산
    for i in range(12):
        if days_counted[i] > 0:  # 해당 월의 데이터가 있을 때만 계산
            monthly_wind[i] /= days_counted[i]

# 월별 평균 풍속 출력
print("Average Wind Speed per Month:")
for i in range(12):
    print(f"{i+1}month: {monthly_wind[i]:.2f} m/s")

# 그래프 그리기
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.plot(months, monthly_wind, marker='o', color='b', linestyle='-', markersize=8)  # 선 그래프
plt.title('Average Wind Speed per Month')  # 제목 설정
plt.xlabel('Month')  # x축 레이블 설정
plt.ylabel('Average Speed (m/s)')  # y축 레이블 설정
plt.xticks(rotation=45)  # x축 라벨 회전
plt.grid(True)  # 그리드 표시

# 그래프 출력
plt.show()
