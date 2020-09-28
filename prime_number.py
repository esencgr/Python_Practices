# -*- coding: utf-8 -*-
check = True
num = int(input( "number : " ))

if( num == 1 ):
    check = False
    
for i in range( 2, num ):
    if( num % i == 0 ):
        check = False
        break
    
if( check ):
    print( f"{num} is prime ")
else:
    print( f"{num} isnt prime ")
