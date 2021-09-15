######################################################################
# Author: Kyle Drummonds
# Username: drummondsk
# Google Docs: https://docs.google.com/document/d/1MinJ08KtjtmUmBsiooU1D00y3z0911M7_YCjq4wOiVE/edit?usp=sharing
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Using turtles to create complex structures
######################################################################
import turtle
import math

wn = turtle.Screen()
wn.bgcolor("cyan")
john = turtle.Turtle()
bell = turtle.Turtle()
john.speed(3)

#function to begin drawing the outer shape of the house
def drawfoundation():
    '''Draws the foundation of the house'''
    john.penup()
    john.goto(-100, -200)
    john.pendown()
    john.color("black",(178,34,34))
    john.begin_fill()
    while True:

        john.left(90)
        john.forward(250)
        john.right(90)
        john.forward(250)
        john.right(90)
        john.forward(250)
        john.right(90)
        john.forward(250)
        break
    john.end_fill()
    john.begin_fill()

    while True:

        john.backward(250)
        john.right(135)
        john.forward(100)
        john.left(45)
        john.forward(250)
        john.left(135)
        john.forward(100)
        break
    john.end_fill()

    john.color("black",(88, 87, 85))
    john.begin_fill()
    while True: #draws the triangular section of the roof
        john.right(75)
        john.forward(160)
        john.left(66)
        john.forward(135)

        break
    john.end_fill()
    john.backward(135)
    john.color("black", (88, 87, 85))
    john.begin_fill()
    while True:

        john.left(141)
        john.forward(210)
        break
    john.end_fill()

#fuction that draws the finer details on the outside of the house, such as the windows and doors
def interior():
    '''Draws the details of the house'''
    jess = turtle.Turtle()
    jess.penup()
    jess.goto(-45, -200)
    jess.pendown()
    jess.left(90)
    jess.forward(100)
    jess.right(90)
    jess.forward(100)
    jess.right(90)
    jess.forward(100)
    jess.color("white", "blue")

    jess.begin_fill()
    jess.penup()
    jess.backward(120)
    jess.pendown()
    for i in range(4):
        jess.left(90)
        jess.forward(50)

    jess.end_fill()
    jess.left(90)
    jess.forward(25)
    jess.left(90)
    jess.forward(50)
    jess.backward(25)
    jess.left(90)
    jess.forward(25)
    jess.backward(50)
    jess.forward(50)
    jess.left(90)
    jess.forward(25)
    jess.penup()
    jess.right(90)
    jess.forward(150)
    jess.pendown()
    jess.begin_fill()
    for i in range(4):
        jess.right(90)
        jess.forward(50)
    jess.end_fill()
    jess.right(90)
    jess.forward(25)
    jess.right(90)
    jess.forward(50)
    jess.backward(25)
    jess.right(90)
    jess.forward(25)
    jess.backward(50)

    jess.penup()
    jess.goto(40, -160)
    jess.pendown()
    jess.begin_fill()
    jess.circle(5)
    jess.end_fill()
# Creates the star


def drawstar():
    '''Draws the Star in the upper left hand corner'''
    bell.penup()
    bell.goto(-155, 145)
    bell.speed(0)
    bell.pendown()
    angle=150
    side = 100
    top = 5
    spin = 360/top
    angle_left = angle
    angle_right = angle
    bell.color("green","yellow")

    for r in range(10):
        bell.begin_fill()
        for p in range(top):
            bell.forward(side)
            bell.right(angle_right)
            bell.forward(side)
            bell.left(angle_left)
            bell.right(spin)
        bell.end_fill()
        bell.right(2)

def main():

    turtle.colormode(255)
    drawfoundation()
    drawstar()
    interior()
    wn.exitonclick()

main()

