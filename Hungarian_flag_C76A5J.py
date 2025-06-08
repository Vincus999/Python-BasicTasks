import turtle

#4. Hungarian flag
def hungary_flag():
    t = turtle.Turtle()
    t.speed(5)

    flag_width = 300
    flag_height = 200
    stripe_height = flag_height // 3

    t.penup()
    t.goto(-flag_width / 2, flag_height / 2)
    t.pendown()
    t.begin_fill()
    t.fillcolor("red")
    for _ in range(2):
        t.forward(flag_width)
        t.right(90)
        t.forward(stripe_height)
        t.right(90)
    t.end_fill()

    t.penup()
    t.goto(-flag_width / 2, flag_height / 2 - stripe_height)
    t.pendown()
    t.begin_fill()
    t.fillcolor("white")
    for _ in range(2):
        t.forward(flag_width)
        t.right(90)
        t.forward(stripe_height)
        t.right(90)
    t.end_fill()

    t.penup()
    t.goto(-flag_width / 2, flag_height / 2 - 2 * stripe_height)
    t.pendown()
    t.begin_fill()
    t.fillcolor("green")
    for _ in range(2):
        t.forward(flag_width)
        t.right(90)
        t.forward(stripe_height)
        t.right(90)
    t.end_fill()

hungary_flag()