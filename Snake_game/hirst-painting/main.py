import turtle
from turtle import Turtle, Screen
import random

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

tim = Turtle()
turtle.colormode(255)
tim.speed("slow")

x = -200.00
y = -100.00
number_of_dot = 100
tim.penup()
tim.setpos(x, y)
print(tim.pos())
for dot_number in range(1, number_of_dot + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_number % 10 == 0:
        y += 50
        tim.setpos(x, y)

tim.hideturtle()


#Solution 2

# x = -200.00
# y = -100.00
# loop = 0
#
# while loop < 10:
#     tim.penup()
#     tim.setpos(x, y)
#     print(tim.pos())
#     for _ in range(10):
#         tim.dot(20, random.choice(color_list))
#         tim.penup()
#         tim.forward(50)
#     y += 50
# loop += 1
# tim.hideturtle()



screen = Screen()
screen.exitonclick()



