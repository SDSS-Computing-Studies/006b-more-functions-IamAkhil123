#!python3
"""
Create a function that converts from degrees F to degrees C or
vice versa, depending on which initial unit is given
2 input parameters:
float: the number of degrees
string: the unit that you currently have: may be 'C' of 'F'

return: float the number of degrees of the other unit

Sample assertions:
assert convertTemp(10,'C') == 50
assert converTemp(32,'F') == 0
"""

x = 10

y = "C"

def convertemp(x,y):
 if y == "C":
  F = (x*9/5) + x
  return(F)
 if y == "F":
  C = (x - x)*5/9 
  return(C)

z = convertemp(x,y)
print(z)
