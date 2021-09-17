#################################################################################
# Author: Finn Bledsoe
# Username: bledsoef
#
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To experiment and draw something complex
#################################################################################
import turtle


def windmill(x):
    x.pencolor('white')
    x.right(90)
    x.forward(30)
    x.left(90)
    x.forward(200)
    x.left(90)
    x.forward(40)
    x.left(90)
    x.forward(200)
    x.left(90)
    x.forward(30)
    x.pensize(2)
    x.pencolor('black')
    x.left(90)
    x.forward(200)
    x.left(90)
    x.pensize(1)
    x.pencolor('white')
    x.forward(10)
    x.pensize(2)
    x.pencolor('black')
    x.left(90)
    x.forward(200)
    x.right(90)
    x.pensize(1)
    x.pencolor('white')
    x.forward(10)
    x.pensize(2)
    x.pencolor('black')
    x.right(90)
    x.forward(200)
    x.left(90)
    x.pensize(1)
    x.pencolor('white')
    x.forward(10)
    x.pensize(1)
    x.pencolor('white')
    x.left(90)
    x.forward(200)

    return


def windmill_base(x):
    x.pencolor('brown')
    x.left(90)
    x.penup()
    x.forward(30)
    x.pendown()
    x.fillcolor('brown')
    x.begin_fill()
    for ii in range(1):
        x.right(90)
        x.forward(60)
        x.right(90)
        x.forward(250)
        x.right(90)
        x.forward(150)
        x.right(90)
        x.forward(250)
        x.right(90)
        x.forward(100)
    x.end_fill()
    return


def ground(x):
    x.fillcolor('green')
    x.pencolor('green')
    x.begin_fill()
    x.pendown()
    x.forward(370)
    x.right(90)
    x.forward(90)
    x.right(90)
    x.forward(740)
    x.right(90)
    x.forward(90)
    x.right(90)
    x.forward(370)
    x.end_fill()


def main():
    wn = turtle.Screen()
    finn = turtle.Turtle()
    finn.speed(10)
    wn.colormode(255)
    wn.bgcolor('light blue')
    windmill_base(finn)
    finn.color(250,250,250)
    finn.penup()
    finn.home()
    finn.begin_fill()
    finn.pendown()
    for i in range(4):
        windmill(finn)
        finn.right(90)
        finn.circle(10, 90)
        finn.right(90)
    finn.end_fill()
    finn.penup()
    finn.home()
    finn.right(90)
    finn.forward(220)
    finn.left(90)
    ground(finn)
    wn.exitonclick()
    return


main()



