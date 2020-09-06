import turtle
import time

import random 

score = 0
high_score = 0
delay = 0.10
# Windows config
windows = turtle.Screen()
windows.title("Snake en 30 minutos")
windows.bgcolor("black")
windows.setup(width=300,height=300)

# Text
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score 0        High score 0", align="center", font=("Courier", 20, "normal"))

# Snake
## Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

## Body
body_now = []

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(50,60)

# Functions
def arriba():
    head.direction = "up"

def abajo():
    head.direction = "down"

def izq():
    head.direction = "left"

def der():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard
windows.listen()
windows.onkeypress(arriba,"Up")
windows.onkeypress(abajo,"Down")
windows.onkeypress(izq,"Left")
windows.onkeypress(der,"Right")

while True:
    windows.update()

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hidden
        for body in body_now:
            body.goto(4000,4000)

        # Clean lists
        body_now.clear()

    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        body_new = turtle.Turtle()
        body_new.speed(0)
        body_new.shape("square")
        body_new.color("white")
        body_new.penup()
        body_now.append(body_new)
        
        score +=10

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score {}  High Score {}".format(score,high_score), align="center", font=("Courier",24))
    
    body_total = len(body_now)
    for index in range(body_total -1, 0, -1):
        x = body_now[index-1].xcor()
        y = body_now[index-1].ycor()
        body_now[index].goto(x,y)

    if body_total > 0:
        x = head.xcor()
        y = head.ycor()
        body_now[0].goto(x,y)

    time.sleep(delay)
    move()


turtle.mainloop()