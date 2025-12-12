import csv

with open('weather.csv', encoding='utf-8') as f:
    data = csv.reader(f)
    header = next(data)
    for row in data:
        print(row[3], end='')
