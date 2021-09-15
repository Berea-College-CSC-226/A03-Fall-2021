######################################################################
# Author: Anh N. Ngo
# Username: ngoa

# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Learns about RGB color with turtle and using turtle proficiently
# Google Doc: https://docs.google.com/document/d/14_qzl73L14HsjTSGOL5SGxO3t4WSWaUL987MQjC0A6s/edit#
######################################################################
# Create a function to draw a oval
def draw_oval(t, x, y, big_radius, small_radius, color):
    """
    x: Abscissa on the axis
    y: Ordinate on the axis
    big_radius: the bigger radius of the eclipse
    small_radius: the smaller radius of the eclipse
    color: color using to fill the area
    This is a function to draw different parts of the pigeon by eclipses
    """
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.seth(45)
    t.color(color)
    t.circle(big_radius, 90)
    t.color(color)
    t.circle(small_radius, 90)
    t.color(color)
    t.circle(big_radius, 90)
    t.color(color)
    t.circle(small_radius, 90)
    t.end_fill()

# Create the main function
def main():
    # import turtle module
    import turtle

    # basic setting for screen and turtle characteristics
    turtle.colormode(255)
    screen = turtle.Screen()
    screen.bgcolor("beige")
    screen.screensize(700, 700)
    screen.title("Draw a penguin with Anh!")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.colormode(255)
    """using draw_oral function to draw different parts of the penguin
    and print out a cute text"""

    anh = turtle.Turtle()
    anh.hideturtle()

    # draw big body
    draw_oval(anh, 70,-150, 250,125,(0,0,0))

    # draw eye area
    draw_oval(anh, 72,40, 100,60,(255,255,255))
    draw_oval(anh, -23,40, 100,60,(255,255,255))

    # draw bottom smaller body area
    draw_oval(anh, 55,-150, 200,100,(255,255,255))

    # draw right eye
    draw_oval(anh, 50,100, 30,10,(0,0,0))
    draw_oval(anh, 50,130, 5,5,(255,255,255))

    # draw left eye
    draw_oval(anh, -70,100, 30,10,(0,0,0))
    draw_oval(anh, -70,130, 5,5,(255,255,255))

    # draw mouth
    draw_oval(anh, 15,60, 5,45,"#ffae42")
    draw_oval(anh, -6.5,60, 20,15,"#ffae42")

    # draw feet
    draw_oval(anh, 70,-195, 10,40,(0,0,0))
    draw_oval(anh, -50,-195, 10,40,(0,0,0))

    # draw hand
    draw_oval(anh, 180,55, 10,45,(0,0,0))
    draw_oval(anh, -153,55, 10,45,(0,0,0))

    #Print out 'This is Anh's cute penguin!' on the screen
    anh.up()
    anh.goto(-180, -250)
    anh.down()
    anh.write("This is Anh's cute penguin!", font=("Ink Free", 20, "bold"))

    screen.exitonclick()

main()

