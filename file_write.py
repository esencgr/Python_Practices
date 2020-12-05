
with open('file.txt','w+') as file :
    
    # enter name on terminal
    print("name:", end = "")
    name = input()

    # write name on file
    file.seek(0)
    file.write("name:") 
    file.seek(5)
    file.write(name + "\n")

    # enter visitnumber on terminal
    print("visit:", end = "")
    visit = input()

    # write name on file
    file.write("visit:")
    file.write(visit + "\n")

file.close()

# print(file.closed)
