import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()

y = -200
while (y < 200): 
  y = y + 50
  x = -350
  painter.goto(x,y)
  painter.color("purple")
  painter.stamp()
  
  while (x < 0):
    x = x + 50
    painter.goto(x,y)
    painter.color("orange")
    painter.stamp()