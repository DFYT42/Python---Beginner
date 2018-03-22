##Function within a function, def stop_when_circle_xd(t,R):
##A drunk pirate has been brought in for being drunk and disorderly. The pirate
##executes a random walk of random steps, with random turn angles between
##each step, and stops first time they hit the wall, which is >= radius of
##R from its start point.
##Use user input to decide the jail cell size and draw a circle of radius R.
##Use turtle position() function, which returns the x and y coordinate
##for the current position of the turtle.
##Print out the number of steps drunken pirate takes before
##hitting jail cell wall.

#################Modules Imported#################
import turtle
import random
import math

#################Screen Setup#################
'''create screen'''
wn = turtle.Screen()
'''set screen color to black'''
wn.bgcolor("black")
'''set screen size to size of user monitor'''
wn.setup(width=1.00, height=1.00, startx=None, starty=None)
'''set screen title'''
wn.title("Drunken Pirate")

#################Turtle Setup#################
'''initialize alex'''
drunk_pirate = turtle.Turtle()
drunk_pirate.color("white")
'''initialize tess'''
jail_cell = turtle.Turtle()
jail_cell.color("hotpink")

#################Inputs#################
'''ask user for desired radius of circle in which drubken pirate will wander'''
R = wn.numinput("Jail Cell Size","What is the Jail Cell Radius?",
    25,minval=20, maxval=300)

#################Functions#################
def draw_circle(t,R):
    '''tess draws a circle'''
    t.pu()
    t.lt(90)
    t.bk(R)
    t.rt(90)
    t.pd()
    t.circle(R)

def stop_when_circle_xd(t,R):
    '''makes turt t execute random walk of size Dz for each step,
    and stops the first time turt is >= radius of R from its start'''
    current_R = 0
    ##Set current radius position to 0
    num_steps = 0
    ##Set drunken_pirate initial setps to 0
    draw_circle(jail_cell,R)
    ##draw circle based on radius given by user
    while(current_R <= R):
        ##While current radius is less than or equal to User radius
        ngl = random.randint(0,359)
        ##Random number chosen between 0-359 for turn
        t.left(ngl)
        ##turt turn random number
        Dz = random.randint(2,30)
        ##Random number chosen between 0-20 for forward progression
        t.forward(Dz)
        ##add each step drunken pirate takes
        num_steps += 1
        ##determine current x,y position of drunken pirate in draw_circle
        x,y = t.pos()
        current_R = math.sqrt(x**2 + y**2) ##imported with math module
    jail_cell.pu()
    jail_cell.right(90)
    jail_cell.forward(50)
    jail_cell.write(('Drunken Pirate took '+
        str(num_steps)+' steps before hitting jail-cell wall with Radius of '+
        str(R)), True, align='center',
    font=("Arial",18,"normal"))

#################Calls#################
stop_when_circle_xd(drunk_pirate,R)

#################Quit Program#################
wn.mainloop()
