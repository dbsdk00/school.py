a = int(input("피라미드의 높이 : "))

if a % 2 == 1:
    for i in range(0, a):
        print(" " * (a - i), end = "")
        print("*" * (2 * i + 1))
else :
    print("홀수 입력하라고")
    a = int(input("홀수를 입력하세요 : "))
    if a % 2 == 1 :
        for i in range(0, a):
            print(" " * (a - i), end = "")
            print("*" * (2 * i + 1))
    else :
        print("꺼져 걍;;")
