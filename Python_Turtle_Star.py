##Create a star image with Turtles

##Import Turtle module
import turtle

##Initialize Turtle Screen
wn = turtle.Screen()
##Set Background color
wn.bgcolor("Black")

##Set Window Title
wn.title("Python Turtle Star")

##Initialize Turtle
alex = turtle.Turtle()
##Set Turtle color and shape
alex.color("orange")
alex.shape("turtle")

##Input
x = turtle.numinput("Star Size","Enter a number for the Star size (20-425): ",50, minval=20, maxval=425)
"assign a variable to dialog box that initializes to the turtle screen for numeric inputs from the user"
"turtle.numinput(""dialog box name"",""direction for input"",default value,minval=x,maxval=x)"
"default value, minval, & maxval are all optional but consider the user might assume program does not work if the scope"
"occurs outside the screen or is so small it cannot be seen"

##Function
def star(x):
    "using a for loop, create a star image, the size of (x), by moving the turtle"
    "around the screen and drawing only in certain locations"
    alex.left(36)
    "initializes turtle to initial position needed to start drawing a star"
    "sum of ""star arms"" internal angles are 180, which we divide by 5 to get 36 degrees"
    "Every point should have an interior angle of 36 degrees"
    
    for i in range(5):
        "For every instance,(number 0-4 bc computers start counting at 0)"
        "turtle does the following"
        alex.forward(x)
        alex.left(144)
        ##turtle can turn 360 degrees, either left or right
        ##consider which direction turtle is facing when it finishes drawing the straight line by x spaces
        ##consider in what direction turtle needs to face in order to draw the next line
        ##choose which direction you want turtle to turn, (outside the star tip or inside)
        ##For this program, the outside angle was chosen and calculated as 180-36 = 144
        ##If you choose the inside angle, the turtle would need to turn right 180+36 = 216
        
        
    "Move turtle back from final spot so it does not cover the star"
    alex.pu()
    alex.left(54)
    alex.backward(25)
##Call Function
star(x)
"when program runs, this line tells computer to find the definition/function of star and take those actions"
"using the parameters given by default--in this case x = 50--, or by the user"

##Close program loop
wn.mainloop()
