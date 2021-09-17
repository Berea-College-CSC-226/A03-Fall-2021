# sky
def sky(t):
    t.pencolor('#66B2FF')
    t.fillcolor('#66B2FF')
    t.begin_fill()
    t.penup()
    t.setpos(-377, 50)  # 1
    t.pendown()
    t.setpos(377, 50) #2
    t.setpos(377, 320) #3
    t.setpos(-377, 320) #4
    t.setpos(-377, 50) #5
    t.end_fill()
#sky()

#sun
def sun(t):
    t.pencolor('yellow')
    t.fillcolor('yellow')
    t.setpos(-377, 220)
    t.begin_fill()

    t.circle(100,120)
    t.setpos(-377, 320)
    t.setpos(-377, 220)
    t.end_fill()
#sun()

# grass
def grass(t):
    t.pencolor('#66B2FF')
    t.setpos(-377, 50) #2

    t.pencolor('green')
    t.fillcolor('#666600')
    t.begin_fill()
    t.pencolor('green')
    t.setpos(373, 50) #3
    t.setpos(374, -310) #3
    t.setpos(-374, -310)
    t.setpos(-377, 50) #2
    t.end_fill()
#grass()

#tree

    # dirt
def dirt(t):
    t.pencolor('#663300')
    t.fillcolor('#663300')
    t.setpos(-377, -200) #2
    t.penup()
    t.circle(-150, -120)
    t.pendown()
    t.right(-60)
    t.begin_fill()
    t.circle(-150, -120)
    t.setpos(-115, -200) #2
    #alex.hideturtle()
    t.end_fill()

#dirt()
def trunk1(t, width, height):
    t.fillcolor('#CC6600')
    t.begin_fill()
    t.setpos(-290, -150)  # 2
    t.setheading(0) # Head to the right
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()
#trunk1(t, 70, 300)

def leaf(t):
    t.penup()
    t.setpos(-350, 150)
    t.pendown()
    t.color("green", "green")
    t.begin_fill()
    t.circle(100)
    t.forward(100)
    t.circle(100)
    t.backward(-30)
    t.left(120)
    t.circle(100)
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.circle(100)
    t.end_fill()
#leaf()



def trunk2(t, width, height):
    t.penup()
    t.color("#CC6600", "#CC6600")
    t.begin_fill()
    t.setpos(0, -200)  # 2
    t.left(180)
    t.pendown()
    t.setheading(1) # Head to the right
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()
#trunk2(t, 70, 300)




def leaf2(t):
    t.penup()
    t.setpos(-60, 150)  # 2
    t.pendown()
    t.color("green", "green")
    t.begin_fill()
    t.circle(100)
    t.forward(100)
    t.circle(100)
    t.backward(-30)
    t.left(120)
    t.circle(100)
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.circle(100)
    t.end_fill()
#leaf2()

def main():
    import turtle

    wn = turtle.Screen()
    alex = turtle.Turtle()

    alex.speed(0)

    wn = turtle.Screen()

    sky(alex)
    sun(alex)
    grass(alex)
    dirt(alex)
    trunk1(alex, 70, 300)
    leaf(alex)
    trunk2(alex, 70, 300)
    leaf2(alex)
    wn.exitonclick()

main()




