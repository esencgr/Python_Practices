# -*- coding: utf-8 -*-

while True:
    num = input( "enter number = " )
    
    try:
        print( float( num ) ** 2  )

    except ValueError: 
        print( "you shouldnt enter a string !")
        
    if( num == 0):
        print( "end of the program.. " )
        break
    
