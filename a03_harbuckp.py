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

def snowflakes(X,Y,t, sz):
    t.goto(X,Y)
    t.shape("turtle")
    t.color("#4181EE")
    t.penup()
    t.shapesize(3)
    for backpetal in range (2):

        for flower in range(12):
            t.stamp()
            t.right(30)
        t.shapesize(2)
        t.color("#72A6FD")


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

    nex.fillcolor("#5C6678")
    nex.begin_fill()
    rectangle(nex, 500, 500)
    nex.end_fill()
    nex.penup()
    nex.backward(25)
    nex.right(90)
    nex.forward(150)
    nex.pendown()



    for coloumns in range(2):

         for windows in range(6):
            nex.fillcolor("#DDEDFA")
            nex.begin_fill()
            rectangle(nex, 100, 50)
            nex.penup()
            nex.backward(80)
            nex.right(90)
            nex.pendown()
            nex.end_fill()

         nex.penup()
         nex.left(90)
         nex.forward(480)
         nex.right(90)
         nex.forward(150)
         nex.pendown()



    for topwin in range(6):
        nex.fillcolor("#DDEDFA")
        nex.begin_fill()
        rectangle(nex, 25, 50)
        nex.penup()
        nex.backward(80)
        nex.right(90)
        nex.pendown()
        nex.end_fill()


    nex.penup()
    nex.backward(450)
    nex.left(90)
    nex.forward(450)
    nex.pendown()
    nex.right(90)
    nex.fillcolor("#6B6555")
    nex.begin_fill()
    rectangle(nex, 100, 60)
    nex.end_fill()

    nex.penup()

    snowflakes(-100,-150, nex, 90)

    snowflakes(250, 240, nex,90)

    snowflakes(-200,50, nex,90)

    snowflakes(250, -250, nex, 90)

    snowflakes(-100,60,nex, 90)

    snowflakes(100, 100, nex, 90)

    wn.exitonclick()
main()
