#google doc url: https://docs.google.com/document/d/1UUqDmJ4APa8-0tSr_X2cgbOJ8YeuLmK-QRMGKhsDHYc/edit?usp=sharing
#Author: Victor Hernandez
#username: hernandezvi

import turtle                               #allows us to use the turtle library

def create_roof(shin):                      #designs the roof of the house
    shin.fillcolor('brown')
    shin.begin_fill()
    shin.penup()
    shin.setpos(-100, 50)
    shin.pendown()
    shin.lt(45)
    shin.fd(100)
    shin.rt(45)
    shin.fd(220)
    shin.rt(45)
    shin.fd(100)
    shin.rt(135)
    shin.fd(360)
    shin.end_fill()
    shin.penup()
    shin.home()

def make_house_wall(shin):                  #designs the walls of the house
    shin.fillcolor('#FFDAB9')               #color that will fill in the shape made by the turtle
    shin.begin_fill()
    shin.penup()
    shin.setpos(-100, 50)
    shin.pendown()
    for i in range(2):                      #a loop that will make a square
        shin.fd(360)
        shin.rt(90)
        shin.fd(300)
        shin.rt(90)
    shin.end_fill()
    shin.penup()
    shin.home()

def make_ground(shin):                          #designs the ground of the house
    shin.setpos(-100, -250)
    shin.fillcolor('#778899')
    shin.begin_fill()
    shin.fd(360)
    shin.rt(45)
    shin.fd(60)
    shin.rt(135)
    shin.fd(430)
    shin.end_fill()
    shin.home()

def make_window(shin, x, y):                    #designs the windows
    shin.penup()
    shin.pensize(2)                             #gives the pen a specific size
    shin.setpos(x, y)                           #this will take any coordinates that will be assigned in the 'main' function
    shin.fillcolor('#3776ab')
    shin.begin_fill()
    for i in range(4):
        shin.pendown()
        shin.fd(100)
        shin.rt(90)
    shin.end_fill()
    shin.penup()
    shin.home()
    shin.setpos(x+50, y)
    shin.pendown()
    shin.rt(90)
    shin.fd(100)
    shin.penup()
    shin.bk(50)
    shin.lt(90)
    shin.pendown()
    shin.fd(50)
    shin.bk(100)
    shin.penup()
    shin.home()

def make_door(shin):                            #designs the door
    shin.setpos(50, -150)
    shin.fillcolor('#8B7355')
    shin.pensize(1/8)
    shin.begin_fill()
    shin.pendown()
    for i in range(2):
        shin.fd(60)
        shin.rt(90)
        shin.fd(100)
        shin.rt(90)
    shin.end_fill()
    shin.penup()
    shin.fd(50)
    shin.rt(90)
    shin.fd(50)
    shin.shape('circle')                    #will give the turtle the shape of a circle
    shin.shapesize(1/4)
    shin.color('#000000')
    shin.stamp()
    shin.home()

def make_chimney(shin):                     #designs the chimney
    shin.setpos(-40, 70)
    shin.pendown()
    shin.fillcolor('#CD661D')
    shin.begin_fill()
    for i in range(2):
        shin.fd(40)
        shin.lt(90)
        shin.fd(100)
        shin.lt(90)
    shin.end_fill()
    shin.penup()
    shin.lt(90)
    shin.fd(100)
    shin.lt(90)
    shin.fd(10)
    for y in range(2):
        shin.pendown()
        shin.fillcolor('#8A360F')
        shin.begin_fill()
        shin.rt(90)
        shin.fd(20)
        shin.rt(90)
        shin.fd(60)
        shin.end_fill()
    shin.penup()
    shin.home()

def make_text(shin, txt):                   #writes text on the screen

    shin.color('#528B8B')
    shin.setpos(-20,200)
    shin.write(txt, move=False, align='center', font=("Arial", 30, ("bold", "normal")))


def filled_circle(shin, radius):            #starting elements for the cloud function
    shin.color("#FFFAFA")
    shin.begin_fill()
    shin.circle(radius)
    shin.end_fill()


def cloud(shin, radius, x, y):              #makes the white clouds also using the function filled circle
    shin.setpos(x, y)
    filled_circle(shin, radius)
    shin.fd(radius)
    filled_circle(shin, radius)
    shin.rt(90)
    filled_circle(shin, radius)
    shin.rt(65)
    filled_circle(shin, radius)
    shin.rt(75)
    filled_circle(shin, radius)
    shin.rt(85)


def main():

    turtle.colormode(255)           # change color modes

    wn = turtle.Screen()            # Makes a new turtle screen
    shin = turtle.Turtle()          #name of the turtle
    shin.hideturtle()               #hides the turtle shape
    shin.speed(10)                  #assigns the turtle the speed in which it will draw
    wn.bgcolor('#97FFFF')           #color of the background
    radius = 30                     #radius of the function cloud

    # Function calls for each part of the house
    create_roof(shin)
    make_house_wall(shin)
    make_ground(shin)
    make_window(shin, -80, 40)
    make_window(shin, 140, 40)
    make_window(shin, -80, -130)
    make_window(shin, 140, -130)
    make_door(shin)
    make_chimney(shin)
    make_text(shin, 'Victors House')
    cloud(shin, radius, -220, 130)
    cloud(shin, radius, 220, 200)

    wn.exitonclick()  # wait for user to click on the window to close


main() # call main()

