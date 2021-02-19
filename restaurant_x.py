import os 

tables = dict ()

for i in range (0, 5):
    tables[i] = 0 


def file_update (file_name):
    with open (file_name, 'w') as file:
        for i in range (0,5):
            pay = tables[i]
            pay = str(pay) + "\n"
            file.write (pay)
 
file_update ("restaurant.txt")