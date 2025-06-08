import turtle

#5 3x3 checkboard
def draw_square(t, size, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def checkboard():
    t = turtle.Turtle()
    t.speed(5)

    square_size = 50

    start_x = -square_size * 1.5
    start_y = square_size * 1.5

    for row in range(3):
        for col in range(3):
            t.penup()
            t.goto(start_x + col * square_size, start_y - row * square_size)
            t.pendown()

            if (row + col) % 2 == 0:
                color = "brown"
            else:
                color = "white"

            draw_square(t, square_size, color)

checkboard()
