##Create Farenheit/Celsius Converter with User GUI

##########Modules##################
import turtle

##########Set up Turtle Screen#####
wn = turtle.Screen()
wn.setup (width=1.00, height=1.00, startx=None, starty=None)
wn.bgcolor("black")
wn.title("Farenheit/Celsius Converter")

trt = turtle.Turtle()
trt.pu()
trt.color("yellow")

##########Input/Variable###########
Temp = wn.textinput("Temperature Type","Choose F for Farenheit or C for Celsius: ")

##########Functions################
def farenheit(Degree):
    A = Degree
    b = round(((A * 1.8) + 32),2)
    trt.write(("Your temperature in Farenheit is", b), False, align='center', font=("Arial",18,"normal"))

def celsius(Degree):
    X = Degree
    i = round(((X - 32) / 1.8),2)
    trt.write(("Your temperature in Celsius is", i), False, align='center', font=("Arial",18,"normal"))

def Conversion():
    if Temp is "F" or Temp is "f":
        Degree = float(wn.numinput("Degree","What is the temperature? "))
        celsius(Degree)
        ##break
    elif Temp is "C" or Temp is "c":
        Degree = float(wn.numinput("Degree","What is the temperature? "))
        farenheit(Degree)
        ##break
    else:
        trt.write('Choose F or C', False, align='center',
              font=("Arial",18,"normal"))

###########Calls####################
Conversion()

###########Quit###############
wn.mainloop()

