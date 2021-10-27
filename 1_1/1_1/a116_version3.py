#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

#body of spider
spider.pensize(40)
spider.circle(20)

number_of_legs = 8
length_of_legs = 100
distance_btwn_legs = 360 / number_of_legs
print("z=", distance_btwn_legs)
spider.pensize(5)

#drawing the spider
amount_of_legs = 0
while (amount_of_legs < number_of_legs):
  ("z*n=", distance_btwn_legs*amount_of_legs)
  spider.goto(0,20)
  spider.setheading(distance_btwn_legs*amount_of_legs)
  spider.forward(length_of_legs)
  amount_of_legs = amount_of_legs + 1
spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()