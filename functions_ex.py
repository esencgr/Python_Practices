# -*- coding: utf-8 -*-

# # 1- Gönderilen bir ifadeyyi belirtilen bir sayı kez ekrana bastıran fonksiyonu yazdırın
# def pr( s, n ):
#     print( s * n )
#     # for i in range( 0, n ):
#     #     print( s )
#
# word = input( "enter string : " )
# num = int( input( "enter num : " ))
# pr( word, num )


# # 2- Sınırsız sayıdaki parametreyi listeye çeviren fonksiyon
# def con_lst( *params ):
#     lst = list()
#     for param in params:
#         lst.append( param )
#     return lst
#
# new = con_lst( 1, 2, 3, 4, "hello", "cool" )
# print( new )


# # 3- Gönderilen iki sayı arası asal sayılar 
# def prime( n1, n2 ):
#     for num in range( n1, n2 ):
#         if( num > 1 ):
#             var = True 
#             for i in range( 2, num ):
#                 if( num % i == 0 ):
#                     var = False 
#             if ( var == True ):
#                 print( num )
# prime( 0, 30 )


# # 4- Kendisine gönderilen sayının tam bölenlerini listeye ekle yazdır
# def div( num ):
#     lst = list()
#     for i in range( 1, num + 1 ):
#         if( num % i == 0 ):
#             lst.append( i )
#     return lst 
# print( lst )
#
# number = int( input( "enter :" ))
# divs = div( number )
# print( divs )
