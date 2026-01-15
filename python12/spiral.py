import turtle

win = turtle.Screen()
win.screensize(400,500)
t = turtle.Turtle()
t.color("green")
side = 5
t.write("guys here is a illusion",font=('impact',24,"bold"))
while True:
    t.forward(side)
    t.right(90)
    side+=1
turtle.done()