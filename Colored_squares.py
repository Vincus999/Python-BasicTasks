import turtle

# Colored square with another colored square

def squares(t, length, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()


def colored_square(t):

    t.penup()
    t.goto(-70, -70)
    t.pendown()
    squares(t, 140, "brown")

    t.penup()
    t.goto(-65, -65)
    t.pendown()
    squares(t, 130, "azure")

    t.penup()
    t.goto(-60, -60)
    t.pendown()
    squares(t, 120, "olive")

    t.penup()
    t.goto(-55, -55)
    t.pendown()
    squares(t, 110, "magenta")

    t.penup()
    t.goto(-50, -50)
    t.pendown()
    squares(t, 100, "maroon")

    t.penup()
    t.goto(-45, -45)
    t.pendown()
    squares(t, 90, "lime")

    t.penup()
    t.goto(-40, -40)
    t.pendown()
    squares(t, 80, "purple")

    t.penup()
    t.goto(-35, -35)
    t.pendown()
    squares(t, 70, "cyan")

    t.penup()
    t.goto(-30, -30)
    t.pendown()
    squares(t, 60, "yellow")

    t.penup()
    t.goto(-25, -25)
    t.pendown()
    squares(t, 50, "pink")


    t.penup()
    t.goto(-20, -20)
    t.pendown()
    squares(t, 40, "blue")

    t.penup()
    t.goto(-15, -15)
    t.pendown()
    squares(t, 30, "orange")

    t.penup()
    t.goto(-10, -10)
    t.pendown()
    squares(t, 20, "red")

    t.penup()
    t.goto(-5, -5)
    t.pendown()
    squares(t, 10, "green")

colored_square(turtle.Turtle())

