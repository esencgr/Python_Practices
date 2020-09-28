# -*- coding: utf-8 -*-

# eq = a.x² + b.x + c = 0
# delta = b² - 4ac 
# x1 = -b + √¯delta / 2a 
# x2 = -b - √¯delta / 2a 
 

print( "Second Degree Equation" )

a = int(input( "a : " )) 
b = int(input( "b : " )) 
c = int(input( "c : " ))

delta = b**2 - 4*a*c 
x1 = (-b + delta**0.5 ) / ( 2*a ) 
x2 = (-b - delta**0.5 ) / ( 2*a ) 

print( "x1 = ", x1 )
print( "x2 = ", x2 )
