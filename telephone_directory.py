# -*- coding: utf-8 -*-

d = { "Kerem": { "phone":"0500139200", "job":"engineer" },
      "Asya" : { "phone":"0543789655", "job":"lawyer" } 
    }  

# print( d )

# for k,v in d.items():
#     print( k, v )
#     for k1,v1  in v.items():
#         print( k1, v1 )

name = input( "enter name : " )
name = name.capitalize()
#print( name )

if name in d.keys():
    info = input( "enter info : " )
    info = info.casefold()
    #print( info )
    print( d.get( name ).get( info, "info  is not found !" ) )    
else:
    print( "name is not found !" )
   
