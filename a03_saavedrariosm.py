###########################################
#Author: Maria Belen Saavedra Rios
# Username: saavedrariosm
#Assignment: A03 - Functional Turtles
#GoogleDoc: https://docs.google.com/document/d/1DFhV70cZmoOaaq1cZl99u7mQhiwm7WyH-I19KNgILmk/edit?usp=sharing
#Project: Bolivian Traum (Bolivian dream)
###########################################

import turtle

#Waves
def olas (lg):
    olitas = turtle.Turtle()
    olitas.hideturtle()
    olitas.speed(10)
    olitas.penup()
    olitas.shape("circle")
    olitas.color (61,89,171)
    olitas.pensize(30)
    olitas.goto (-650, 0)
    olitas.pendown()

    for olas in range (8):
        olitas.forward (lg)
        olitas.right(90)
        olitas.forward(30)
        olitas.right(90)
        olitas.forward(lg)
        olitas.left(90)
        olitas.forward(30)
        olitas.left(90)

#Mountains
def montanitas (hght):
    monta = turtle.Turtle()
    monta.hideturtle()
    monta.speed(0)
    monta.pensize(6)
    monta.color(150, 75, 0)
    monta.penup()
    monta.goto(-800, 10)
    monta.right (45)
    monta.pendown()

    for mountains in range (4):
        monta.begin_fill()
        monta.left(90)
        monta.forward(hght)
        monta.right(90)
        monta.forward(hght)
        monta.end_fill()

def sun():
    solecito = turtle.Turtle()
    solecito.hideturtle()
    solecito.speed(0)
    solecito.penup()
    solecito.goto(0, 200)
    solecito.begin_fill()
    solecito.pendown()
    solecito.color ("yellow")
    solecito.circle(50)
    solecito.end_fill()


#Clouds
def sky ():
    clouds = turtle.Turtle()
    clouds.color (0,139,139)
    clouds.hideturtle()
    clouds.speed(0)
    clouds.penup()
    clouds. goto(350, 280)
    clouds.pendown()

    for a in range(80):
        clouds.circle(8+a, 20)

    clouds.penup()
    clouds.goto(-350, 280)
    clouds.pendown()

    for a in range(80):
        clouds.circle(8+a, 20)

def main ():
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(152, 245, 255)
    wn.title("Bolivien Traum")
    wave_1 = turtle.Turtle()

    sky()
    montanitas(280)
    sun()
    olas(1800)

    wn.exitonclick()
main()
