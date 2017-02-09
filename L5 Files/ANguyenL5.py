def main():
    number_string = input('Enter a sequence of digits with nothing separating them: \n')
    total = string_total(number_string)

    print('The total of the digits in the string you entered is', str(total)+'.')

# The string_total method receives a string and returns
# the total of all the digits contained in the string.
# The method assumes that the string does not contain
# non-digit characters
def string_total(string):
    # Local variables
    total = 0
    number = 0

    for i in range(0,len(string)):
        number = int(string[i])    #changed string to an int() form.
        total += 
    return total		#changed the return to "total"

# Call the main function.
main()

