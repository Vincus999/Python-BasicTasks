import turtle

# Saw

def saw():
    t = turtle.Turtle()
    t.speed(5)

    t.penup()
    t.goto(-150,-150)
    t.pendown()
    t.begin_fill()
    t.color("brown")

    for _ in range(2):
        t.forward(50)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.end_fill()


    t.penup()
    t.goto(-100, -150)
    t.pendown()

    t.pensize(3)
    t.begin_fill()
    t.color("gray")

    for _ in range(5):
        t.left(45)
        t.forward(25)

        t.right(90)
        t.forward(25)

        t.left(45)
        t.forward(25)

    t.left(135)
    t.forward(15)
    t.forward(30)
    t.left(45)
    t.forward(270)
    t.left(30)
    t.forward(20)
    t.end_fill()

saw()
