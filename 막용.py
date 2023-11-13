numbers = input("여러 숫자를 입력해주세요 : ")
numbers_ = numbers.split()
max_ = max(map(int,numbers_)) #map은 3 7 1 9를 입력하면[3,7,1,9]리스트를 만들어줌, max 는 9를 반환해줌
print("가장 큰 수 : ", max_)