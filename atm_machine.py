# -*- coding: utf-8 -*-
# işlem menusu
#    1 - bakiye sorgulama
#    2 - para yatırma
#    3 - para çekme
#    q - çıkış

money = 1000

while( True ):
    choise = input( "choise : " )

    if( choise == "q" ):
        break

    if( choise == "1" ):
        print( f"total balance = {money}" )

    elif( choise == "2" ):
        ex = int(input( "how much money invest want you : " ))
        money += ex 
        print( f"update balance = {money}" )

    elif( choise == "3" ):
        ex = int(input( "how much withdraw money want you : " ))

        if( money - ex <= 0 ):
            print( f"balance is not enough and now balance = {money} " )
            continue
        money -= ex
        print( f"update balance = {money}" )

    else:
        print( "invalid process " )
