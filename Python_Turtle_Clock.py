##Create a clock image with Turtles

##Import Turtle module
import turtle

##Initialize Turtle Screen
wn = turtle.Screen()
##Set Background color
wn.bgcolor("Black")
##Set Window Title
wn.title("Python Turtle Clock")

##Initialize Turtle
alex = turtle.Turtle()
##Set Turtle color and shape
alex.color("orange")
alex.shape("turtle")

##Input
x = turtle.numinput("Clock Size","Enter a number for the clock size (10-425): ",50, minval=10, maxval=425)
"assign a variable to dialog box that initializes to the turtle screen for numeric inputs from the user"
"turtle.numinput(""dialog box name"",""direction for input"",default value,minval=x,maxval=x)"
"default value, minval, & maxval are all optional but consider the user might assume program does not work if the scope"
"occurs outside the screen or is so small it cannot be seen"

##Function
def clock(x):
    "using a for loop, create a clock image, the size of (x), by moving the turtle"
    "around the screen and drawing only in certain locations"
    alex.left(90)
    "initializes turtle to 12:00 position"
    ##For loop
    for i in range(12):
        "For every instance,(number 0-11 bc computers start counting at 0)"
        "turtle does the following"
        alex.pu() ##pick turtle pen up so turtle leaves no trace
        alex.forward(x) ##move turtle x spaces
        alex.pd() ##put turtle pen down to draw again
        alex.forward(20) ##move turtle a set 20 spaces
        alex.pu()
        alex.forward(20) ##move turtle a set 20 spaces
        alex.stamp() ##place a stamp of the turtle shape
        alex.backward(x+40) ##move turtle back the total distance traveled, (x+20+20)
        alex.right(30) ##turn turtle by 30 degrees to position for next loop, (360 degrees in circle/12 clock numbers)

##Call Function
clock(x)
"when program runs, this line tells computer to find the definition/function of clock and take those actions"
"using the parameters given by default--in this case x = 50--, or by the user"

##Close program loop
wn.mainloop()
