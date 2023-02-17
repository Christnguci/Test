from turtle import Screen
import turtle as t
import random
random_step=t.Turtle()
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

random_step.pensize(5)
random_step.speed("normal")
colours=["light steel blue","sky blue","dark cyan","medium spring green","beige","gold","moccasin","bisque"]
direction = [0,90,180,270]
for _ in range(200):
    random_step.color(random_color())
    random_step.forward(15)
    random_step.setheading(random.choice(direction))
# go back, go forward, turn left, turn right
screen=Screen()
screen.exitonclick()