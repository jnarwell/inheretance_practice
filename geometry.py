#In VS Code, create a module titled geometry and add two functions in there. One that will calculate the area of a circle given a radius. The second will find the hypotenuse of a right angle given the two sides. Import the module or the functions from the module and use it to find the answers to the below questions

#What is the area of a circle with a radius of 7cm?

import math

def area(rad):
    return round(rad**2*math.pi,3)

def hypotonuse(leg1, leg2):
    return round(math.sqrt(leg1**2+leg2**2),3)
