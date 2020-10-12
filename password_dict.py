# -*- coding: utf-8 -*-

d = { "Kerem":"3242", "Asya":"9087" }

names = d.keys()
nm = input( "enter name : " )

if nm in names:
    print( f"welcome { nm } ..!" )
    p = input("password : " )
    
    if p == d[ nm ]:
        print( "logged in." )
    else:
        print( "invalid log in ." )      

else:
    print( "no users found!")