# ---------------------- CLEAN ---------------------- #

#  clean file content before process
with open('docs.txt','w') as file :
    pass

with open('docs.txt','r+') as file :
    
# ---------------------- WRITE ---------------------- #
    
    # enter name on terminal
    print("\nname : ", end = "")
    name = input()

    # write name on file
    file.seek(0)
    file.write("name : ") 
    file.seek(7)
    file.write(name + "\n")

    # enter visit number on terminal
    print("visit : ", end = "")
    visit = input()

    # write visit number on file
    file.write("visit : ")
    file.write(visit + "\n")

# ---------------------- READ ---------------------- #

    print("\n")

    # file content moves the lst
    file.seek(0)
    lst = file.readlines()
    print(lst)

    print("\n")

    # read file
    file.seek(0)
    res = file.read()
    print(res) 
    print("\n")

    # Access visit number information
    vst = lst[1].split(" : ")
    if (vst[1][:-1] == '0'):
        lst.append("note : new user\n")
    else:
         lst.append("note : old user\n") 
    print(lst)

    # file content moves the lst
    file.seek(0)
    file.writelines(lst)        
    print("\n")

    # read file
    file.seek(0)
    res = file.read()
    print(res) 

file.close()