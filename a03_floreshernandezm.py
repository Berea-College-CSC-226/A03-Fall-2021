###############################################################################
# Author: Michell Flores
# Username: floreshernandezm
#
# Assignment: Homework A03 - Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: to create a drawing using different functions
# Google Doc: https://docs.google.com/document/d/10YtfVvOBWU_anp4a2QwwaNC8iGd5oO4-grcRlWFjytk/edit#heading=h.jr3eaq51gzcu
#
###############################################################################

import turtle
k = turtle.Turtle()
moe = turtle.Turtle()
p = turtle.Turtle()
h = turtle.Turtle()
# import the different turtles and name them

k.hideturtle()
moe.hideturtle()
p.hideturtle()
h.hideturtle()
# hide the turtle pens so there is no visible shape drawing

def make_house(k):
    """Drawing a house and the roof and filling them in"""
    k.color("#FFD39B")
    k.pensize(4)
    k.speed(2)
    k.penup()
    k.goto(-80, -260)
    k.pendown()
    k.begin_fill()
    for i in range(4):
        k.fd(350)
        k.left(90)
    k.end_fill()
# just finished creating the square of the house

    k.color("red")
    k.begin_fill()
    k.penup()
    k.goto(-100, 90)
    k.pendown()
    k.fd(390)
    k.left(135)
    k.fd(276)
    k.left(90)
    k.fd(276)
    k.end_fill()
# create the roof of the house and filled it in

def make_door_and_windows(k):
    """Draw door on house and use the same turtle to draw the windows"""
    k.pensize(4)
    k.speed(5)
    k.color("red")
    k.penup()
    k.home()
    k.goto(70, -160)
    k.pendown()
    k.begin_fill()
    k.right(90)
    k.fd(100)
    k.left(90)
    k.fd(50)
    k.left(90)
    k.fd(100)
    k.left(90)
    k.fd(50)
    k.end_fill()
# created the door of the house in the above code

    k.color("lightblue")
    k.penup()
    k.goto(60, -90)
    k.pendown()
    k.begin_fill()
    for i in range(4):
        k.fd(100)
        k.right(90)
    k.end_fill()
# created the left window of the house and filled it in

    k.color("brown")
    k.penup()
    k.goto(60, -90)
    k.pendown()
    k.pensize(5)
    for i in range(4):
        k.fd(100)
        k.right(90)
    k.fd(50)
    k.right(90)
    k.fd(100)
    k.right(90)
    k.fd(50)
    k.right(90)
    k.fd(50)
    k.right(90)
    k.fd(100)            # created the brown border of the left window

    k.color("lightblue")
    k.penup()
    k.goto(230, -90)
    k.pendown()
    k.begin_fill()
    for i in range(4):
        k.fd(100)
        k.right(90)
    k.end_fill()        # created the blue inside of the right window and filled it in

    k.color("brown")
    k.penup()
    k.goto(230, -90)
    k.pendown()
    k.pensize(5)
    for i in range(4):
        k.fd(100)
        k.right(90)
    k.fd(50)
    k.right(90)
    k.fd(100)
    k.right(90)
    k.fd(50)
    k.right(90)
    k.fd(50)
    k.right(90)
    k.fd(100)
    k.penup()           # created the brown border of the right window

    k.home()
    k.goto(-500, -260)
    k.pendown()
    k.color("#00FF00")      # use hexadecimal color for the houses foundation
    k.begin_fill()
    k.fd(1000)
    k.right(90)
    k.fd(500)
    k.right(90)
    k.fd(1000)
    k.right(90)
    k.fd(500)
    k.end_fill()     # created the green grass below the house for the flowers to stand on


def make_flower1(moe):
    """Draw flower 1 next to house"""
    moe.hideturtle()
    moe.color("pink")
    moe.pensize(3)
    moe.speed(5)
    moe.penup()
    moe.goto(-140, -120)
    moe.pendown()
    for i in range(8):
        moe.right(45)
        moe.fd(30)
        moe.left(45)
        moe.fd(30)
        moe.left(135)
        moe.fd(30)
        moe.left(45)
        moe.fd(30)
        moe.left(135)
    moe.right(90)
    moe.fd(137)
# created the middle pink flower of the house

def make_flower2(p):
    """Draw flower 3"""
    p.hideturtle()
    p.color("orange")
    p.pensize(3)
    p.speed(5)
    p.penup()
    p.goto(-60, -180)
    p.pendown()
    for i in range(8):
        p.right(45)
        p.fd(30)
        p.left(45)
        p.fd(30)
        p.left(135)
        p.fd(30)
        p.left(45)
        p.fd(30)
        p.left(135)
    p.right(90)
    p.fd(77)
# created the right orange flower of the house

def make_flower3(h):
    """Draw last flower"""
    h.hideturtle()
    h.color("yellow")
    h.pensize(3)
    h.speed(5)
    h.penup()
    h.goto(-220, -180)
    h.pendown()
    for i in range(8):
        h.right(45)
        h.fd(30)
        h.left(45)
        h.fd(30)
        h.left(135)
        h.fd(30)
        h.left(45)
        h.fd(30)
        h.left(135)
    h.right(90)
    h.fd(77)
# created the left yellow flower of the house

def main():
    """Draw house with flowers near it"""
    wn = turtle.Screen()
    wn.bgcolor("cyan")      # set the screen background to cyan

    make_house(k)
    make_door_and_windows(k)
    make_flower1(moe)
    make_flower2(p)
    make_flower3(h)
# call all the functions in the main

    wn.exitonclick()
# allow the user to exit the window on click

main()