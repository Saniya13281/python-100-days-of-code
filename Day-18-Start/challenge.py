import turtle as t
import random

tim= t.Turtle()
t.colormode(255)
tim.speed("fastest")

def color_mode():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colours = (r, g, b)
    return colours

def draw_spirograph(size_of_gap):
    draw = int(360 / size_of_gap)
    for _ in range(draw):
        tim.color(color_mode())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)



















my_screen= Screen()
my_screen.exitonclick()