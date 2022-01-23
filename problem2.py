#!python3

"""
##### Problem 2
Create a function that determines if a triangle is scalene,
right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is scalene
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 1  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""
import math
a = 1

b = 1

c = 4

def triangle(a,b,c):
 if a+b>=c and b+c>=a and c+a>=b:
      e = [a,b,c]
      q = max(e)
      w = min(e)
      p = sorted(e)
      r = p[1]
      if (q*q>w*w+r*r):
        return("3")
      elif (q*q==w*w+r*r):
        return("2")
      else:
        return("1")
 else:
        return("0")

x = triangle(a,b,c)
print(x)



