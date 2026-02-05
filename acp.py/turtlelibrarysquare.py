import turtle

def draw_square():
    for _ in range(4):
        turtle.forward(100)   # move forward 100 units
        turtle.right(90)      # turn right 90 degrees

draw_square()
turtle.done()