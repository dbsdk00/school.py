# def p(*arge) :
#     a = ""
#     for i in arge :
#         a = a + i

# def p(*args) :
#     a = ""
#     for i in args :
#         a = a + i
#     print(a)

def star(a, *args):             # 여러개의 인자를 함수로 받고자 할 때 // *a 라고 써도 되고, *이름 이렇게 써도 되고
    for i in args:
        print(a*i)

star("*", 3)
star("a", 1, 2, 3)