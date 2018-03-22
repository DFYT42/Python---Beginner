##Create spiral of multi-colored squares, incrementally incresing in size with Turtles

##Import Turtle module
import turtle
##Initialize Turtle Screen
wn = turtle.Screen()
##Set Background color
wn.bgcolor("black")
##Set Window Title
wn.title("Python Turtle Growing & Colorful Square Spiral")

##Initialize Turtle
alex = turtle.Turtle()
##Set Turtle color and shape
alex.color("pink")
alex.shape("arrow")

#Variables
"Variables are used to assign lengthy lists or equations"
"or any instruction to one small, conside variable, which can be any size"
"although the purpose is to make it simple and easy"
colors = ["red","pink","yellow","white"]
sz = 5 ##Starting size
t = alex ##assigned alex to variable t

##Function
def square(t,sz):
    "make square with every side a different color"
    ##For loop
    for i in colors:
        "for every position in the list ""colors"", do the following"
        t.color(i) ##use the color in this i position
        t.forward(sz) ##move forward sz spaces
        t.left(90) ##squares have right angles of 90 degrees

##Call w For Loop
"Calls can be as simple as calling a function with defined parameters"
"Calls can also be a list of instructions that call functions"
"Calls within calls"
for i in range(25):
    "For every instance,(number 0-24 bc computers start counting at 0)"
    "turtle does the following"
    square(t,sz) ##Call square function
    sz = sz +10 ##for every i, add 10 to the sz in previous i
    t.forward(10) ##move turtle forward
    t.right(20) ##turn turtle

##Close program loop
wn.mainloop()
