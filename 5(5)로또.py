# import random

# user = int(input("출력할 로또번호 개수 : "))

# for i in range(1, user + 1):
#     num = random.sample(range(1, 46), 6)            # 1부터 45까지의 숫자를 랜덤하게 6개씩 출력
#     print(f"{i} : {num}")


# # # 이렇게도 가능합니다
from random import *

for i in range(1, 7):
    print(f"{i}번째 자리는 : ", end = "")
    print(randint(1, 45))