import turtle

win = turtle.Screen()
win.screensize(400, 500)
win.title("polygon")

t = turtle.Turtle()
t.color("navy")
side = 3
angle = 360 / side
t.width(6)
t.fillcolor("red")
t.write("oye ye dekh totka",font=('impact',24,"bold"))

t.begin_fill()
for i in range(side):
    t.forward(90)
    t.left(angle)
t.left(90)
t.penup()
t.forward(55)# do it #
t.pendown()
t.right(90)
for i in range(side):
    t.forward(90)
    t.right(angle)
t.end_fill()

turtle.done()
