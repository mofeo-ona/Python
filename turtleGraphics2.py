from turtle import *
from random import *

speed(-20)
bgcolor("navyblue")
pendown()
color("white")
fillcolor("white")
begin_fill()
penup()
def satr(size,colr,ps):
    for star in range(5):
        fillcolor(colr)
        begin_fill()
        pensize(ps)
        color(colr)
        pendown()
        left(144)
        forward(size)
        end_fill()
        penup()

    forward(100)

def MoveToRandom():
    penup()
    setpos(randint(-350,350), randint(-350,350))
    pendown()

def drawGalaxy(No_of_star):
    color_list = ["yellow","pink","lightblue","white"]
    MoveToRandom()

    for start in range(No_of_star):
        penup()
        left(randint(-1,180))
        forward(randint(1,20))
        pendown()
        satr(10,choice(color_list),3)

def Constellation(No_of_Star):
    MoveToRandom()
    stars_positions=[]

    for _ in range(No_of_Star):
        satr(randint(7,15),"white",2)
        stars_positions.append(pos())
        left(randint(-90,90))
        forward(randint(30,70))

    color("white")
    pensize(1)
    penup()
    for i in range(len(stars_positions)-1):
        goto(stars_positions[i])
        pendown()
        goto(stars_positions[i+1])
        penup()

for _ in range(30):
    MoveToRandom()
    satr(randint(5,25),"white",2)

    for _ in range(3):
        drawGalaxy(4)
    
for _ in range(2):
    Constellation(4)

#Constellation(30)
done()

