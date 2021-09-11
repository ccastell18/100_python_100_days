import colorgram
import turtle as turtle_module
import random
#
# rgb_colors = []
# colors = colorgram.extract('painting.jpg', 20
#                            )
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)
#
turtle_module.colormode(255)
t = turtle_module.Turtle()
# print(rgb_colors)
colors = [ (200, 12, 32), (250, 237, 21), (39, 76, 189), (239, 228, 4), (38, 217, 69), (228, 159, 48), (28, 40, 156), (215, 75, 12), (16, 154, 15), (197, 15, 11), (242, 35, 164), (228, 18, 122), (71, 10, 31), (61, 15, 8), (224, 141, 207), (11, 97, 63)]

t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 101
t.speed('fastest')

for dot_count in range(1, number_of_dots):
   t.dot(20, random.choice(colors))
   t.forward(50)

   if dot_count % 10 == 0:
      t.setheading(90)
      t.forward(50)
      t.setheading(180)
      t.forward(500)
      t.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()


