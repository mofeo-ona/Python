from turtle import*

bgcolor("skyblue")
speed(3)

def square(x,y,size, colr):
    penup()
    goto(x,y)
    color(colr)
    begin_fill()
    pendown()
    for _ in range(4):
        forward(size)
        right(90)
    end_fill()

def tri(x,y,l,colr):
    penup()
    goto(x,y)
    color(colr)
    begin_fill()
    pendown()
    for _ in range(3):
        forward(l)
        left(120)
    end_fill()

def rect(x,y,width, height, colr):
    penup()
    goto(x,y)
    color(colr)
    begin_fill()
    pendown()
    for _ in range(2):
        forward(width)
        right(90)
        forward(height)
        right(90)
    end_fill()

square(0,0,200,"blue")
tri(0,0,200,"pink")
rect(50,-100,50,100,"brown")
done()