from turtle import Turtle, Screen
import random

is_race_on = False
t = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle do you think will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50,80]
all_turtles = []

for turtle_index in range(0,6):
    t = Turtle(shape='turtle')
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You won. The winning color wasw {winning_color}")
            else:
                print(f"You Lost. The winning color was {winning_color}")

        random_distance = random.randint(0, 10)
        t.forward(random_distance)


screen.exitonclick()