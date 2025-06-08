import turtle

#3. Stickman
def stickman():
    t = turtle.Turtle()
    t.speed(5)

    # Draw head
    t.penup()
    t.goto(0, -50)  # Position the turtle for the head
    t.pendown()
    t.circle(50)  # Head radius

    # Draw body
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.goto(0, -200)  # Body length

    # Draw left arm
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.goto(-70, -100)  # Left arm length

    # Draw right arm
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.goto(70, -100)  # Right arm length

    # Draw left leg
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.goto(-50, -300)  # Left leg length

    # Draw right leg
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.goto(50, -300)  # Right leg length

stickman()
