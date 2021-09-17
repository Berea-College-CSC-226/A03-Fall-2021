######################################################################
# Author: Justin Roberts
# Username: robertsj2
#
# Assignment: a03 Functional Turtles
# Purpose: To show that we can create functions for slightly more complex things.
######################################################################

import turtle
import random

# Hides the turtle, sends it somewhere, un-hides it.
def hide_goto(t, x, y):
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.showturtle()
    t.pendown()

# A function that allows me to fully set up one of my turtle variables in one line so it is ready to be used
def turtle_setup(turtle, hidet, shapet, colort, sx, sy, sizet, direction):
    turtle.shape(shapet)
    turtle.color(colort)
    turtle.pensize(sizet)
    turtle.right(direction)
    hide_goto(turtle, sx, sy)

    if hidet == 0:
        turtle.hideturtle()

# A function that I used to create the lines in the diamond pattern
def stamp_line(turt, x1, y1, x2, y2):

    turt.stamp()
    turt.pendown()
    turt.goto(x1, y1)
    turt.stamp()
    turt.penup()
    turt.goto(x2, y2)

# A function that allows you to create a specified amount of random circles filled or unfilled.
def random_circles(tu, amount, fill, color):
    tu.color(color)

    if fill == 0:
        tu.begin_fill()

    for c in range(amount):
        turtle.penup()
        tu.goto(random.randrange(-400, 400), random.randrange(-400, 400))
        tu.circle(20)

    if fill == 0:
        tu.end_fill()

# screen
wn = turtle.Screen()
wn.screensize(500, 500)
wn.bgcolor((.3, .4, .1))

def main():

    # Variables
    # turtle for testing functions
    tester = turtle.Turtle()
    # turtles for creating my design
    tline = turtle.Turtle()
    tcircle = turtle.Turtle()

    tcircle.speed(0)
#   Creates abstract patterns
    random_circles(tcircle, 10, 0, "dark blue")
    random_circles(tcircle, 10, 0, "dark red")
    random_circles(tcircle, 10, 0, "grey")

    tline.speed(8)
#   Using tline to draw the orange diamond shape
    turtle_setup(tline, 1, "turtle", "orange", 50, 300, 15, 90)
    stamp_line(tline, 300, 50, 50, 200)
    stamp_line(tline, 200, 50, 50, 100)
    stamp_line(tline, 100, 50, -50, 300)
    stamp_line(tline, -300, 50, -50, 200)
    stamp_line(tline, -200, 50, -50, 100)
    stamp_line(tline, -100, 50, -50, -300)
    stamp_line(tline, -300, -50, -50, -200)
    stamp_line(tline, -200, -50, -50, -100)
    stamp_line(tline, -100, -50, 50, -300)
    stamp_line(tline, 300, -50, 50, -200)
    stamp_line(tline, 200, -50, 50, -100)
    stamp_line(tline, 100, -50, 0, 0)


main()

wn.exitonclick()