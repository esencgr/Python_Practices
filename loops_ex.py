# # -*- coding: utf-8 -*-

# # ---------------------------------- Problem 1 ----------------------------------,

# # Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
# # Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
# # Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

# tot = 0
# num = int(input( "number : " ))
# for i in range( 1, num ):
#     if( num % i == 0 ):
#         tot += i

# if( num == tot ):
#     print( "number is perfect. " )
# else:
#     print( "not perfect.")
    
    
    
# # ---------------------------------- Problem 2 ----------------------------------

# # Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

# # Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin 
# # toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
# # Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
# tot = 0
# number = input( "number : " )
# digit = len( number )
# num = int( number )

# while( num > 0 ):
#     dig = num % 10
#     num //= 10 
#     tot += dig**digit 
#     print( dig )

# #print( number, tot )
# if( int( number )  == int( tot ) ):
#     print( "number is perfect. " )
# else:
#     print( "not perfect.")
    


# # ---------------------------------- Problem 3 ----------------------------------

# # 1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın
# # İpucu: İç içe 2 tane for döngüsü kullanın. 
# # Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
# res = 1 
# for i in range( 1, 11 ):
#     print( f" DIGIT-{ i } ".center( 30 ,'*' ) )
#     for j in range( 1, 11 ):
#         print( f"{ i } x { j } = { i*j }" )

        

# # ---------------------------------- Problem 4 ----------------------------------

# # Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği 
# # sayıları "toplam" isimli bir değişkene ekleyin. 
# # Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
# # i :while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.

# sm = 0
# while( True ):
#     num = input( "number : " )
#     if( num == 'q' ):
#         break
#     sm += int( num )

# print( "sum = ", sm)



# #   ---------------------------------- Problem 5 ----------------------------------

# # 1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın.
# # Bu işlemi continue ile yapmaya çalışın.

# for i in range( 1, 100 ):
#     if( i % 3 != 0 ):
#         continue
#     else:
#         print( i )



# #   ---------------------------------- Problem 6  ----------------------------------

# # Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. 
# # Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan 
# # syaılaradan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

# # Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla 
# # da öğrendiğimiz şeyler olur. Bu problemde deneme yanılma yoluyla list comprehension'ın 
# # koşullu durumlarla kullanımını öğreneceksiniz.

# # İpucu: Basit düşünmeye çalışın.

# lst = [ x for x in range( 1, 100 ) if (x % 2 == 0) ]
# # print( lst )

# l = [ "6" if( y % 3 == 0) else "odd" for y in lst  ]
# print( l )