# 원하는 단을 입력받아, 구구단이 출력되도록.
dan = int(input("단: "))
i = 1

while i <= 9:
    print("%s * %s = %s" % (dan, i, dan * i))
    i = i + 1


