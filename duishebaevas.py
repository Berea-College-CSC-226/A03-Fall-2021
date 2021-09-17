#################################################################################
# Author: Sabira Duishebaeva
# Username: Duishebaevas
#
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Designing a code or a program that could be used to draw a large square
#          and fill it using non-overlapping, just touching boustrophedon patterns.
#################################################################################
# Acknowledgements: Runestone Book and video from T03 Docs.
#Google Doc link: https://docs.google.com/document/d/1ohoMJXuuH4_POFBpW3MgT5h0yyGdIYoHP2xt7j1TH84/edit?usp=sharing
#
#################################################################################
# Python program to draw car in turtle programming

# Create the main function
import turtle



# Below code for drawing rectangular upper body

def main_car (shape):
    shape.fillcolor("pink")
    shape.penup()
    shape.goto(0, 0)
    shape.pendown()
    shape.begin_fill()
    shape.forward(370)
    shape.left(90)
    shape.forward(50)
    shape.left(90)
    shape.forward(370)
    shape.left(90)
    shape.forward(50)
    shape.end_fill()
def window_car (window):
# Below code for drawing window and roof
    window.penup()
    window.goto(90, 60)
    window.pendown()
    window.setheading(30)
    window.forward(65)
    window.setheading(0)
    window.forward(100)
    window.setheading(-35)
    window.forward(100)
    window.setheading(100)
    window.penup()
    window.goto(200, 50)
    window.pendown()
    window.forward(49.50)
#Draw tyres for the car
def main_tyres (tyres):
    tyres.penup()
    tyres.goto(100, -10)
    tyres.pendown()
    tyres.color('#000000')
    tyres.fillcolor('#000000')
    tyres.begin_fill()
    tyres.circle(20)
    tyres.end_fill()
    tyres.penup()
    tyres.goto(300, -10)
    tyres.pendown()
    tyres.color('#000000')
    tyres.fillcolor('#000000')
    tyres.begin_fill()
    tyres.circle(20)
    tyres.end_fill()

    tyres.hideturtle()

def main():
    """
    Draws a house at x, y on the screen.

    :return: None
    """

    car = turtle.Turtle()
    turtle.colormode(300)
    screen = turtle.Screen()
    screen.bgcolor("green")
    screen.screensize(800, 800)
    # Function calls for each part of the house
    main_car(car)
    window_car(car)
    main_tyres(car)
main()
