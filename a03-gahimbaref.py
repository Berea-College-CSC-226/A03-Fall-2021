######################################################################
# Author: fleur gahimbare
# Username: gahimbaref

# Assignment: A03
# Purpose: functional turtles
# Google Doc: https://docs.google.com/document/d/1TLBu_bBryR7OgdNl3cK5yRIKkXbeXfwQ8JX9OoRIzq0/edit?usp=sharing
######################################################################

import turtle
turtle.colormode(255)


def drawGrass(t):
    """
    :param t: a turtle object
    draws grass under the bicycle
    """
    #goes to a specific location, sets the fillcolor to green using RGB, draws a rectangle and fills it.
    t.penup()
    t.goto(-320, -150)
    t.begin_fill()
    t.fillcolor((8,165,21))
    t.left(50)
    t.pencolor("black")
    t.pendown()
    t.forward(640)
    t.right(90)
    t.forward(110)
    t.right(90)
    t.forward(640)
    t.right(90)
    t.forward(110)
    t.end_fill()

def drawTiles(d):
    """
    :param d: a turtle object
    This function draws the tiles of my bicycle
    """
    for i in range(2):                  #Uses a nested loop to draw tiles
        for i in range(6):
            for i in range(4):
                d.circle(90, 240)
                d.left(45)
                d.forward(50)
                d.penup()
                d.forward(30)
                d.pendown()
        d.penup()
        d.goto(160, -100)

def chainStay(c):
    """
    draws the chainStay of the Bicycle
    """
    #goes to a specific location, uses half circles and lines to draw the chainStay.
    c.goto(-140, -40)
    c.right(5)
    c.pendown()
    c.forward(135)
    c.circle(20, 180)
    c.left(5)
    c.forward(145)
    c.circle(13, 180)
    c.forward(7)

    c.penup()
    c.forward(125)
    c.pendown()
    c.circle(10, 360)

def drawTubes(b):
    """
    :param b: a turtle object
    This function draws the tubes that connect the bike (3)
    """
    b.penup()
    b.goto(150, -40)
    b.pendown()
    b.left(110)
    b.forward(220)
    b.left(30)
    b.circle(40, 20)
    b.forward(40)
    b.penup()
    b.goto(170,-40)
    b.pendown()
    b.left(-50)
    b.forward(230)
    b.left(30)
    b.circle(40,20)
    b.forward(40)
    b.forward(30)
    for i in range(2):
        b.circle(30,30)
        b.left(30)
    b.left(90)
    b.forward(50)
    b.penup()
    b.goto(0, -12)
    b.pendown()
    for i in range(2):
        b.left(50)
        b.forward(170)
        b.penup()
        b.goto(15,-12)
        b.pendown()
        b.left(-50)

    b.penup()
    b.goto(-15,-12)
    b.pendown()
    b.left(120)
    for i in range(2):
        b.forward(170)
        b.penup()
        b.goto(0, -12)
        b.pendown()

def drawSeat(s):
    """
    draws the seat of the bicycle and colors it pink using RGB values
    """
    s.penup()
    s.goto(-130, 150)
    s.pendown()
    s.begin_fill()
    s.fillcolor((252,186,203))
    s.circle(30, 250)
    s.circle(-70, 30)
    s.circle(40, 20)
    s.circle(20, 100)
    s.circle(15, 60)
    s.forward(50)
    s.end_fill()

def drawBasket(k):
    """
    draws the basket attached to the bike using a turtle object
    """
    k.penup()
    k.goto(210, 150)
    k.pendown()
    k.left(10)

    k.penup()
    k.forward(110)
    k.pendown()
    k.begin_fill()
    k.fillcolor("pink")
    k.left(90)
    for i in range(4):
        k.left(40)
        k.forward(50)
    k.end_fill()

def drawFlowers(w):
    """
    draws the flowers "in" the basket
    """
    for i in range(2):
        w.forward(70)
        w.begin_fill()
        w.fillcolor("red")
        for i in range(2):
            for i in range(6):
                for i in range(4):
                    w.circle(10,170)
                    w.left(35)
                    w.forward(50)
                    w.penup()
                    w.forward(30)
                    w.pendown()
        w.end_fill()

def main():
    f = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor((208,240,192))
    f.penup()
    f.goto(-160,-100)
    f.speed(0)
    """
    The following block Calls the previous functions 
    """

    drawTiles(f)  # calls the drawTiles function
    chainStay(f)  #calls the chainStay function
    drawTubes(f)
    drawSeat(f)
    drawBasket(f)
    drawFlowers(f)
    drawGrass(f)
    wn.exitonclick()

main()




