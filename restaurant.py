import os 

tables = dict ()
for i in range (0, 5):
    tables[i] = 0

def add_pay ():
    tab_no = int (input ("enter table no : "))
    add = float (input ("added pay : "))
    tables[tab_no] += add    

def del_pay ():
    tab_no = int (input ("enter table no : "))
    ex = float (input ("deleted pay : "))
    ch = tables[tab_no] - ex 

    if ch < 0:
        print ("invalid process. pay is not enough.")
    else: 
        tables[tab_no] = ch


def file_check (file_name):
    try:
        # when the finished process close file automaticaly
        with open (file_name, 'r') as file:
            data = file.read()
            data = data.split("\n")
            data.pop()
            flag = True

    except FileNotFoundError:
        # when the finished process close file automaticaly
        with open (file_name, 'w') as file:
            flag = False

    if flag:
        for item in enumerate(data):
            tables[item[0]] = float (item[1])
    else:
        pass

def file_update (file_name):
    with open (file_name, 'w') as file:
        for i in range (0,5):
            pay = tables[i]
            pay = str(pay) + "\n"
            file.write (pay)

def main ():

    file_check ("restaurant.txt")

    while (True):
        os.system("clear")
        file_update ("restaurant.txt")

        print( 
        """
        [1] show tables.
        [2] add pay.
        [3] del pay.
        [q] quit.
        """)
        
        case = input ("enter your choise : ")

        if case == "1":
            for i in range (0, 5):
                print (f"table {i} : {tables[i]}")
            print ("done. tab enter for rechoose.")
            input ()

        if case == "2":
            add_pay()
            print ("done. tab enter for rechoose.")
            input ()

        if case == "3":
            del_pay()
            print ("done. tab enter for rechoose.")
            input ()

        if case == "q":
            print ("quitting.")
            quit ()

main()