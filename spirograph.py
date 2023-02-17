import turtle as t
from turtle import Screen
import random
spiro =t.Turtle()
current_position=spiro.heading()

t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
for _ in range(40):
    spiro.speed("fastest")
    spiro.color(random_color())
    spiro.circle(120)
    spiro.setheading(spiro.heading() + 10)


screen = Screen()
screen.exitonclick()