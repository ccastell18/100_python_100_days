import turtle
from turtle import Turtle, Screen
import random

t = Turtle()

colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']


# # draw multiple circles
# r = 100
#
# t.speed('fastest')
# for _ in range(74):
#     t.pencolor(random.choice(colors))
#     t.circle(r)
#     t.left(5)

# Random walk
# directions = [0, 90, 180, 270]
#
#
# t.pensize(10)
# t.speed('fastest')
# for _ in range(200):
#     t.pencolor(random.choice(colors))
#     t.forward(30)
#     t.setheading(random.choice(directions))

# Drawing random shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         t.forward(100)
#         t.right(angle)
#
#
# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)
#     t.pencolor(colors[shape_side_n - 3])










screen = Screen()
screen.exitonclick()