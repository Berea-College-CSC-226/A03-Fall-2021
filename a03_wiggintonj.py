############################################################################
#Name: Johann Wigginton
#Username: wiggintonj
#Google Doc Link: https://docs.google.com/document/d/1nqHOh27QOILOovLKE5weqfz1OBob_-g0hBAEVfbxx7k/edit?usp=sharing
############################################################################

import turtle
import random
def main_building (t, color, width, length):
    """ Creates the main structure of the house
    Parameters:
        t: controls the turtle assigned
        color: User can control the color of the main structure
        length: User controls how tall the main structure is
        width: User controls how wide the main structure is """
    t.penup()
    t.color(color)
    t.setpos(-300,0) #Starting position of the main building
    t.begin_fill()
    t.pendown()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.color('') #Makes the turtle invisible. Makes overall picture cleaner without the turtles.


def roof (t, color, base, side):
    """Creates the roof of the house
    Parameters:
        t: controls the turtle assigned
        color: User controls what color the roof is
        base: User chooses how wide the base of the roof is (recommended to be width of the main building)
         side: User controls how long the sides of the roof are"""
    t.penup()
    t.color(color)
    t.setpos(-300,225)
    t.begin_fill()
    t.pendown()
    t.forward(base)
    t.left(160)
    t.forward(side)
    t.left(40.6)
    t.forward(side)
    t.left(160)
    t.end_fill()
    t.color('')



def first_windows (t, color,  width, length):
    """Creates two windows on the first floor
    Parameters:
        t: controls the turtle assigned
        color: User decides what color the windows can be
        width: User decides how wide the windows can be
        length: User decides how tall the windows can be"""
    t.penup()
    t.color(color)
    t.setpos(-250,75)
    t.pendown()
    t.begin_fill()
    # Creates the first window
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.penup()
    t.forward(375)
    t.pendown()
    t.begin_fill()
    # Creates the second window
    for j in range(2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.color('')

def second_windows (t, color, width, length):
    """Creates three windows on the second floor
        Parameters:
            t: controls the turtle assigned
            color: User decides what color the windows can be
            width: User decides how wide the windows can be
            length: User decides how tall the windows can be"""
    t.penup()
    t.color(color)
    t.setpos(-250, 150)
    t.pendown()
    t.begin_fill()
    # Creates the first window
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.penup()
    t.forward(225)
    t.pendown()
    t.begin_fill()
    # Creates the second window
    for j in range(2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.penup()
    t.forward(200)
    t.pendown()
    t.begin_fill()
    # Creates the third window
    for k in range(2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.color('')

def chimney (t, color, width, length):
    """Creates two chimneys on the roof
        Parameters:
            t: controls the turtle assigned
            color: User decides what color the chimneys can be
            width: User decides how wide the chimneys can be
            length: User decides how tall the chimneys can be"""
    t.penup()
    t.color(color)
    t.setpos(-150,225)
    t.pendown()
    t.begin_fill()
    #Creates the first chimney
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.penup()
    t.forward(250)
    t.pendown()
    t.begin_fill()
    # Creates the second chimney
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.color('')


def chimney_smoke (t, smoke_puffs, size):
    """Creates puffs of smoke from the chimneys
    Parameters:
        t: controls the turtle assigned
        smoke_puffs: User can decide how many smoke puffs come out of the chimney
        size: Determines the size of the smoke puffs. Doubles as the distance between smoke puffs."""
    t.color('gray')
    t.shape("circle")
    t.penup()
    t.pensize(size)
    t.setpos(-133.5, 345) #Positions the turtle over the left chimney
    t.left(90)
    #Creates the first set of smoke puffs
    for puffs in range(smoke_puffs):
        t.stamp()
        t.forward(size)
        t.pensize(size-3)
    t.setpos(133.5, 345) #Positions over the right chimney
    t.pensize(size + (smoke_puffs*3))
    #Creates the second set of smoke puffs
    for puffs in range(smoke_puffs):
        t.stamp()
        t.forward(size)
        t.pensize(size - 3)
    t.color('')

def door (t, color, width, length):
    """Creates the door to the house
    Parameters:
        t: controls the turtle assigned
        width: User decides how wide the door can be
        length: User decides how tall the door is"""
    t.color(color)
    t.penup()
    t.setpos(-75, 0)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.color('')

def sun (t, color, x, y, diameter):
    """Creates a sun in the sky
    Parameters:
        t: controls the turtle assigned
        color: User can decide on the color of the sun
        x: User can position the sun along the x axis
        y: User can position the sun on the y axis
        diameter: User can choose the diameter of the sun"""
    t.penup()
    t.color('')
    t.shape('circle')
    t.setpos(x, y) #Allows user to choose where the sun will be positioned
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(diameter)
    t.end_fill()
    t.color('')
def walkway (t, length):
    """Creates a walkway to the house
    Parameters:
        t: controls the turtle assigned
        length: User can decide how long the walkway is"""
    t.color('gray')
    t.penup()
    t.setpos(-75,0)
    t.right(90)
    t.pendown()
    t.begin_fill()
    #Creates the walkway to the house
    for i in range(2):
        t.forward(length)
        t.left(90)
        t.forward(145)
        t.left(90)
    t.end_fill()
    t.color('')
def lawn (t, color):
    """Creates the lawn in front of the house
    Parameters:
        t: controls the turtle assigned
        color: User decides what color the lawn will be"""
    t.penup()
    t.color(color)
    t.setpos(-1000, 0)
    t.pendown()
    t.begin_fill()
    #Creates the lawn
    for i in range(2):
        t.forward(2000)
        t.right(90)
        t.forward(1000)
        t.right(90)
    t.end_fill()
    t.color('')
def flowers(w, t):
    """Creates a random set of flowers on the lawn.
    Parameters:
        w: designates the screen
        t: controls the turtle assigned
    Note: Credit to Ahmed and Destiney for helping me with this function"""

    out_count = 0 # Creates a counter for how many times the turtle goes out of the window
    #Sets the boundaries of the screen
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    x_check = t.xcor()
    y_check = t.ycor()
    inLawn = True
    #Conditionals for when the turtle goes out of the window
    if x_check > topBound or x_check < bottomBound:
        out_count += 1
        print(out_count)
        if out_count >= 2: #If the turtle goes out twice, it stops making flowers.
            inLawn = False
    if y_check > rightBound or y_check < leftBound:
        # out_count = 0
        out_count += 1
        print(out_count)
        if out_count >= 2:
            inLawn = False

    t.setpos(0, -1)
    return inLawn


def main():
    #Creating the turtles
    wn = turtle.Screen()
    turtle.colormode(255) #Allows for RGB inputs (R,G,B)
    wn.bgcolor(150, 252, 255)
    building = turtle.Turtle()
    roofturtle = turtle.Turtle()
    windows_1 = turtle.Turtle()
    windows_2 = turtle.Turtle()
    chimneyturtle = turtle.Turtle()
    smoke = turtle.Turtle()
    doorturtle = turtle.Turtle()
    sol = turtle.Turtle()
    walker = turtle.Turtle()
    grass = turtle.Turtle()
    flowerturtle = turtle.Turtle()
    #Setting the speeds so it draws faster
    grass.speed(15)
    building.speed(15)
    roofturtle.speed(15)
    windows_1.speed(15)
    windows_2.speed(15)
    chimneyturtle.speed(15)
    smoke.speed(15)
    doorturtle.speed(15)
    sol.speed(15)
    walker.speed(15)
    flowerturtle.speed(150)
    #Creates the different parts of the house using the functions
    chimney(chimneyturtle, (104, 4, 0), 50, 100)
    sun(sol, (255, 254, 150), -300, 200, 50)
    main_building(building, (88, 40, 29), 600, 225)
    roof(roofturtle, (255, 251, 214), 600, 324)
    first_windows(windows_1, (194, 225, 249), 125, 50)
    second_windows(windows_2, (194, 225, 249), 75, 50)
    chimney_smoke(smoke, 3, 20)
    door(doorturtle, "brown", 145, 75)
    lawn(grass, "green")
    while flowers(wn, flowerturtle): #Makes flowers using the random list until the inLawn variable becomes false
        x = random.randrange(-750, 750)
        y = random.randrange(-375, 1)
        flowerturtle.penup()
        flowerturtle.setpos(x, y)
        color = ["yellow", "blue", "white", "red", "orange", "purple"]
        #Credit to Ahmed and Destiney for helping with this bit of code to pull randomly from the list
        random_color = random.choice(color)
        for i in range(5):
            flowerturtle.color(random_color)
            flowerturtle.stamp()
            flowerturtle.forward(1)
            flowerturtle.right(72)

    walkway(walker, 500)





    wn.exitonclick()
main()


