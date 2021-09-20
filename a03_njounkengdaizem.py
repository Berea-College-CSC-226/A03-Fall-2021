#################################################################################################
#Author: Daize Njounkeng
#Username: njounkengdaizem
#
#Assignment: A03:Fully Functional Gitty Psychedelic Robotic Turtles
#Google Link: https://docs.google.com/document/d/17olAVuyfkXp12OCnMtIG84UDU28Sy5hG0UMKkKcaM2Q/edit?usp=sharing

################################################################################################
import turtle                                                                       #import turtle library


def background ():
    """ Define function that sets the sky's background color"""
    backgd = turtle.Turtle()
    backgd.hideturtle()
    backgd.penup()
    backgd.speed(0)
    backgd.setpos(-650, -180)                                #Sets position for background filling
    backgd.pendown()
    backgd.color("#40E0D0")
    backgd.begin_fill()
    for i in range(4):                                        #Fills background
        backgd.forward(1600)
        backgd.left(90)
    backgd.end_fill()

def pathlead():
    """ Define function that draws the path leading to the house and set color to orange"""
    path= turtle.Turtle()
    path.speed(0)
    path.hideturtle()
    path.penup()
    path.goto(-25, -180)
    path.color("orange")
    path.pendown()
    path.begin_fill()
    path.right(90)
    path.forward(150)
    path.left(90)
    path.forward(70)
    path.left(90)
    path.forward(150)
    path.end_fill()

def sqareshape():
    """ Define function that draws square part of the house"""
    square = turtle.Turtle()
    square.penup()
    square.speed(0)
    square.hideturtle()
    square.color("white")

    square.setpos(-100, -180)
    square.pendown()
    square.begin_fill()
    for i in range(4):                                        #Draws square
        square.forward(200)
        square.left(90)
    square.end_fill()

def roofing():
    """ Define function that creates the roofing"""
    roof = turtle.Turtle()
    roof.speed(0)
    roof.hideturtle()
    roof.penup()
    roof.color("brown")
    roof.begin_fill()
    roof.goto(-125, 20)
    roof.pendown()
    for i in range(3):                                      #Draws roof
        roof.forward(250)
        roof.left(120)
    roof.end_fill()

def chimneytop():
    """ Define function that draws the chimney and the smoke from the chimney"""
    chimney = turtle.Turtle()
    chimney.speed(0)
    chimney.hideturtle()
    chimney.penup()
    chimney.goto(70, 115)
    chimney.pendown()
    chimney.color("brown")
    chimney.begin_fill()
    chimney.left(90)                                                 #Draws chimney
    chimney.forward(70)
    chimney.left(90)
    chimney.forward(20)
    chimney.left(90)
    chimney.forward(40)
    chimney.end_fill()

    smoke = turtle.Turtle()                                        #Turtle that creates smoke
    smoke.hideturtle()
    smoke.color("gray")
    smoke.penup()
    smoke.goto(60, 190)
    smoke.begin_fill()
    smoke.circle(7)
    smoke.end_fill()

    smoke.penup()
    smoke.goto(62, 220)
    smoke.begin_fill()
    smoke.circle(7)
    smoke.end_fill()

    smoke.penup()
    smoke.goto(65, 250)
    smoke.begin_fill()
    smoke.circle(7)
    smoke.end_fill()

def frontdoor():
    """ Define function that draws the front door"""
    door = turtle.Turtle()
    door.speed(0)
    door.hideturtle()
    door.penup()
    door.goto(40, -180)
    door.color("brown")
    door.begin_fill()
    door.pendown()
    door.left(90)                                      #Draws door
    door.forward(90)
    door.left(90)
    door.forward(60)
    door.left(90)
    door.forward(90)
    door.end_fill()

    knob = turtle.Turtle()
    knob.speed(0)
    knob.hideturtle()
    knob.color("black")
    knob.penup()
    knob.goto(-10, -140)
    knob.pendown()
    knob.begin_fill()
    knob.circle(3)                                            #Draws circular knob
    knob.end_fill()

def window():
    """ Define function that draws the windows of the house"""
    win = turtle.Turtle()
    win.speed(0)
    win.hideturtle()
    win.pensize(3)
    win.penup()
    win.goto(-80, -70)
    win.pendown()
    for i in range(4):                                    #Draws windows
        win.forward(40)
        win.left(90)
    win.penup()
    win.goto(-60, -70)
    win.pendown()
    win.left(90)
    win.forward(40)


    win.penup()
    win.goto(70, -30)
    win.pendown()
    win.left(90)
    for i in range(4):
        win.forward(40)
        win.left(90)
    win.penup()
    win.goto(65, -30)
    win.pendown()
    win.left(90)
    win.forward(40)

def sunny():
    """ Define function that draws the sun in the sky"""
    sun = turtle.Turtle()
    sun.speed(0)
    sun.hideturtle()
    sun.color("yellow")
    sun.penup()
    sun.speed(0)
    sun.goto(-500, 200)
    sun.pendown()
    sun.begin_fill()
    for i in range(10, 50):                            #Draws circular sun
        sun.circle(i)
    sun.end_fill()

def cloudsky():
    """ Define function that draws the clouds in the sky"""
    cloud = turtle.Turtle()                             #turtle that draws clouds in the sky in the form of 3 circles
    cloud.speed(0)
    cloud.hideturtle()
    cloud.penup()
    cloud.color("white")
    cloud.goto(500,200)
    cloud.begin_fill()
    cloud.circle(40)
    cloud.end_fill()

    cloud.goto(460,220)
    cloud.begin_fill()
    cloud.circle(40)
    cloud.end_fill()

    cloud.goto(450,170)
    cloud.begin_fill()
    cloud.circle(40)
    cloud.end_fill()

def tree():
    """ Define function that draws the trees"""
    tr = turtle.Turtle()                               #Draws tree. First rectangle, then circles
    tr.hideturtle()
    tr.color("#808000")
    tr.penup()
    tr.goto(-300, -180)
    tr.pendown()
    tr.begin_fill()
    tr.left(90)
    tr.forward(90)
    tr.left(90)
    tr.forward(20)
    tr.left(90)
    tr.forward(90)
    tr.end_fill()

    trtop = turtle.Turtle()
    trtop.hideturtle()
    trtop.color("#008000")
    trtop.penup()
    trtop.goto(-310, -90)
    trtop.pendown()
    trtop.begin_fill()
    trtop.circle(40)
    trtop.end_fill()

    tr.penup()
    tr.goto(300, -180)
    tr.pendown()
    tr.begin_fill()
    tr.left(90)
    tr.forward(20)
    tr.left(90)
    tr.forward(90)
    tr.left(90)
    tr.forward(20)
    tr.left(90)
    tr.forward(90)
    tr.end_fill()

    trtop.penup()
    trtop.goto(310, -90)
    trtop.pendown()
    trtop.begin_fill()
    trtop.circle(40)
    trtop.end_fill()


def main():
    """ Define main function to call the previously defined functions"""
    wn = turtle.Screen()
    wn.bgcolor("#008000")  # set background color to #008000
    background()                            #Calling the background function
    pathlead()                              #Calling the pathlead function
    tree()                                  #Calling the tree function
    sunny()                                 #Calling the Sunny function
    cloudsky()                              #Calling the Cloudsky function
    sqareshape()                            #Calling the Squareshape function
    roofing()                               #Calling the roofing function
    chimneytop()                            #Calling the Chimney function
    frontdoor()                             #Calling the frontdoor function
    window()                                #Calling the window function
    wn.exitonclick()
main()                                      #Terminating main function


