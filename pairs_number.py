
indice = [ 0 ] * 100

def check( indice ):
    total = 0
    n = int( input() )
    for i in range( 0, n ):
        a = int( input() )
        indice[ a ] += 1 

    for c in range( 1, 100 ):
        indice[ c ] /= 2 
        total += int(indice[ c ]) 
            
    return int(total)

res = check( indice )

print( "total_pairs : " + str(res))

