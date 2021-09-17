# Said Maalim                           #a03_maalims
# https://docs.google.com/document/d/1laUQHY-7mgIsRNbiXOhdgg4IhXlRRyVDnslmMxGrgbg/edit?usp=sharing


import turtle               # allows us to use the turtles library


def make_roof(wn, shape):
    """
    A new roof! (Made from an image of bricks)

    :param wn: a turtle Screen object
    :param shape: a Turtle object
    :return: None
    """
    wn.register_shape("Bricks.gif")         # Registers a shape so it can be used by the turtle library
    shape.penup()
    shape.setpos(80,80)
    shape.pendown()
    shape.shape("Bricks.gif")               # Sets the shape to the image registered above
    shape.stamp()

def flag_block(shape, color):
    """
    Makes the main house rectangle.

    :param shape: a Turtle object
    :return: None
    """

    shape.color(color)
    shape.begin_fill()
    for side in range(2):
        shape.forward(200)
        shape.right(90)
        shape.forward(30)
        shape.right(90)
    shape.end_fill()


def make_text(shape, txt):
    """
    Writes text to the screen.

    :param shape: a Turtle object
    :return: None
    """
    shape.color("#0F00F0")
    shape.penup()
    shape.setpos(120,120)
    shape.down()
    shape.write(txt, move=False, align='center', font=("Arial", 30, ("bold", "normal")))


def maalim():
    """
    Draws a house at x, y on the screen.

    :return: None
    """

    turtle.colormode(255)           # change color modes

    wn = turtle.Screen()            # Makes a new turtle screen
    wn.bgpic("hub_karen.gif")      # Sets background to an image; must be a gif!
    shape = turtle.Turtle()
    shape.hideturtle()

    # Function calls for each part of the house

    make_text(shape, "The Karen Nairobi")

    shape.penup()
    shape.setpos(-270, 200)
    shape.pendown()
    flag_block(shape, '#060606')

    shape.setpos(-270, 170)
    flag_block(shape, '#FDFFFE')

    shape.setpos(-270, 140)
    flag_block(shape, '#E21515')

    shape.setpos(-270, 110)
    flag_block(shape, '#15E253')



    wn.exitonclick()  # wait for a user click on the canvas


maalim() # call main()