#Name/author: Dimitrios Ntentia
#Username: ntentiad
#date created: 09/15/2021
#google doc link: https://docs.google.com/document/d/18KyUXaJU4-X-hoknCF4zLGkTmabaT63LZOBg8_nuRv8/edit?usp=sharing



import turtle

wn=turtle.Screen()
depressed = turtle.Turtle()


def sun(t):
    '''draws a sun'''
    t.pensize(20)
    t.pencolor("yellow")
    t.circle(50)
    for i in range(9):
        t.penup()
        t.circle(50, 40)
        t.pendown()
        t.right(90)
        t.forward(25)
        t.left(180)
        t.forward(25)
        t.right(90)
def house(t):
    ''''We are creating the squared block, that will be our house'''
    t.pensize(10)
    t.pencolor("black")
    t.left(90)
    for i in range(2):
        t.forward(250)
        t.left(90)
        t.forward(200)
        t.left(90)
    t.forward(250)
    triangle(t)
def triangle(t):
    '''we will need this function for the roof of the house'''
    for i in range(2):
        t.left(60)
        t.forward(115)

def windows(t):


    t.pensize(5)
    for i in range(4):
        t.forward(25)
        t.right(90)
    t.forward(12.5)
    t.right(90)
    t.forward(12.5)
    t.left(90)
    t.pendown()
    t.forward(12.5)
    t.forward(-25)
    t.right(90)
    t.forward(-12.5)
    t.forward(25)
def main():
    wn.bgcolor("light blue")
    wn.screensize(800, 700)
    depressed.penup()
    depressed.goto(-300, 200)
    depressed.pendown()
    sun(depressed)#building a sun
    depressed.penup()
    depressed.goto(300, -350)#going into the location to draw the house
    depressed.pendown()
    house(depressed)
    depressed.penup()
    depressed.left(60)
    depressed.forward(150)
    depressed.left(90)
    depressed.forward(80)
    depressed.pendown()
    windows(depressed)
    depressed.right(180)
    depressed.penup()
    depressed.forward(120)
    depressed.pendown()
    depressed.right(90)
    windows(depressed)
    depressed.right(180)
    depressed.penup()
    depressed.right(30)
    depressed.forward(300)
    depressed.pendown()
    depressed.pencolor(0.2, 0.8, 0.55)
    depressed.left(90)
    for i in range(7):
        depressed.forward(100)
        depressed.forward(-20)
        depressed.left(90)
        depressed.forward(100)
        depressed.forward(-50)
        depressed.right(90)
    wn.exitonclick()

main()










