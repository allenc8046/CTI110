import turtle
wn = turtle.Screen()
c = turtle.Turtle()
c.color("blue")            # set C turtle color
c.pensize(3)               # set C turtle width


# draw the C
c.left(180)
c.forward(150)
c.left(90)
c.forward(150)
c.left(90)
c.forward(150)

# space the letters apart
c.penup()
c.forward(50)
c.pendown()

# draw the A
c.left(45)
c.forward(200)
c.right(90)
c.forward(200)
c.left(180)
c.forward(75)
c.left(45)
c.forward(180)


