numbers = input("여러 숫자를 입력해주세요 : ").split()
max_ = max(map(int, numbers))
print("가장 큰 수는 {} 입니다".format(max_))

#split 함수 사용 x