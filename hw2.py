from turtle import*
from random import*
bgcolor("midnight blue")
hideturtle()

colors = ["blue","pink","green","orange"]

for i in range(100):
    color(choice(colors))
    forward(i*2)
    left(59)

done()