PASSWORD = "dongyang"  

while True:
    attempt = input("암호를 입력하세요: ")
    if attempt == PASSWORD:
        print("Login Successful.")
        break
    print("Try again.")
