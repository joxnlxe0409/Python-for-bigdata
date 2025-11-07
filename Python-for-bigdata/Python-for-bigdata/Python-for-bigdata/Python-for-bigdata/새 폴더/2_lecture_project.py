# BMI 구하기 -> 몸무게 40kg, 키 150cm 기준 BMI는 어떻게 될까?
weight = 40.0
height = 1.50
bmi = weight / height**2

print("키:", height, "m", "||", "몸무게:", weight, "kg")
print("BMI:", bmi)

#원기둥 부피 구하기
pi = 3.141592
radius = 10
height = 20

volume_of_cylinder = pi * (radius ** 2) * height
print(volume_of_cylinder)

# input 함수
ans = input("이름을 입력하시오: ")
print(str(ans) + "씨 안녕하세요?")
print("파이썬의 세계에 오신 것을 환영합니다.")
age = int(input("나이를 입력하시오: "))
print(age)

num1 = int(input("첫 번째 정수를 입력하시오: "))
num2 = int(input("두 번째 정수를 입력하시오: "))
ans = num1 + num2
print(str(num1) + "과" + str(num2) + "의 합은" + str(ans) + "입니다.")