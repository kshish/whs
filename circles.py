import turtle

running = True
radius=100
pencolor=1
angle=49
turtle.tracer(0, 0)
turtle.pencolor(pencolor)

while running == True:
    turtle.circle(radius)
    turtle.pu()
    turtle.lt(angle)
    turtle.fd(radius/2)
    turtle.pd()
    turtle.update()
    pencolor=pencolor+1
    if pencolor==255:
        pencolor=1
        
