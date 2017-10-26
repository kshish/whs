import turtle

running = True
radius=200
angle=181
x=0
y=0
x=x-(radius/2)
y=y-(radius/2)
pencolorR=1
pencolorG=1
pencolorB=1
turtle.ht()
turtle.pu()
turtle.goto(-100, -100)
turtle.pd()

turtle.tracer(0, 0)
turtle.colormode(255)
turtle.pencolor(pencolorR, pencolorG, pencolorB)

while running == True:
    turtle.circle(radius)
    turtle.pu()
    turtle.lt(angle)
    turtle.fd(radius/2)
    turtle.pd()
    turtle.update()
    pencolorR=pencolorR+3
    if pencolorR>=255:
        pencolorR=1
    pencolorG=pencolorG+2
    if pencolorG>=255:
        pencolorG=1
    pencolorB=pencolorB+1
    if pencolorB>=255:
        pencolorB=1
    turtle.pencolor(pencolorR, pencolorG, pencolorB)
   
