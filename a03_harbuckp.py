# Name : Priss Harbuck

# Username : harbuckp

# Google Doc link : https://docs.google.com/document/d/1QbDxboNXIvGIt7XvtQryX8-r2sUDNTo9Sd8HJN7CYas/edit?usp=sharing
import turtle


def rectangle(t, sz, leftsz):
    t.forward(sz)
    t.right(90)
    t.forward(leftsz)
    t.right(90)
    t.forward(sz)
    t.right(90)
    t.forward(leftsz)

def snowflakes(t, sz, petals ):
    petals = 3

    t.shape("turtle")
    t.color("#4181EE")
    t.penup()
    for backpetal in range (2):

        for flower in range(12):
            t.stamp()
            t.right(30)
        t.shapesize(petals - 1)
        t.color("#72A6FD")
        petals = 3

def main():

    wn = turtle.Screen()
    wn.bgcolor('#FADADD')

    nex = turtle.Turtle()
    nex.shapesize(5)

    nex.penup()
    nex.backward(200)
    nex.left(90)
    nex.backward(200)
    nex.pendown()

    rectangle(nex, 500, 500)
    nex.penup()
    nex.backward(25)
    nex.right(90)
    nex.forward(150)
    nex.pendown()
    for coloumns in range(2):

         for windows in range(6):
            rectangle(nex, 100, 50)
            nex.penup()
            nex.backward(80)
            nex.right(90)
            nex.pendown()
         nex.penup()
         nex.left(90)
         nex.forward(480)
         nex.right(90)
         nex.forward(150)
         nex.pendown()

    for topwin in range(6):
        rectangle(nex, 25, 50)
        nex.penup()
        nex.backward(80)
        nex.right(90)
        nex.pendown()
    nex.penup()
    nex.backward(450)
    nex.left(90)
    nex.forward(450)
    nex.pendown()
    nex.right(90)
    rectangle(nex, 100, 60)

    nex.goto(-100,-150)
    snowflakes(nex, 90, 10)

    nex.goto(200, 200)
    snowflakes(nex,90,10)

    wn.exitonclick()
main()
