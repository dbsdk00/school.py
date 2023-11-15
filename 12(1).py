def t(w, h):
    return w * h * 1/2

def b(w, h):
    return w * h

def p(w, h):
    print(f"가로{w} 세로{h}인 삼각형의 넓이 : ", t(w, h))
    print(f"가로{w} 세로{h}인 삼각형의 넓이 : ", b(w, h))

if __name__ == "__main__":
    print(3, 5)
