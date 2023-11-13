i = 0
while True :
    print("{}번째 반복문 입니다.".format(i))
    i += 1
    j = input("종료하시겠습니까? (y) : ")
    if j in ["y", "Y"]:
        print("종료합니다.")
        break