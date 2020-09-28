# İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

# Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi, 
# dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

# Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı 
# eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. 

# Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.

shape = input( "enter side number of shape : " ) 

if( shape == "4" ):
    
    a = int(input( "side1 = " ))
    b = int(input( "side2 = " ))
    c = int(input( "side3 = " ))
    d = int(input( "side4 = " ))
  
    if( a == b == c == d ):
        print( "A square." )
    elif( a == b and c == d ):
        print( "A rectangle.")
    else:
        print( "A quadliteral.")
        
elif( shape == "3" ):
    
    a = int(input( "side1 = " ))
    b = int(input( "side2 = " ))
    c = int(input( "side3 = " ))
    
    res = (abs( a-b ) < c < abs( a+b )) and (abs( a-c ) < b < abs( a+c )) and (abs( b-c ) < a < abs( b+c ))
    
    if( res ):   

        if( a == b == c ):
            print( "A equilateral triangle." )
        elif( a == b or a == c or b == c ):        
            print( "a isosceles triangle." )
        elif( (a ** 2) + (b ** 2) == (c ** 2) or (b ** 2) + (c ** 2) == (a ** 2) or (a ** 2) + (c ** 2) == (b ** 2) ):
            print( "A right triangle" ) 
        else:
            print( "Only a triangle" )

    else:
        print( "Not a triangle.")

else: print( "invalid shape !")






