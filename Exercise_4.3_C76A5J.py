import turtle

#1 Square
#2. Square length

def square(t, length):
    for nn in range(4):
        t.forward(length)
        t.left(90)

comenius_logo = turtle
square(comenius_logo, 100)
square(comenius_logo, 200)


def bob():
    bob=turtle
    square(bob, 100)
bob()

#3 n-sided polygon
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)


polygon(comenius_logo,8, 80)

#4. Circle
import math

def circle(t, r):
    circumference  = 2 * math.pi * r
    n = 100
    length = circumference/n
    polygon(comenius_logo, n, length)


r = 50
circle(comenius_logo, 50)

#5. Arc
def polygon_arc(t, n, length, angle):
    step_angle = 360 / n
    steps = int(n * angle / 360)
    for _ in range(steps):
        t.forward(length)
        t.left(step_angle)

def arc(t, r, angle):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon_arc(comenius_logo, n, length, angle)

arc(comenius_logo, 75, 270)




