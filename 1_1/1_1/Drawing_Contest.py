from abc import get_cache_token
import turtle
from typing import BinaryIO
t = turtle.Turtle()
t.speed(0)
t.pensize(8)
t.penup()
t.goto(0,-100)
t.pendown()

#head
for i in range(36):
  t.forward(30)
  t.left(10)

#eyes
t.penup()
t.goto(80,90)
t.pendown()





wn = t.Screen()
wn.mainloop()