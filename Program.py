import time, math

time.sleep(0.5)

print "Hey! Welcome to Shapeator. I can help you find out the values of Shapes (area, height, etc). Be advised that this program will loop until closed."


def circlearea(radius):


    Area = math.pi * radius * radius

    time.sleep(0.5)

    AreaRounded = round(Area, 2)

    print " The Area is ", AreaRounded

def circleradius(Area):

    radius = math.sqrt(Area/math.pi)

    time.sleep(0.5)

    radiusrounded = round(radius, 2)

    print "The Radius is ", radiusrounded

def circlecircumference(radius):

    circum = 2 * math.pi * radius

    circumrounded = round(circum, 2)

    print "The circumference is " , circumrounded

def trianglearea (base, height):

    Area = (height * base) / 2

    Arearounded = round (Area, 2)

    print "The Area of this triangle is " , Arearounded

def trianglebase (area, height):

    base = 2 / (area/height)

    baserounded = round(base, 2)

    print "The base of this triangle is ", baserounded

def triangleheight (area, base):

    height = 2 / (area/base)

    heightrounded = round (height, 2)

    print "The height is ", heightrounded

def triangleperimeter(sidea,base, sidec):

    p = sidea + base+ sidec

    prounded = round(p, 2)

    print "The perimeter is ", prounded

def rectarea(length, width):

    area = length * width

    arearounded = round(area, 2)

    print "The area of this rectangle is ", arearounded


shape = raw_input("What's the shape you working with? (Enter C for circle, T for Triangle, or R for rectangle) \n")

if shape == "circle":

    function = raw_input("What are you trying to figure out? (Radius, Area, Circumference) \n")

    if function == "area":

        r = float(raw_input("To get the area, you only need the radius. What is it?"))

        circlearea(r)

    elif function == "radius":

        a = float(raw_input("I need the area! What's the area?"))
        circleradius(a)

    elif function == "circumference":

        radius = float(raw_input("Gotcha. What is the radius?"))

        circlecircumference(radius)

    else:

        print "Not a valid response"


if shape == "T":
    function = raw_input("What are you trying to figure out? (Base, Height , Area, Circumference) \n")

    if function == "area":

        base = float(raw_input("For this I would need two variables. The base and the height. What's the base? \n"))
        height = float(raw_input("And the Height? \n"))

        print "Got it"

        trianglearea(base, height)


    elif function == "Height":

        a = float(raw_input("I need the area! What's the area?"))
        circleradius(a)

    elif function == "circumference":

        radius = float(raw_input("Gotcha. What is the radius?"))

        circlecircumference(radius)

    else:

        print "Not a valid response"
