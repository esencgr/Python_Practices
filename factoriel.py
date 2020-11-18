# -*- coding: utf-8 -*-
while( True ):
    p = 3
    num = (input( "enter number( exit : q ) = " ))
    
    if( num == "q" ):
        break
    
    else:
        num = int( num )
        while( num != 1 ):
            p *= num 
            num -= 1 
        print( p )