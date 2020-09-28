# 1-100 arası random sayı üret.
# Hak bilgisini kullanıcıdan al ve tahminlere başla.
# Her yanlış cevap için 100 üzerinden optimize puan düş.

import random 

num = random.randint(1,100)
print( num )

chance = int( input( "chance ---> " ))

total = 100 
step = total / chance 
print( f"total point = {total} and each wrong guess decrease {step:.3f} point" )

try_count = 0

for guess in range( 0, chance ):
    guess = int( input( "guess: " ))
    try_count += 1 
    
    if( guess == num ):    
        print( f"\tyou win in {try_count} try !! number : { num } !" )
        print( f"\tfinal point = {total:.3f}" )
        break
    
    elif( guess > num ):
        total -= step
        print( "down.." )
        print( f"point = {total:.3f}" )

    elif( guess < num ):
        total -= step 
        print( "up.." )
        print( f"point = {total:.3f}" )

    if( total == 0 ):   # or chance = try_count
        print( f"\nyou are out of chance !!  number : { num } !" )


    
