# EX : Calculate the body mass index according to the height and weight values ​​received
# from the user and print the following outputs .

#  Body Mass Index: Weight / Height (m) * Height (m)

#  If BMI is below 18.5 -------> Weak
#  If BMI is between 18.5 and 25 ------> Normal
#  If your BMI is between 25 and 30 --------> Overweight
#  If BMI is over 30 -------------> Obese,
 
h = float(input("height:"))
w = int(input("weight:"))

bm = w / ( h ** 2 )

if ( bm < 18.5):
    print( f"your bm = {bm:.8f} -- weak ")
    
elif ( bm >= 18.5 and bm < 25):
    print( f"your bm = {bm:.8f} -- Normal ")
    
elif ( bm >= 25 and bm < 30):
    print( f"your bm = {bm:.8f} -- Owerweight ")
    
else:
    print( f"your bm = {bm:.8f} -- Obese ")



