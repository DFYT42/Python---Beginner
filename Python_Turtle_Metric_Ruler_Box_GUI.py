##With user input GUI, have Turtle create metric_ruler with (n) length
##representing large, medium, and fine ruler ticks. Will need
##conditionals with logic to choose 1(3) tick sizes based on tick value.
##Using metric_ruler, create a square, with each side being a ruler.
##Must use helper functions

################Modules##############
import turtle

########Turtle & Screen Setup########
'''create screen'''
wn = turtle.Screen()
'''set screen color to black'''
wn.bgcolor("black")
'''set screen size to size of user monitor'''
wn.setup(width=1.00, height=1.00, startx=None, starty=None)

'''create turtle'''
alex = turtle.Turtle()
'''set turtle to white'''
alex.color('white')
'''set turtle run speed to 0, which is fastest possible without hiding movement and
simply printing the output'''
alex.speed(0)

############GUI Input################
'''User GUI input set to integer'''
n = int(wn.numinput('Ruler Length Input','How long would you like the ruler to be? ',10,minval=10, maxval=150))

############Functions################
def ruler_values(t,i):
    '''write value of hash mark on ruler'''
    t.right(90)
    t.pu()
    t.forward(15)
    t.pd()
    t.write(str(i))
    t.pu()
    t.backward(15)
    t.pd()
    t.left(180)

def tens_hash(t,i):
    '''make hash mark for non-terminating tens place'''
    t.forward(20)
    t.backward(20)
    t.right(90)
    t.forward(5)

def tens_last_hash(t,i):
    '''make hash mark for terminating tens place'''
    t.forward(20)
    t.backward(20)
    t.right(90)

def fives_hash(t,i):
    '''make hash mark for non-terminating fives place'''
    t.forward(10)
    t.backward(10)
    t.right(90)
    t.forward(5)

def fives_last__hash(t,i):
    '''make hash mark for terminating fives place'''
    t.forward(10)
    t.backward(10)
    t.right(90)

def small_hash(t,i):
    '''make hash mark for non-terminating non 5s and 10s place'''
    t.left(90)
    t.forward(1)
    t.backward(1)
    t.right(90)
    t.forward(5)

def small_last_hash(t,i):
    '''make hash mark for terminating non 5s and 10s place'''
    t.left(90)
    t.forward(1)
    t.backward(1)
    t.right(90)

    
def ruler_tics(t,n):
    '''create 3 sizes of ruler tics based on 10s, 5s, and inbetweens'''
    for i in range(n+1):
        if i % 10 == 0 and i < n:
            '''all 10s tic marks that are not the last tic on the ruler'''
            ruler_values(t,i)
            tens_hash(t,i)
        elif i % 10 == 0:
            '''last tic on ruler. turn turt to start onactula ruler to make things even all around'''
            ruler_values(t,i)
            tens_last_hash(t,i)
        elif i % 5 == 0 and i < n:
            '''all 5s tic marks that are not the last tic on the ruler'''
            ruler_values(t,i)
            fives_hash(t,i)   
        elif i % 5 == 0:
            '''last tic on ruler. turn turt to start onactula ruler to make things even all around'''
            ruler_values(t,i)
            fives_last__hash(t,i)
        elif i < n:
            '''all non 5s and non 10s tic marks that are not the last tic on the ruler'''
            small_hash(t,i)            
        else:
            '''last tic on ruler. turn turt to start onactula ruler to make things even all around'''
            small_last_hash(t,i)
            

def ruler_square(t,n):
    '''start turtle in position that leaves box centered'''
    t.home()
    '''to make ruler box centered, need to move turtle backward and down by half the user input (n).
    However, tic marks are set with a distance of 5 "lengths", which means the user input must first
    be multiplied by 5.'''
    a = (n*5)/2
    t.pu()
    t.backward(a)
    t.right(90)
    t.forward(a)
    t.left(90)
    t.pd()
    '''create a square using the ruler function above'''
    for i in range(4):
        ruler_tics(t,n)
        t.left(90)


######################Call##############      
ruler_square(alex,n)

