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
a = 5

b = 15

c = 12

def triangle(a,b,c):
 if a+b>=c and b+c>=a and c+a>=b:
    sa = pow(a, 2)
    sb = pow(b, 2)
    sc = pow(c, 2)
    if a*a + b*b == c*c:
        return("2")
    if (a != b or a != c or b != c):
        return("1")
    if (sa > sc + sb or sb > sa+sc or sc > sa+sb):
        return("3")
 else:
        return("0")

x = triangle(a,b,c)
print(x)



