import turtle
t = turtle.Turtle()

def k(col):
    t.color(col)
    t.begin_fill()
    t.circle(100)
    t.left(120)
    t.end_fill()

k("red"), k("yellow"), k("blue")