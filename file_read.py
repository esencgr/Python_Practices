
with open('file.txt','r') as file :
   
    file.seek(0)
    # read file
    res = file.read()
    print(res) 


file.close()

# print(file.closed)
