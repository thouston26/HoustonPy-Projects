
# Getting User Input
n = input("Enter a number: ")
# Defining factorial
factorial = 1
if int(n) >= 1:
 for i in range (1,int(n)+1):
   factorial = factorial * i
 print("Factorail of ",n , " is : ",factorial)
 #Print for error
if int(n) <= 0:
    print("ERROR: Number must be whole, posivite, and greater than 0")




