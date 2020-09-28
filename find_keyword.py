content = "İlaç şirketinde HR Recruitment Specialist"
content_sp = content.split()
print( content_sp )
key =['Human','Software','HR', "Recruitment"]

#for i in range ( 0, 4 ): 
for k in range ( 0, 4 ):  
    
    if  key[k] in content_sp:
        print( str(k) + " - " + key[k] )          
        
    else:
        print( str(k) + " - " + "none")

