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

def rectlength (area, width):

    length = area / width

    lengthrounded = round(length, 2)

    print "The length is ", lengthrounded

def rectwidth (area, length):

    width = area/length

    widthrounded = round(width, 2)

    print "The width is ", widthrounded

def rectdiagonal (length, width):

    diagonal = math.sqrt((width*width)+ (length * length))

    diagonalrounded = round (diagonal, 2)

    print "The diagonal length of this rectangle is ", diagonalrounded

def rectperimeter (length, width):

    perimeter = 2*(length + width)

    perimeterrounded = round (perimeter, 2)

    print "The perimeter is ", perimeterrounded

def squarearea (side):

    area = side * side

    arearounded = round(area, 2)

    print "The area of this sqaure is ", arearounded

def squareperimeter (side):

    perimeter = 4 * side

    perimeterrounded = round(perimeter, 2)

    print "The perimeter is ", perimeterrounded

def squarediagonal (side):

    diagonal = math.sqrt(2) * side

    diagonalrounded = round(diagonal, 2)

    print "The diagonal is ", diagonalrounded


shape = raw_input("What's the shape you working with? (Enter C for circle, T for Triangle, S for Sqaure, or R for rectangle) \n")

if shape == "c" or "C":

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

if shape == "T" or "t":
    function = raw_input("What are you trying to figure out about the triangle? (Base, Height , Area, Perimeter) \n")

    if function == "area":

        base = float(raw_input("For this I would need two variables. The base and the height. What's the base? \n"))
        height = float(raw_input("And the Height? \n"))

        print "Got it"

        trianglearea(base, height)


    elif function == "base":

        a = float(raw_input("I need the area and the height! What's the area? \n"))

        h = float(raw_input("And the Height? \n"))

        print "Thank you."

        time.sleep(2)

        trianglebase(a, h)


    elif function == "height":

        area = float(raw_input("Gotcha. What is the area? \n"))

        base = float(raw_input("And the base? \n"))

        print "Calculating..."

        time.sleep(3)

        triangleheight(area, base)

    elif function = "perimeter":

        sidea = float(raw_input("Ah perimeter. For this I would need three things. 2 sides (A and C), and the base. Let's start with Side A, what is it?" \n))

        base = float(raw_input("And the base?" \n))

        sidec = float(raw_input("Last but not least, what's side C?"))

        print "Thank you! On it..."

        time.sleep(3)

        triangleperimeter(sidea, base, sidec)

    else:

        print "Not a valid response."

if shape == "R" or "r":

    function = raw_input("Rectangle it is! What are you looking to calculate? (Area, length, width, diagonal, perimeter) \n")

    if function == "area" or "Area":

        print "Area huh? \n"

        length = float(raw_input("I will need the length and the width to calculate it. Let's start with the base. What's the base? \n"))

        width = float(raw_input("Now enter the width: \n"))

        print "Got it!"

        time.sleep(3)

        rectarea(length, width)

    if function "length" or "Length":

        area = float(raw_input("For the length, I need to things. The area, and the width. What's the area? \n"))

        width = float(raw_input("Got it. And the width? \n"))

        print "....."

        time.sleep(3)

        rectlength(area, width)

    if function = "width" or "Width":

        area = float(raw_input("For the area, I will need the area and the length of the Rectangle. Enter the area. \n"))

        length = float(raw_input("Now the length: \n"))

        print "On it!"

        time.sleep(3)

        rectwidth(area, length)

    if function == "Diagonal" or "diagonal":

        length = float(raw_input("Ah, diagonal. Okay. I would need the length and width. Give me the length first: \n"))

        width = float(raw_input("Now the width: \n"))

        print "On it!"

        time.sleep(3)

        rectdiagonal(length, width)

    if function == "Perimeter" or "perimeter":
        length = float(raw_input("Perimeter. Okay. I would need the length and width. Give me the length first: \n"))

        width = float(raw_input("Now the width: \n"))

        print "On it!"

        time.sleep(3)

        rectperimeter(length, width)

if shape == "S" or "s":

    function = raw_input("Rectangle it is! What are you looking to calculate? (Area, Perimeter, Diagonal) \n")

    if function == "area" or "Area":
        print "Area huh? \n"

        side = float(raw_input("I will need to know the side of the square. What is it? \n"))

        print "Got it. Working..."

        time.sleep(3)

        squarearea(side)

    if function "perimeter" or "Perimeter":

        side = float(raw_input("For the perimeter, I only need the side. What is the side? \n"))

        print "....."

        time.sleep(3)

        squareperimeter(side)

    if function = "diagonal" or "Diagonal":

        side = float(raw_input("For the diagonal, I only need to know the side. What is the side? \n"))

        print "Working..."

        time.sleep(3)

        squarediagonal(side)
