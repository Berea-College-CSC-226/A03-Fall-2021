#############################################################################################
#Name- Paw Ehler Thaw
#Username- thawp
#Google Docs- https://docs.google.com/document/d/1vAkZUZCNQb8ppk8OlM3QBfpPQNnIhSuhVdzuft6QXjQ/edit?usp=sharing
#############################################################################################

import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.hideturtle()
tess.speed(10)
tess.pensize(5)
wn.bgcolor("black")
tess.pencolor("white")



# start of the head
def make_head():
    """
    this function makes the head of the robot
    :return:
    """
    tess.penup()
    tess.setpos(-80, 150)
    tess.pendown()

    for i in range(4):
        tess.forward(100)
        tess.right(90)


#start of face
def make_face():
    """
    this function makes the face of the robot which includes the left and right eyes and the mouth
    :return:
    """
    tess.penup()
    tess.setpos(-60, 110)
    tess.pendown()
    tess.circle(10)             #left eyes

    tess.penup()
    tess.setpos(0, 110)         #right eyes
    tess.pendown()
    tess.circle(10)

    tess.penup()
    tess.setpos(-10, 85)
    tess.pendown()

    for i in range(4):
        tess.right(90)
        tess.forward(20)       #mouth
        tess.right(90)
        tess.forward(50)

def make_neck():
    """
    this function makes the neck of the robot
    :return:
    """
    tess.penup()
    tess.setpos(0, 49)
    tess.pendown()

    for i in range(4):
        tess.right(90)
        tess.forward(20)
        tess.right(90)
        tess.forward(55)

#start of the body
def make_body():
    """
    this function created the rectangle that is the body of the robot
    :return:
    """
    tess.penup()
    tess.setpos(-115, 29)
    tess.pendown()
    wn.colormode(255)
    tess.fillcolor(255, 165, 0)
    tess.begin_fill()

    for i in range(4):
        tess.forward(180)
        tess.right(90)
        tess.forward(120)
        tess.right(90)
    tess.end_fill()
#start of left leg
def make_leg():
    """
    this function creates both the left and the right leg of the robot using rectangles
    :return:
    """
    tess.penup()
    tess.setpos(-60, -90)
    tess.pendown()

    for i in range(4):
        tess.right(90)
        tess.forward(120)
        tess.right(90)
        tess.forward(20)
#start of left foot
    tess.penup()
    tess.setpos(-70, -230)
    tess.pendown()
#start of right leg
    tess.penup()
    tess.setpos(30, -90)
    tess.pendown()
    for i in range(4):
        tess.right(90)
        tess.forward(120)
        tess.right(90)
        tess.forward(20)
def make_arms():
    """
    This function created both the left and the right arms of the robot
    :return:
    """
#Start of right arm
    tess.speed(10)
    tess.penup()
    tess.setpos(63, 11)
    tess.pendown()
    tess.forward(75)
    tess.right(90)
    tess.forward(70)
    tess.right(90)
    tess.forward(25)
    tess.right(90)
    tess.forward(50)
    tess.left(90)
    tess.forward(47)
#start of left arm
def make_circles():
    """
    This function creates five various circles in different spots with different colors
    :return:
    """
    tess.speed(10)
    tess.penup()
    tess.setpos(-117, 8)
    tess.pendown()
    tess.forward(47)
    tess.right(90)
    tess.forward(50)
    tess.left(90)
    tess.forward(25)
    tess.left(90)
    tess.forward(70)
    tess.left(90)
    tess.forward(75)
#start of circles 1
    tess.speed(10)
    tess.penup()
    tess.setpos(200, 100)
    tess.pendown()
    tess.pencolor("pink")
    r = 5
    n = 5
    for i in range(1, n + 1, 1):
        tess.circle(r * i)
#start of circle 2
    tess.speed(10)
    tess.penup()
    tess.setpos(-100, 200)
    tess.pendown()
    tess.pencolor("blue")
    r = 6
    n = 6
    for i in range(1, n + 1, 1):
        tess.circle(r * i)
#start of circle 3
    tess.speed(10)
    tess.penup()
    tess.setpos(-250, 100)
    tess.pendown()
    tess.pencolor("purple")
    r = 6
    n = 6
    for i in range(1, n + 1, 1):
        tess.circle(r * i)
#start of circle 4
    tess.speed(10)
    tess.penup()
    tess.setpos(-280, -50)
    tess.pendown()
    wn.colormode(255)
    tess.pencolor(115, 135, 120)
    r = 6
    n = 6
    for i in range(1, n + 1, 1):
        tess.circle(r * i)
#start of circle 5
    tess.speed(10)
    tess.penup()
    tess.setpos(200, -100)
    tess.pendown()
    wn.colormode(255)
    tess.pencolor("green")
    r = 6
    n = 6
    for i in range(1, n + 1, 1):
        tess.circle(r * i)

def main():
    make_head()
    make_face()
    make_neck()
    make_body()
    make_leg()
    make_leg()
    make_arms()
    make_circles()
main()


wn.exitonclick()