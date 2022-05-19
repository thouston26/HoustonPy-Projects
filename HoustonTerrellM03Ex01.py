#define string
def value(string):
    count = 0
    for num in str(string)[0:]:
        if num.isdigit() and int(num) in range(10):
            count += int(num)

    return count

#Get the numbers the user inputs
def main():
    user_input_string = input('Enter a set of single digit with no separation: ') #variable for user input

    print('The total value of those numbers ' + str(value(user_input_string)) + '.')


main()