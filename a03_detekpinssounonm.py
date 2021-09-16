#
######################################################################
# Author: Moise Dete-Kpinssounon
# Username: detekpinssounonm
# GitHub username: Shalum11059
# Google Doc link: https://docs.google.com/document/d/1VKI1zQMfFyNFF2HTCLYneZ1Lftv1HOhzSwEBgLi8uoo/edit?usp=sharing
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles

# Purpose:
# Continue practicing creating and using functions.
# More practice on using the turtle library.
# Learn about how computers represent colors.
# Learn about source control and git.

######################################################################

import turtle
from time import sleep


def draw_ball(trtl):
    """ Takes a turtle and makes it draw a simple soccer ball"""
    trtl.color((0, 15, 112), (0, 15, 112))
    jump_to(trtl, 0, -225)
    trtl.circle(50, -360)
    jump_to(trtl, -13, -200)
    trtl.begin_fill()
    for i in range(5):
        trtl.forward(30)
        trtl.right(72)
        trtl.forward(15 + 2 * i)
        trtl.backward(15 + 2 * i)
        trtl.left(72 * 2)
    trtl.end_fill()


def jump_to(trtl, x, y):
    """Shortcut for frequent moves of a turtle to a position without drawing"""
    trtl.penup()
    trtl.goto(x, y)
    trtl.pendown()


def draw_rectangle(trtl, pos_x, pos_y, width, height):
    """General way of drawing a rectangle at a given position, with a given width and length"""
    jump_to(trtl, pos_x, pos_y)
    trtl.forward(width)
    trtl.left(90)
    trtl.forward(height)
    trtl.left(90)
    trtl.forward(width)
    trtl.left(90)
    trtl.forward(height)
    trtl.left(90)


def draw_tracks(trtl, ):
    """Successively draws rectangles with two semi-circles at each end"""
    spacing = 0
    for i in range(5):
        if i == 0:
            trtl.begin_fill()
        jump_to(trtl, -180 - spacing, -60 - spacing)
        trtl.circle(110 + spacing, -180)
        trtl.backward(360 + 2 * spacing)
        trtl.circle(110 + spacing, -180)
        trtl.backward(360 + 2 * spacing)
        trtl.end_fill()
        spacing += 10


def draw_field(trtl):
    """Uses draw_rectangle() to draw the main field in a soccer stadium"""
    # Draws the big rectangle
    draw_rectangle(trtl, -180, -50, 360, 200)
    # Draws the two penalty boxes
    draw_rectangle(trtl, -180, 0, 50, 100)
    draw_rectangle(trtl, 130, 0, 50, 100)
    # Draws the two goal_boxes
    draw_rectangle(trtl, -180, 25, 20, 50)
    draw_rectangle(trtl, 160, 25, 20, 50)


def draw_center_and_penalty_arc(trtl):
    """Draws the two penalty kicking point of a soccer field"""

    # Drawing penalty arc
    jump_to(trtl, -130, 30)
    trtl.circle(20, 180)
    jump_to(trtl, 130, 30)
    trtl.circle(-20, 180)

    # Draw center
    jump_to(trtl, 0, 25)
    trtl.circle(25)
    jump_to(trtl, 0, 150)
    trtl.right(90)
    trtl.forward(200)
    trtl.left(90)


def write_slogan(trtl):

    jump_to(trtl, -120, 200)
    trtl.hideturtle()
    trtl.write("ICI,", False, font=("arial", 24, "normal"))
    sleep(1)
    jump_to(trtl, -70, 200)
    trtl.write(" C'EST", False, font=("arial", 24, "normal"))
    sleep(1)
    trtl.write("            PARIS!", False, font=("arial", 24, "normal"))
    sleep(1)


def main():
    """Creates and set up the turtle and the screen objects. Calls the methods in appropriate order.
    Does other polishing stuff"""
    wn = turtle.Screen()
    wn.bgpic("psg.png")
    wn.bgcolor("grey")
    wn.colormode(255)  # Make the screen object support RGB color model
    alex = turtle.Turtle()
    alex.color((0, 65, 112), (0, 255, 0))  # Uses Paris Saint Germain's color as pen color, green as fill color
    alex.speed(0)

    # Draw individual component of the soccer field
    draw_tracks(alex)
    draw_field(alex)
    draw_center_and_penalty_arc(alex)
    draw_ball(alex)

    write_slogan(alex)

    alex.showturtle()
    alex.speed(0)
    wn.tracer(0)
    wn.addshape("mmn.gif")  # register the image with the screen as a shape
    alex.shape("mmn.gif")  # now set the turtle's shape to it
    alex.penup()
    alex.goto(-350, 50)
    moves = int(900 / 0.01)

    while True:  # The program runs until the window is closed.
        for i in range(moves):
            wn.update()
            alex.forward(0.01)
        alex.goto(-350, 50)


main()
