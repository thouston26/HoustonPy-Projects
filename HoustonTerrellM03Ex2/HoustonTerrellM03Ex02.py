#Defining random and getting user input
def main():
    import random
    numberOfTimes = int(input('Enter the amount of random numbers you would like in numeric '))
    counter = 0
    outfile = open('numbers.txt', 'w') #creating outgoing file
    while counter < numberOfTimes:
        randomNumber = random.randint(1, 500)
        counter = counter + 1
        outfile.write(str(randomNumber) + '\n')

    outfile.close()
    print('Data written to numbers.txt') # Printing output file name
    f = open('numbers.txt', 'r')  #displaying output of numbers in txt file
    file_contents = f.read()
    print(file_contents)
    f.close()
main()