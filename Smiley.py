import turtle


# Smiley with a curved, filled mouth

def smiley():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(5)


    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.begin_fill()
    t.color("pink")
    t.circle(100)
    t.end_fill()


    t.penup()
    t.goto(-35, 35)
    t.pendown()
    t.begin_fill()
    t.color("magenta")
    t.circle(15)
    t.end_fill()


    t.penup()
    t.goto(35, 35)
    t.pendown()
    t.begin_fill()
    t.color("magenta")
    t.circle(15)
    t.end_fill()


    t.penup()
    t.goto(-50, -10)
    t.setheading(-60)
    t.pendown()
    t.begin_fill()
    t.color("magenta")
    t.circle(50, 120)
    t.goto(-50, -10)
    t.end_fill()




smiley()
