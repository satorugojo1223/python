import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.title("Anime Battle")
screen.bgcolor("black")
screen.setup(width=900, height=500)

# Health bars
health_hero = 100
health_enemy = 100

# Draw health bars
bar = turtle.Turtle()
bar.hideturtle()
bar.penup()

def draw_health():
    bar.clear()
    # Hero health
    bar.goto(-400, 200)
    bar.color("white")
    bar.write("HERO", font=("Arial", 12, "bold"))
    bar.goto(-400, 180)
    bar.color("cyan")
    bar.begin_fill()
    bar.forward(health_hero * 2)
    bar.right(90)
    bar.forward(20)
    bar.right(90)
    bar.forward(health_hero * 2)
    bar.right(90)
    bar.forward(20)
    bar.end_fill()
    bar.setheading(0)

    # Enemy health
    bar.goto(200, 200)
    bar.color("white")
    bar.write("ENEMY", font=("Arial", 12, "bold"))
    bar.goto(200, 180)
    bar.color("red")
    bar.begin_fill()
    bar.forward(health_enemy * 2)
    bar.right(90)
    bar.forward(20)
    bar.right(90)
    bar.forward(health_enemy * 2)
    bar.right(90)
    bar.forward(20)
    bar.end_fill()
    bar.setheading(0)

# Characters
hero = turtle.Turtle()
hero.shape("square")
hero.color("cyan")
hero.shapesize(2, 2)
hero.penup()
hero.goto(-300, -50)

enemy = turtle.Turtle()
enemy.shape("square")
enemy.color("red")
enemy.shapesize(2, 2)
enemy.penup()
enemy.goto(300, -50)

draw_health()
time.sleep(1)

# Hero dash attack
for _ in range(15):
    hero.forward(15)
    time.sleep(0.02)

health_enemy -= 30
draw_health()

# Energy blast
blast = turtle.Turtle()
blast.shape("circle")
blast.color("yellow")
blast.shapesize(1)
blast.penup()
blast.goto(hero.xcor() + 30, hero.ycor())

for _ in range(20):
    blast.forward(20)
    time.sleep(0.02)

blast.hideturtle()
enemy.goto(350, -50)

# Enemy counter
health_hero -= 20
draw_health()
time.sleep(0.5)

# Finish move
text = turtle.Turtle()
text.hideturtle()
text.color("white")
text.penup()
text.goto(0, 0)
text.write("🍑 FINAL STRIKE 🍆", align="center", font=("Arial", 28, "bold"))

time.sleep(1)

enemy.goto(600, -50)
health_enemy = 0
draw_health()

text.clear()
text.write("🏆 HERO WINS 🏆", align="center", font=("Arial", 30, "bold"))
print("DJKGHSD")
turtle.done()
