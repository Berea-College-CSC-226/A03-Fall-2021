######################################################################
# Author: Samiha Sultana
# Username: sultanas
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Introduces the use of functions with the turtle library
# Google Doc link: https://docs.google.com/document/d/104SpSOHGLHB7FCTDaiDXDmA99eMgXBtoQ6M8MIh_twI/edit?usp=sharing
######################################################################
import turtle
wn = turtle.Screen()        # creates a graphics window
wn.colormode(255)
wn.bgcolor(240,230,140)
alex = turtle.Turtle()      # create a turtle named alex
alex.penup()                # set initial position
alex.goto(0, 200)
alex.pendown()

def make_base():
    """
    this function created the base of the rose
    :return:
    """
    alex.fillcolor("maroon")
    alex.begin_fill()
    alex.circle(10, 180)
    alex.circle(25, 110)
    alex.left(50)
    alex.circle(60, 45)
    alex.circle(20, 170)
    alex.right(24)
    alex.forward(30)
    alex.left(10)
    alex.circle(30, 110)
    alex.forward(20)
    alex.left(40)
    alex.circle(90, 70)
    alex.circle(30, 150)
    alex.right(30)
    alex.forward(15)
    alex.circle(80, 90)
    alex.left(15)
    alex.forward(45)
    alex.right(165)
    alex.forward(20)
    alex.left(155)
    alex.circle(150, 80)
    alex.left(50)
    alex.circle(150, 90)
    alex.end_fill()
    alex.left(150)
    alex.circle(-90, 70)
    alex.left(20)
    alex.circle(75, 105)
    alex.setheading(60)
    alex.circle(80, 98)
    alex.circle(-90, 40)
    alex.left(180)
    alex.circle(90, 40)
    alex.circle(-80, 98)
    alex.setheading(-83)

def make_leaves():
    """
    this function created the leaves
    :return:
    """
    alex.forward(30)
    alex.left(90)
    alex.forward(25)
    alex.left(45)
    alex.fillcolor("green")
    alex.begin_fill()
    alex.circle(-80,90)
    alex.right(90)
    alex.circle(-80,90)
    alex.end_fill()
    alex.right(135)
    alex.forward(60)
    alex.left(180)
    alex.forward(85)
    alex.left(90)
    alex.forward(80)

    alex.right(90)
    alex.right(45)
    alex.fillcolor("green")
    alex.begin_fill()
    alex.circle(80, 90)
    alex.left(90)
    alex.circle(80, 90)
    alex.end_fill()
    alex.left(135)
    alex.forward(60)
    alex.left(180)
    alex.forward(60)
    alex.right(90)
    alex.circle(200, 60)

def main():
    make_base()
    make_leaves()
    wn.exitonclick()
main()
