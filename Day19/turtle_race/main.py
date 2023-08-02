from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtle_color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-75, -45, -15, 15, 45, 75]

turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(turtle_color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.pendown()
    turtle.append(new_turtle)
    
    
if user_bet:
    is_race_on = True
    

while is_race_on:
    rand_distance = random.randint(0, 10)
    rand_turtle = turtle[random.randint(0,5)]
    rand_turtle.penup()
    rand_turtle.forward(rand_distance)
    if rand_turtle.xcor() > 230:
        winning_color = rand_turtle.pencolor()
        if winning_color == user_bet:
            print(f"You've won! The {winning_color} turtle is the winner!")
        else:
            print(f"You've lose! The {winning_color} turtle is the winner!")
        is_race_on = False


screen.exitonclick()