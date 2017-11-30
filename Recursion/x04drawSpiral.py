import turtle

myTurtle = turtle.Turtle()
myCanvas = turtle.Screen()

def drawSpiral(myTurtle, linelength):
    if linelength > 0:
        myTurtle.forward(linelength)
        myTurtle.left(90)
        drawSpiral(myTurtle, linelength - 10)

drawSpiral(myTurtle, 100)
myCanvas.exitonclick()


    