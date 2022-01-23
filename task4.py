#!python3

"""
Create a function that determines the 
area of a circle if given the radius
1 input parameter
float: radius

return: float area for the circle

note: Area of a circle is given by A = pi*(square of the radius)
You may want to use the math module to complete this problem
"""

import math

r = 2

def area(r):
 A = math.pi*r*r
 A = round(A, 2)
 return(A)

x = area(r)
print(x)





def area():
    return

