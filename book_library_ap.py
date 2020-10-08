# -*- coding: utf-8 -*-
book_list = list()
book_list =  [ "dava", "beyaz diş" ]

menu = """

 --- MENU --- 
a -> add book 
d -> delete book 
s -> show book list 
q -> quit
       
       """
       
def add( books ):
    new = input( "enter book name for add : " )
    books.append( new )
    # books += [ new ]
    return books 

def delete( books ):
    dl = input( "enter book name for delete : " )
    books.remove( dl )
    return books 

def show( books ):
    c = 0
    for book in books:
        c += 1
        print( f"{c} : {book}" )

while True: 
    print( menu )
    ch = input( "enter your choise : " )
    print()
    
    if( ch == "a" ):
        update = add( book_list )
        # print( f"Updated book list : {update}" )
        print( "\nupdated list " ) 
        show( update )
        
    elif( ch == "d" ):
        update = delete( book_list ) 
        # print( f"Updated book list : {update}" )
        print( "\nupdated list " ) 
        show( update )
        
    elif( ch == "s" ):
        update = show( book_list )
    
    elif( ch == "q" or ch == "Q" ):
        print( "End ..." )
        break 
    
    else:
        print( "Wrong input. Try again !!" )

        
        
        