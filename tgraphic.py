from turtle import *
from random import randint

# Set up the screen
bgcolor("midnight blue")
speed(0)
hideturtle()
tracer(0)  # Turn off animation for faster drawing

def moveToRandom():
    penup()
    goto(randint(-300, 300), randint(-300, 300))
    pendown()

def drawStar(size, col):
    color(col)
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()

def drawGalaxie(radius):
    for _ in range(15):
        moveToRandom()
        drawStar(randint(2, 4), "light blue")

def drawConstellation(No_of_star):
    moveToRandom()
    stars_positions = []

    for _ in range(No_of_star):
        drawStar(randint(7, 15), "white")
        stars_positions.append(pos())
        left(randint(-90, 90))
        forward(randint(30, 70))

    # connect the stars with lines
    color("white")
    pensize(1)
    penup()
    for i in range(len(stars_positions) - 1):
        goto(stars_positions[i])
        pendown()
        goto(stars_positions[i + 1])
        penup()

# Draw scattered stars
for _ in range(30):
    moveToRandom()
    drawStar(randint(5, 20), "white")

# Draw multiple galaxies
for _ in range(3):
    drawGalaxie(40)

# Draw constellations
for _ in range(2):
    drawConstellation(5)

update()
done()
