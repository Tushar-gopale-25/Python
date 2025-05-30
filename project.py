import turtle
import random
import time

delay = 0.1
sc = 0
hs = 0

# creating a bodies
bodies = []

# creating a screen
s1 = turtle.Screen()
s1.title("Snake Game")
s1.bgcolor("sky blue")
s1.setup(width=600, height=600)

# creating a head
h1 = turtle.Turtle()
h1.speed(0)
h1.shape("circle")
h1.color("red")
h1.fillcolor("blue")
h1.penup()
h1.goto(0, 0)
h1.direction = "stop"

# creating a food
f1 = turtle.Turtle()
f1.speed(0)
f1.shape("square")
f1.color("green")
f1.penup()
f1.ht()
f1.goto(150, 240)
f1.st()
f1.direction = "stop"

# creating a scoreboard
sb = turtle.Turtle()
sb.ht()
sb.penup()
sb.goto(-270, 270)
sb.write("Score: 0 | High Score: 0", font=("Arial", 14, "normal"))


def moveup():
    if h1.direction != "down":
        h1.direction = "up"


def moveleft():
    if h1.direction != "right":
        h1.direction = "left"


def moveright():
    if h1.direction != "left":
        h1.direction = "right"


def movedown():
    if h1.direction != "up":
        h1.direction = "down"


def movestop():
    h1.direction = "stop"


def move():
    if h1.direction == "up":
        y = h1.ycor()
        h1.sety(y + 20)
    if h1.direction == "left":
        x = h1.xcor()
        h1.setx(x - 20)
    if h1.direction == "down":
        y = h1.ycor()
        h1.sety(y - 20)
    if h1.direction == "right":
        x = h1.xcor()
        h1.setx(x + 20)


# event handling
s1.listen()
s1.onkey(moveup, "Up")
s1.onkey(movedown, "Down")
s1.onkey(moveleft, "Left")
s1.onkey(moveright, "Right")
s1.onkey(movestop, "space")


while True:
    s1.update()

    # check collision with border
    if h1.xcor() > 290:
        h1.setx(-290)
    if h1.xcor() < -290:
        h1.setx(290)
    if h1.ycor() > 290:
        h1.sety(-290)
    if h1.ycor() < -290:
        h1.sety(290)

    # check collision with food
    if h1.distance(f1) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        f1.goto(x, y)

        # increase the length of snake
        b1 = turtle.Turtle()
        b1.speed(0)
        b1.penup()
        b1.shape("square")
        b1.color("red")
        b1.goto(1000, 1000)  # move it out of view initially
        bodies.append(b1)

        # increase score
        sc += 10
        if sc > hs:
            hs = sc
        sb.clear()
        sb.write("Score: {} | High Score: {}".format(sc, hs), font=("Arial", 14, "normal"))
        delay = max(0.01, delay - 0.001)

    # move snake bodies
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = h1.xcor()
        y = h1.ycor()
        bodies[0].goto(x, y)

    move()

    # check collision with snake body
    for b in bodies:
        if b.distance(h1) < 20:
            time.sleep(1)
            h1.goto(0, 0)
            h1.direction = "stop"
            for body in bodies:
                body.goto(1000, 1000)
            bodies.clear()
            sc = 0
            delay = 0.1
            sb.clear()
            sb.write("Score: {} | High Score: {}".format(sc, hs), font=("Arial", 14, "normal"))

    time.sleep(delay)

s1.mainloop()
