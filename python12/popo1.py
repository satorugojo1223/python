
import turtle
win = turtle.Screen()
win = turtle.screensize(400,500)
win.title("polygon")
t = turtle.Turtle()
t.color("navy")
side = 6
angle = 360/side
t.width(6)
t.fillcolor("violet")
t.begin_fill()
for i in range(6):
    t.forward(90)
    t.right(angle)

t.end_fill()


turtle.done()


