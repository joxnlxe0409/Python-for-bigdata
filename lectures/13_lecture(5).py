import csv

# 파일을 UTF-8로 열고 처리
with open('weather.csv', encoding='utf-8') as f:
    data = csv.reader(f)
    header = next(data)  # 첫 번째 줄은 헤더이므로 건너뛰기
    max_wind = 0.0  # 최대 풍속 초기화
    
    # 각 행에서 풍속 값을 읽어 최대 풍속 계산
    for row in data:
        if row[2] == '':  # 풍속 값이 비어있다면 0으로 처리
            wind = 0
        else:
            wind = float(row[2])  # 풍속 값이 있으면 실수로 변환
        
        if max_wind < wind:  # 최대 풍속 업데이트
            max_wind = wind

# 최대 풍속 출력
print(f'지난 10년간 울릉도의 최대 풍속은: {max_wind} 입니다.')
