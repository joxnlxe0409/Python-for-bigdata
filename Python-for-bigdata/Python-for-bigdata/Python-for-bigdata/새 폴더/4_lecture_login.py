# 아이디와 비밀번호를 입력받고 로그인 여부를 알아보자.
id1 = "ilovepython"
pw1 = "python"
id = str(input("아이디를 입력하세요: "))
if id == id1:
    pw = str(input("비밀번호를 입력하세요: "))
    if pw == pw1:
        print("로그인이 완료되었습니다.")
else:
    print("아이디를 찾을 수 없습니다.")