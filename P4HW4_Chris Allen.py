import turtle
redCross = turtle.Screen()
x = turtle.Turtle()
x.color("red")            # set x turtle color
x.pensize(3)               # set x turtle width

print("It's a red cross!")
print ()
# use a for loop
for redCross in range (4):
    x.forward(150)
    x.left(90)
    x.forward(150)
    x.left(90)
    x.forward(150)
    x.right(90)
