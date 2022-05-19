# Take input from user
primeNumber = int(input("Input the number you want to list prime numbers under: "))

if primeNumber > 1:

    # Defining the prime number
    for i in range(2, int(primeNumber / 2) + 1):

        # If primeNumber is divisible by any number between
        # 2 and primeNumber / 2, it is not prime
        if (primeNumber % i) == 0:
            print(primeNumber, "is not a prime number")
            break
    else:
        print(primeNumber, "is a prime number")

else:
    print(primeNumber, "is not a prime number")


print("\nAll prime numbers up to", primeNumber, "are : ")


for num in range(2, primeNumber + 1):


    i = 2


    for i in range(2, num):
        if(num % i == 0):
            i = num
            break;


    # Print prime numbers.
    if(i != num):
        print(num, end=" ")
