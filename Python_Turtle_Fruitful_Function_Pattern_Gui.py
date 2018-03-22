##Using Python Turtle Module and user input parameters with gui dialogue boxes,
##open screen to width of user monitor and
##create repeated pattern, centered on screen, based on user input
##User parameter options: pattern size,
##pattern speed, and pattern colors.


###############################################################################
##############################'''import module'''##############################
###############################################################################
import turtle

###############################################################################
#################################'''window'''##################################
###############################################################################
wn = turtle.Screen()
wn.setup (width=1.00, height=1.00, startx=None, starty=None)
wn.title("Repeated Turtle Pattern")
wn.bgcolor('black')

###############################################################################
#################################'''turtle'''##################################
###############################################################################
tess = turtle.Turtle()
tess.home() ##Starts turtle at coordinates (0,0)

###############################################################################
###############################'''user inputs'''###############################
###############################################################################
sz = wn.numinput("Size","What size would you like the pattern? ",5,.5,1000)
turtspd = wn.textinput("Turtle Speed","How fast would you like the turtle to draw the pattern: fast or slow? ")
a = wn.textinput("1st Color","What is your first color? ")
b = wn.textinput("2nd Color","What is your second color? ")

###############################################################################
##############################'''simple shapes'''##############################
###############################################################################
def square(sz):
    '''make square'''
    tess.begin_fill()
    for i in range(4):
        tess.forward(sz)
        tess.left(90)
    tess.end_fill()
    tess.forward(sz)

def triangle(sz,c):
    '''make triangle'''
    tess.begin_fill()
    tess.color('',c)
    tess.forward(sz)
    tess.left(90)
    tess.forward(sz)
    tess.left(135)
    tess.forward(hypot(sz))
    tess.end_fill()

def trisqre(sz,a,b):
    '''makes square with diagonal hypot & fill'''
    triangle(sz,a)
    hypmove(sz)
    triangle(sz,b)
    hypmove(sz)
    tess.forward(sz)

def hypmove(sz):
    '''moves turt and neatens up trsq code'''
    tess.backward(hypot(sz))
    tess.right(45)

def hypot(sz):
    '''create diagonal(hypot) for trsq'''
    a = sz**2
    b = sz**2
    c = (a + b)**(.5)
    return float(c)

###############################################################################
############################'''panel rows'''##################################
###############################################################################
def tessmovebk(sz):
    '''move tess for repositioning to start next row'''
    tess.backward(sz*4)
    tess.right(90)
    tess.forward(sz)
    tess.left(90)

def row_1(sz,a,b):
    '''create row 1 in pattern panel'''
    for i in range(4):
        if i <=2:
            tess.color('',a)
            square(sz)
        else:
            tess.color('',b)
            square(sz)
            tessmovebk(sz)

def row_2(sz,a,b):
    '''create row 2 in pattern panel'''
    for i in range(4):
        if i == 0:
            tess.color('',a)
            square(sz)
        elif i == 1 or i == 2:
            tess.color('',b)
            square(sz)
        else:
            trisqre(sz,a,b)
            tessmovebk(sz)

def row_3(sz,a,b):
    '''create row 3 in pattern panel'''
    for i in range(4):
        if i != 1:
            tess.color('',a)
            square(sz)
        else:
            tess.color('',b)
            square(sz)
    tessmovebk(sz)

def row_4(sz,a,b):
    '''create row 4 in pattern panel'''
    for i in range(4):
        if i == 0:
            tess.color('',b)
            square(sz)
        elif i == 1:
            trisqre(sz,a,b)
        else:
            tess.color('',a)
            square(sz)

###############################################################################
####################'''panel--1/4th if pattern quadrant'''#####################
###############################################################################
def panel(sz,a,b):
    row_1(sz,a,b)
    row_2(sz,a,b)
    row_3(sz,a,b)
    row_4(sz,a,b)

###############################################################################
################'''turtle moves/turns within panels/quadrants'''###############
###############################################################################
def panelmove(sz,a,b):
    '''move tess for repositioning to start next panel'''
    tess.left(90)
    tess.forward(sz*4)
    tess.right(90)
    tess.forward(sz*3)
    tess.right(90)
    panel(sz,a,b)

def Quadmove(sz):
    '''move turtle to make quadrant'''
    tess.left(90)
    tess.backward(sz*7)
    tess.right(90)
    tess.backward(sz*72)
    tess.left(90)
    tess.backward(sz)
    tess.right(180)
    tess.forward(sz)
    tess.left(90)

def QuadPatternMove(sz):
    '''move turtle to make quadrant pattern'''
    tess.forward(sz*3)
    tess.right(90)
    tess.forward(sz*5)

def TurtleDrawingStart(sz):
    '''start turtle so center of drawing is at (0,0)'''
    tess.home()
    tess.backward(sz*32)
    tess.left(90)
    tess.forward(sz*28)
    tess.right(90)

###############################################################################
#############################'''pattern building'''############################
###############################################################################

def QuadPattern_1(sz,a,b):
    '''creates one square'''
    for i in range(4):
        if i == 0:
            panel(sz,a,b)
        else:
            panelmove(sz,a,b)
    QuadPatternMove(sz)

def fillpattern1(sz,a,b):
    '''sets colors based on user imputs'''
    for i in range(8):
        if i == 0 or i == 1 or i == 4 or i == 5:
            QuadPattern_1(sz,b,a)
        else:
            QuadPattern_1(sz,a,b)
    Quadmove(sz)

def fillpattern2(sz,a,b):
    '''flips user color inputs'''
    for i in range(8):
        if i == 0 or i == 1 or i == 4 or i == 5:
            QuadPattern_1(sz,a,b)
        else:
            QuadPattern_1(sz,b,a)
    Quadmove(sz)

def QuadPattern_row_1(sz,a,b):
    '''creates first row of 4 X 4 pattern'''
    ##add range(start,stop,step)
    for i in range(8):
        if i == 0 or i == 1 or i == 4 or i == 5:
            fillpattern1(sz,a,b)
        else:
            fillpattern2(sz,a,b)

def TurtleDrawing(sz,turtspd,a,b):
    '''final function to draw 4X4 pattern of quadrants'''
    tess.pu()
    if turtspd == "fast" or turtspd == "Fast":
        turtle.tracer(0,0)
        TurtleDrawingStart(sz)
        QuadPattern_row_1(sz,a,b)
    else:
        turtle.tracer(5,0)
        TurtleDrawingStart(sz)
        QuadPattern_row_1(sz,a,b)

###############################################################################
###############################'''calls'''#####################################
###############################################################################
TurtleDrawing(sz,turtspd,a,b)


wn.mainloop()
