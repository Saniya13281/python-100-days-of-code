from turtle import Turtle, Screen
import random

is_race_on = "False"

screen= Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bets", "Which turtle will win the race ? Enter the colour: ")
print(user_bet)
colors =["red","green","blue","yellow","purple","orange"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y= y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = "True"

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win.The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()