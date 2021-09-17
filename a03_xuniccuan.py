#################################################################################
# Author: Nelson Xunic Cuá
# Username: xuniccuan
#
# Assignment: A03: Functional Turtles
# Purpose: Draw something complex while practicing creating and using functions,
# and more practice on using the turtle library. Also, learn how computers represent colors.
#
# Google Doc Link: https://docs.google.com/document/d/13IwgfbubJQs9GHFnrWd6G7MpxJrX3kWrhevGgu3mOqo/edit?usp=sharing
#
#################################################################################

import turtle
import random
wn = turtle.Screen()
wn.bgcolor("#90ee90")


def function_1():

    turtle_1 = turtle.Turtle()                          # make a new turtle, initialize values
    turtle_1.hideturtle()
    turtle_1.shape("turtle")
    turtle_1.pensize(0.1)
    turtle_1.speed(10)

    turtle_1.up()  # instructions for the first turtle
    turtle_1.goto(-190, -200)
    turtle_1.color("#0000FF")
    turtle_1.down()
    turtle_1.showturtle()

    for n in (range(10, 410, 10)):
        turtle_1.goto(-200, 210 - n)  # defines movement of the turtle
        turtle_1.goto(-200 + n, -200)

    turtle_1.up()  # sets final position of the turtle
    turtle_1.goto(210, 210)
    turtle_1.down()
    turtle_1.right(135)


def function_2():

    turtle_2 = turtle.Turtle()  # make a new turtle, initialize values
    turtle_2.hideturtle()
    turtle_2.shape("turtle")
    turtle_2.pensize(0.1)
    turtle_2.speed(10)

    turtle_2.up()
    turtle_2.goto(200, -190)
    turtle_2.color("#FF0000")
    turtle_2.down()
    turtle_2.showturtle()

    for n in (range(10, 410, 10)):
        turtle_2.goto(-210 + n, -200)  # defines the movement of the turtle
        turtle_2.goto(200, -200 + n)

    turtle_2.up()  # sets final position of the turtle
    turtle_2.goto(-210, 210)
    turtle_2.down()
    turtle_2.right(45)


def function_3():

    turtle_3 = turtle.Turtle()  # make a new turtle, initialize values
    turtle_3.hideturtle()
    turtle_3.shape("turtle")
    turtle_3.pensize(0.1)
    turtle_3.speed(10)

    turtle_3.up()
    turtle_3.goto(190, 200)
    turtle_3.color("#000000")
    turtle_3.down()
    turtle_3.showturtle()

    for n in (range(10, 410, 10)):
        turtle_3.goto(200, -210 + n)  # defines the movement of the turtle
        turtle_3.goto(200 - n, 200)

    turtle_3.up()  # sets final position of the turtle
    turtle_3.goto(-210, -210)
    turtle_3.down()
    turtle_3.left(45)


def function_4():

    turtle_4 = turtle.Turtle()  # make a new turtle, initialize values
    turtle_4.hideturtle()
    turtle_4.shape("turtle")
    turtle_4.pensize(0.1)
    turtle_4.speed(10)

    turtle_4.up()  # instructions for the fourth turtle
    turtle_4.goto(-200, 190)
    turtle_4.color("#FFFF00")
    turtle_4.down()
    turtle_4.showturtle()

    for n in (range(10, 410, 10)):  # defines the movement of the turtle

        turtle_4.goto(210 - n, 200)
        turtle_4.goto(-200, 200 - n)

    turtle_4.up()  # sets final position of the turtle
    turtle_4.goto(210, -210)
    turtle_4.down()
    turtle_4.left(135)


def photo(turtle_5):
    turtle_5 = turtle.Turtle()
    wn.register_shape("Flag_of_Guatemala.gif")
    turtle_5.shape("Flag_of_Guatemala.gif")
    turtle_5.stamp()


def message_1(turtle_5):
    turtle_5 = turtle.Turtle()
    turtle_5.color("#FFFFFF")
    turtle_5.hideturtle()
    turtle_5.penup()
    turtle_5.goto(-150, 215)
    turtle_5.write("September 15", font=("Verdana", 30, "normal"))


def message_2(turtle_5):
    turtle_5 = turtle.Turtle()
    turtle_5.color("#FFFFFF")
    turtle_5.hideturtle()
    turtle_5.penup()
    turtle_5.goto(-187.5, -250)
    turtle_5.write("Independence Day", font=("Verdana", 30, "normal"))


def main():
    my_list = [0, 1, 2, 3]
    for repeat in range(4):  # sets the number of time that the program will run

        counter = random.choice(my_list)       # makes the program run 'randomly,' to get a different pattern
        if counter == 0:                    # Function call to function_1
            function_1()
            my_list.remove(counter)
            print(my_list)
        elif counter == 1:                  # Function call to function_2
            function_2()
            my_list.remove(counter)
            print(my_list)
        elif counter == 2:                  # Function call to function_3
            function_3()
            my_list.remove(counter)
            print(my_list)
        else:                               # Function call to function_4
            function_4()
            my_list.remove(counter)
            print(my_list)
    photo("turtle_5")
    message_1("turtle_5")
    message_2("turtle_5")
    input()

main()
input()