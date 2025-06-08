import turtle
import random

#Spiral colored squares
def spiral_squares():
    t = turtle.Turtle()
    t.speed(10)

    colors = ["red", "royalblue", "green", "purple", "orange", "yellow", "peachpuff", "cyan", "maroon", "lime", "cyan", "magenta", "olive", "wheat", "crimson"]
    size = 20
    increment = 15

    size = 20  # Initial square size
    last_color = None

    for i in range(15):
        t.color(colors[i % len(colors)])
        t.begin_fill()

        for _ in range(4):
            t.forward(size)
            t.right(90)
        t.end_fill()

        current_color = random.choice(colors)
        while current_color == last_color:
            current_color = random.choice(colors)

        t.right(20)
        size += increment


spiral_squares()
