from turtle import Turtle, Screen


t=Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def move_backwards():
    t.backward(10)


def move_left():
    new_heading = t.heading() +10
    t.setheading(new_heading)


def move_right():
    new_heading = t.heading() -10
    t.setheading(new_heading)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()



screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(move_right, 'd')
screen.onkey(move_left, 'a')
screen.onkey(clear, 'c')
screen.exitonclick()