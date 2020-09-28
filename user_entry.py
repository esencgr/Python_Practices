# -*- coding: utf-8 -*-

us = "cgr"
ps = "1234"
chance = 3 

while( True ):
    
    user = input( "enter username : " ) 
    pwd = input( "enter password : " )
    
    if( user != us and pwd == ps ):
        print( " username is uncorrect ! ".center( 50,'*') )
        chance -= 1 

    elif( user == us and pwd != ps ):
        print( " password is uncorrect ! ".center( 50,'*') )
        chance -= 1 

    elif( user != us and pwd != ps ):
        print( " username and password is incorrect ! ".center( 50,'*') )
        chance -= 1 

    else:
        print( " succesfull login ! ".center( 50,'-') )
        break
    
    if( chance == 0 ):
        print( " dont have any chance ! ".center( 50,'x') )
        break

