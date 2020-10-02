# -*- coding: utf-8 -*-
import pandas as pd 
# intialise data of lists. 
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18] }
df = pd.DataFrame( data )
print( df )

    
d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3 : "three"}

# adds element with key 3
d.update(d1)
print(d)