pi = 3.141592
print(pi, "의 소수점 1의 자리 반올림은?", round(pi))
# 아 놓쳤다
name = input("이름 : ")
age = input("나이 : ")
print(f"{name} 님의 나이는 {age} 세군용!")

say = "{0} 님! 나이는 {1} 세군요! 놀랍다"
print(say.format(name, age))