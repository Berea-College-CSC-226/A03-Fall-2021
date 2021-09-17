#####################################################################################################################
# Name: Ethan Campbell
# Username: campbelle2
# Assignment: A03
# Google Doc Link: https://docs.google.com/document/d/1HTNFVbuYYJo1rWLEh1L9kYekHd9TefO3PxlP40nxlK0/edit?usp=sharing
########################################################################################################################

import turtle


def walls(dave):
    """
    this draws the frame/walls of the house
    :param dave: Turtle object
    :return: none
    """
    dave.penup()
    dave.setpos(50, -105)
    dave.pendown()
    dave.color(220, 50, 150)
    dave.begin_fill()
    for i in range(2):             # makes rectangle shape (house frame)
        dave.forward(180)
        dave.left(90)
        dave.forward(140)
        dave.left(90)
    dave.end_fill()


def roof(dave):
    """
    draws roof for the house
    :param dave: Turtle object
    :return: none
    """
    dave.penup()
    dave.setpos(50, 35)
    dave.color(75, 0, 130)
    dave.pendown()
    dave.begin_fill()
    dave.left(45)
    dave.forward(127)
    dave.right(90)
    dave.forward(127)
    dave.end_fill()
    dave.left(45)


def door(dave):
    """
    draws a door for the house
    :param dave: Turtle object
    :return: none
    """
    dave.penup()
    dave.setpos(125, -105)
    dave.pendown()
    dave.color(248, 248, 255)
    dave.begin_fill()
    for i in range(2):
        dave.forward(27.5)
        dave.left(90)
        dave.forward(60)
        dave.left(90)
    dave.end_fill()
    dave.penup()
    dave.forward(5)
    dave.left(90)
    dave.forward(27)
    dave.color(255, 215, 0)
    dave.dot()
    dave.right(90)


def window(dave, x, y):
    """
    draws a window in the position of x and y
    :param dave: Turtle object
    :param x: x coordinate of window
    :param y: y coordinate of window
    :return: none
    """
    dave.color(0, 0, 0)
    dave.penup()
    dave.setpos(x, y)
    dave.pendown()
    dave.fillcolor(0, 191, 255)
    dave.begin_fill()
    for i in range(4):
        dave.forward(30)
        dave.left(90)
    dave.end_fill()
    dave.forward(15)
    dave.left(90)
    dave.forward(30)
    for i in range(2):
        dave.left(90)
        dave.forward(15)
    dave.left(90)
    dave.forward(30)





def main():
    """
    this will make the house in full
    :return: none
    """
    turtle.colormode(255)
    wn = turtle.Screen()
    dave = turtle.Turtle()
    wn.bgpic("trees.gif")                                # sets background as pretty forest
    walls(dave)
    roof(dave)
    door(dave)
    window(dave, 70, -85)
    window(dave, 70, -20)
    window(dave, 180, -85)
    window(dave, 180, -20)
    wn.exitonclick()

main()
