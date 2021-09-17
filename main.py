######################################################################
# Author: Lawrence Hoerst
# Username: hoerstl
#
# Assignment: A03: Functional Turtles
# Purpose: Draw something complex
#
# Google Docs link: https://docs.google.com/document/d/123ZunEQBD70OC146X774eyDHagNg1zsk3sKZIWjwBO4/edit?usp=sharing
#
######################################################################


import turtle
import math

def curveline (t, distance, curve, direction = "left"):
    """draws a curved line in a given direction"""
    startang = t.heading()

    circleamount = math.acos((-(distance/curve)**2+2)/2)
    circleamount = circleamount * 180 / math.pi


    if direction == "left":
        t.seth(-circleamount / 2 + startang)
        t.circle(curve, circleamount, 40)

    else:
        t.seth(circleamount / 2 + 180 + startang)
        t.circle(curve, circleamount * -1, 40)

    return curve, circleamount


def set_up(t):
    t.penup()
    t.speed(0)
    t.goto(0, -200)


def reset(t,start):
    t.penup()
    t.setpos(start)
    t.seth(0)


def drawleftleg(t,start):
    """Draws Kirby's left leg"""
    legscale = 1.2
    turtle.colormode(255)
    t.color(0, 0, 0)
    t.pensize(2)
    t.forward(60)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.seth(-25)
    t.pendown()
    t.begin_fill()
    curveline(t, 60 * legscale, 100 * legscale, "right")
    t.seth(-115)
    curveline(t, 10 * legscale, 10 * legscale, "right")
    t.seth(170)
    curveline(t, 80 * legscale, 100 * legscale, "right")
    t.color(220, 0, 0)
    t.end_fill()

    reset(t, start)


def drawrightleg(t,start):
    """Draws Kirby's right leg"""
    legscale = 1.2
    turtle.colormode(255)
    t.color(0, 0, 0)
    t.pensize(2)
    t.forward(-60)
    t.right(90)
    t.forward(-40)
    t.seth(-25 - 130)
    t.pendown()
    t.begin_fill()
    curveline(t, 60 * legscale, 100 * legscale)
    t.seth(-115 + 50)
    curveline(t, 10 * legscale, 10 * legscale)
    t.seth(170 - 160)
    curveline(t, 80 * legscale, 100 * legscale)
    t.color(220, 0, 0)
    t.end_fill()

    reset(t, start)

def drawbody(t,start):
    """Draws Kirby's body"""
    t.pendown()
    t.pensize(5)
    t.color("black")
    t.begin_fill()
    t.circle(100)
    t.color("pink")
    t.end_fill()
    t.color("black")

    reset(t,start)


def drawleftarm(t,start):
    """Draws Kirby's left arm"""
    t.circle(100, 130)
    t.begin_fill()
    t.color("black")
    t.pensize(5)
    t.seth(90)
    t.penup()
    t.forward(-30)
    t.seth(0)
    t.forward(10)
    t.pendown()
    t.seth(45)
    t.begin_fill()
    t.forward(25)
    t.circle(30, 180)
    t.forward(25)
    t.color("pink")
    t.end_fill()
    reset(t, start)


def drawrightarm(t,start):
    """Draws Kirby's right arm"""
    t.color("black")
    t.circle(100, 270)
    t.seth(180)
    t.backward(10)
    t.seth(270)
    t.right(25)
    t.begin_fill()
    t.pendown()
    t.forward(40)
    t.circle(30, 180)
    t.forward(10)
    t.color("pink")
    t.end_fill()
    reset(t, start)


def drawrighteye(t,start):
    """Draws Kirby's right eye"""
    eyescale = 1.5
    t.circle(100, 205)
    t.seth(270)
    t.forward(40)
    t.color("black")
    t.pendown()
    t.begin_fill()
    t.forward(20 * eyescale)
    t.circle(10 * eyescale, 180)
    t.forward(20 * eyescale)
    t.circle(10 * eyescale, 180)
    t.end_fill()

    t.penup()
    t.color(0, 0, 200)
    t.forward(20 * eyescale - 3)
    t.begin_fill()
    t.seth(0)
    curveline(t, 20 * eyescale, 50, "right")
    t.seth(90)
    t.forward(-3)
    t.circle(10 * eyescale, -180)
    t.end_fill()
    t.circle(10 * eyescale, 180)
    t.forward(20 * eyescale)
    t.circle(10 * eyescale, 180)

    t.color("white")
    t.penup()
    eyescale = .4
    t.left(90)
    t.forward(12)
    t.right(90)
    t.begin_fill()
    t.pendown()
    t.forward(20 * eyescale)
    t.circle(10 * eyescale, 180)
    t.forward(20 * eyescale)
    t.circle(10 * eyescale, 180)
    t.end_fill()

    reset(t, start)



def drawlefteye(t,start):
    """Draws Kirby's left eye"""
    eyescale = 1.5
    t.circle(100, 155)
    t.seth(0)
    t.backward(20)
    t.seth(270)
    t.forward(40)

    t.color("black")
    t.pendown()
    t.begin_fill()
    t.forward(20 * eyescale)
    t.circle(10 * eyescale, 180)
    t.forward(20 * eyescale)
    t.circle(10 * eyescale, 180)
    t.end_fill()

    t.penup()
    t.color(0, 0, 200)
    t.forward(20 * eyescale - 3)
    t.begin_fill()
    t.seth(0)
    curveline(t, 20 * eyescale, 50, "right")
    t.seth(90)
    t.forward(-3)
    t.circle(10 * eyescale, -180)
    t.end_fill()
    t.circle(10 * eyescale, 180)
    t.forward(20 * eyescale)
    t.circle(10 * eyescale, 180)

    t.color("white")
    t.penup()
    eyescale = .4
    t.left(90)
    t.forward(12)
    t.right(90)
    t.begin_fill()
    t.pendown()
    t.forward(20 * eyescale)
    t.circle(10 * eyescale, 180)
    t.forward(20 * eyescale)
    t.circle(10 * eyescale, 180)
    t.end_fill()

    reset(t, start)


def drawmouth(t,start):
    """Draws Kirby's mouth"""
    t.pensize(3)
    t.circle(100, 75)
    t.seth(180)
    t.forward(45)
    t.color("black")
    t.pendown()
    t.begin_fill()
    curveline(t, 100, 100)
    t.seth(0)
    a, b = curveline(t, 100, 55)

    t.color("dark red")
    t.end_fill()
    t.color("black")
    t.pensize(2)
    t.circle(a, -20)
    t.begin_fill()
    t.circle(a, -b + 40)
    t.seth(0)

    curveline(t, 76, 70, "right")

    t.color("red")
    t.end_fill()

    reset(t, start)


def drawkirby(t):
    start = t.pos()

    reset(t, start)

    # Draw's Kirby's left leg
    drawleftleg(t, start)

    # Draws Kirby's right leg
    drawrightleg(t, start)

    # Kirby body
    drawbody(t, start)

    # Draw Kirby's left arm
    drawleftarm(t, start)

    # Draw kirby's right arm
    drawrightarm(t, start)

    # Draws Kirby's right eye
    drawrighteye(t, start)


    # Draw's Kirby's left eye
    drawlefteye(t, start)



    # Draws Kirby's mouth
    drawmouth(t,start)


    # Makes the turtle invisible
    t.hideturtle()







def main():

    wn = turtle.Screen()
    wn.bgpic("Whispy Woods.gif")

    kirb = turtle.Turtle()



    set_up(kirb)
    drawkirby(kirb)

    wn.exitonclick()


main()


