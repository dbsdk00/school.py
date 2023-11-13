def p(*args):
    a = ""
    for b in args:
        a = a + b
    print(a)

p("*")
p("*", "@")
p("*", "@", "&")