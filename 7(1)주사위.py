import random

def r(a, b):                # 주사위 면 수, 주사위 돌릴 횟수
    for i in range(1, b + 1):
        n = random.randint(1, a)
        print(f"{a}면 주사위 굴린 결과{r} : {n}")

r(6,6)