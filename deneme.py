# -*- coding: utf-8 -*-
# data scraping part
key_word = ['Human','Software','HR','Leader','Manager','Founder','Recruitment',
            'Machine Learning','Data','Vision','Python', 'C++']
content = ['x','a','y','z','t','C++']

def search( con, keys ):
    for c in con:    
        if  c in keys: 
            return True
        
res = search( content , key_word )
print( res )


