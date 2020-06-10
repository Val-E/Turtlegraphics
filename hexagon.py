import turtle, time


turtle.speed(10000)
            
colors = [ "red","purple","blue","green","orange","yellow"]
pen = turtle.Pen()

for x in range(360):
   pen.width(25)
   pen.pencolor(colors[x % 6])
   pen.forward(x)
   pen.left(59)


time.sleep(10)
