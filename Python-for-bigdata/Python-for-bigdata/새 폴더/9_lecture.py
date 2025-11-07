#2025-11-07
# 이름: 이준영
# 학과: 컴퓨터소프트웨어공학과
# 학년: 2학년
# 파일: py9w_c4

# 오늘 내용: 딕셔너리, 세트, 파일
# 딕셔너리: key + value
# 비상 연락망
phone_book = {}  # 빈 딕셔너리 생성
phone_book["홍길동"] = "010-1234-5678"
print(phone_book)
phone_book = {"경찰서": "112"}
print(phone_book)
phone_book["강감찬"] = "010-9876-5432"
phone_book["단군"] = "123-4567-8901"
print(phone_book)
print(phone_book.keys())
print(phone_book.items())
for name, phone_num in phone_book.items():
    print(name, ":", phone_num)

person_dic = {"Name": "홍길동", "Age": 27, "Class": "초급"}
print(person_dic)
print(person_dic['Name'])
print(person_dic['Age'])

stores = {"커피음료": 7, "펜": 3, "우유": 8}
for names in stores.keys():
    print("물건의 종류:", names)
ques = input("물건 이름을 입력하세요: ")
if ques in stores:
    print(f"{ques}의 재고는 {stores[ques]}개 입니다.")
else:
    print(f"{ques}는 재고에 없습니다.")

numbers = {2, 1, 3}
print(numbers)

set[1, 2, 3, 1, 2]
set("abcdefa")

# 집합 항목 검색
numbers1 = {2, 1, 3}
ques1 = int(input("숫자를 입력하세요:"))
if ques1 in numbers1:
    print(f"입력하신 {ques1}는 집합 안에 존재합니다.")
else:
    print(f"입력하신 {ques1}은 집합 안에 존재하지 않습니다.")

numbers2 = {2, 1, 3}
for x in numbers2:
    print(x, end=" ")
numbers2.add(4)
print(numbers2)
numbers2.remove(4)
print(numbers2)

# 파일: 컴퓨터의 저장장치 내에 데이터를 저장하기 위한 논리적 단위
