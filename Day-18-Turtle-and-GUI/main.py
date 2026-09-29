# from turtle import Turtle,Screen
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("VioletRed")
# # tim.forward(100)
# # tim.right(90)
# # tim.forward(100)
# # tim.right(90)
# # tim.forward(100)
# # tim.right(90)
# # tim.forward(100)
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
#
#
#
#
# screen = Screen()
# screen.exitonclick()


# from turtle import Turtle,Screen
# import random
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue")
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side_n in range(3,11):
#     timmy.color(random.choice(colours))
#     draw_shapes(shape_side_n)
#
#
#
# screen = Screen()
# screen.exitonclick()

import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours=(r, g, b)
    return colours

directions = [0,90,180,270]
timmy.speed("fastest")
timmy.pensize(15)

for _ in range(200):
    timmy.setheading(random.choice(directions))
    timmy.forward(20)
    timmy.color(random_color())

screen = Screen()
screen.exitonclick()
