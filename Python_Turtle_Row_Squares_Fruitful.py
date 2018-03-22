##Use turtle module with user-input GUI dialogue boxes and fruitful functions to
##create centered pattern withsame shape of same size in user desired quantity.

##Module
import turtle

##Set up Turtle Screen
wn = turtle.Screen()
wn.setup (width=1.00, height=1.00, startx=None, starty=None)
wn.bgcolor("black")
wn.title("Row of Non-Fruitful Squares")

##User Import Gui
TN = wn.textinput("Turtle Name","What is your turtle's name? ")
clr = wn.textinput("Turtle Color","What color do you want "+TN+" to be? ")
sz = int(wn.numinput("Size","What size would you like the pattern? ",5,.5,50))
nm = int(wn.numinput("Quantity","How many squares should "+TN+" draw? ",5,1,20))

##Set up Turtle
TN = turtle.Turtle()
TN.color(clr)
TN.pu()
TN.pensize(5)
TN.shape("arrow")

##Definitions
def square(sz): ##Basic square
    for i in range(4):
        TN.forward(sz)
        TN.left(90)

def row_squares(sz,nm): ##fruitful function
    for i in range(nm):
        square(sz)
        TN.pu()
        TN.forward(sz+20)
        TN.pd()
def start_position(sz,nm): ##move turtle back at start, so pattern is screen centered
    TN.home()
    TN.pu()
    TN.backward(((sz+20)*nm)/2)
    TN.pd()

def make_turtle_pattern(sz,nm): ##create pattern
    start_position(sz,nm)
    row_squares(sz,nm)
    TN.pu()

##Call functions   
make_turtle_pattern(sz,nm)

wn.mainloop()
