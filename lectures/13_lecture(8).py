import pandas as pd

weather = pd.read_csv('weather.csv', index_col=0)
print(weather.describe())

print('----------평균분석----------')
print(weather.mean)

print('----------표준편차----------')
print(weather.std)

print(weather.count)
print(weather['최대 풍속'].count)

print(weather.count()[['최대 풍속, 평균 풍속']])