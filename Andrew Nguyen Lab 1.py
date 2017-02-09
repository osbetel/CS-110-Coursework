#Written by Andrew Nguyen
#Program for converting feet to meters (assuming 1 foot =.3048 meters)
#I was curious as to how I could get the program to re-run and ask for more inputs; eg, if someone had several
#values they needed to convert. And I came across the "while" loop and "break" statement.
name = input("What is your name?")
while True:
    length = float(input("What is the length, in feet, that you wish to convert?"))
    def feet_to_meter(length):
        return length * .3048
    length = feet_to_meter(length)
    print("")
    print('Your converted length is',
          length)
    print("")
    print("Ready for the next value to be converted!")

    #This piece of code below is currently defective
    if length == "":
        break
print("Thanks for using this program!")