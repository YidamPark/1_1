#group members: George, Jeramiah, Kunsh, Yidam
import turtle as trtl
painter = trtl.Turtle()

#ask user for the slope, and y-intercept (POSITIVE NUMBERS ONLY)
eq = input("Enter the equation in y=mx+b form: ")
slope = int(input("Enter the slope: "))
turn = 45/slope
yint = int(input("Enter the y-intercept: "))


    
#graph (the y, x axis, and dashes)
def make_graph():
    painter.speed(0)
    painter.setposition(0,0)
    
    for i in range (4):
        painter.forward (400)
        painter.backward(400)
        painter.right(90)
    
    painter.setposition(-400,0)
    for i in range (80):
        painter.forward(10)						
        painter.right(90)
        painter.backward(5)
        painter.forward(5)
        painter.left(90)
    painter.penup()
    painter.setposition(0,400)
    painter.pendown()
    painter.right(90)
    for i in range (80):
        painter.forward(10)
        painter.right(90)
        painter.backward(5)
        painter.forward(5)
        painter.left(90)

make_graph()

#creating the y-int
painter.setposition(0,0)
painter.left(180)
painter.forward(yint*10)

#creating a line
painter.pendown()
painter.right(turn)
painter.backward(500)
painter.forward(1000)




wn = trtl.Screen()
wn.mainloop()