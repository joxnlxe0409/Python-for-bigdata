import pandas as pd

# 시리즈 생성
name_series = pd.Series(['David', 'Daniel', 'Christien', 'Ethan', 'Aaron'])
age_series = pd.Series([20, 17, 23, 12, 35])
sex_series = pd.Series(['M', 'M', 'F', 'M', 'M'])
grade_series = pd.Series([90, 55, 85, 100, 60])

# 시리즈 출력
print(name_series)
print(age_series)
print(sex_series)
print(grade_series)

df = pd.DataFrame({'이름:': name_series, '나이': age_series, '성별': sex_series, '성적': grade_series})
print(df)
