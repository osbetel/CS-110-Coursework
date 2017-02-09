#Written by Andrew Nguyen; July 8, 2015
#The purpose of this program is to convert meters/centimeters into feet/inches. The user will be able to select both
#the input unit and the output unit. Conversions will be flexible in that one can select any of the 4 units and
#convert to any of the other units, regardless of whether it is feet-to-meters or inches-to-centimeters, etc.

#c = 5.97
#y = int(c)
#x = format(c - int(a), '.4f')

#print(y)
#print(x)
#CONVERSION RATES
    #1 ft = 30.48 cm
    #1 ft = .3048 m
    #1 in = 2.54 cm
    #1 in = 0.0254 m
    #1 m = 100 cm
    #1 ft = 12 in

name = input("What is your name?")
print("---------------------------")
conversion_unit_input = input("""What is the unit you are starting from?\nEnter "cm" for centimeters, "m" for meters, "ft" for feet, or "in" for inches.""")
conversion_unit_output = input("""What unit would you like to convert to?\nEnter "cm" for centimeters, "m" for meters, "ft" for feet, or "in" for inches.""")
print("---------------------------")



#Start definition of the conversion functions.
#
#
def feet_meters():
    if conversion_unit_input == "ft" and conversion_unit_output == "m":
        length = float(input("What is the length, in feet, that you wish to convert to meters?"))
        print("Your converted length is", float(format(length * .3048, '.4f')), "meters.")
        a = int(length * .3048)
        b = format(length * .3048 - a)
        print("Or,", a, "meter(s) and",format(float(b) * 100, '.2f'), "centimeter(s).")
    if conversion_unit_input == "m" and conversion_unit_output == "ft":
        length = float(input("What is the length, in meters, that you wish to convert to feet?"))
        print("Your converted length is", float(format(length / .3048, '.4f')), "feet.")
        a = int(length / .3048)
        b = format(length / .3048 - a)
        print("Or,", a, "feet and",format(float(b) * 12, '.2f'), "inch(es).")

def feet_inches():
    if conversion_unit_input == "ft" and conversion_unit_output == "in":
        length = float(input("What is the length, in feet, that you wish to convert to inches?"))
        print("Your converted length is", float(format(length * 12, '.4f')), "inches.")
        a = int(length)
        b = format(length - a)
        print("Or,", a, "feet and",format(float(b) * 12, '.2f'), "inch(es).")
    if conversion_unit_input == "in" and conversion_unit_output == "ft":
        length = float(input("What is the length, in inches, that you wish to convert to feet?"))
        print("Your converted length is", float(format(length / 12, '.4f')), "feet.")
        a = int(length / 12)
        b = format(length / 12 - a)
        print("Or,", a, "feet and",format(float(b) * 12, '.2f'), "inch(es).")

def feet_centimeters():
    if conversion_unit_input == "ft" and conversion_unit_output == "cm":
        length = float(input("What is the length, in feet, that you wish to convert to centimeters?"))
        print("Your converted length is", float(format(length * 30.48, '.4f')), "centimeters.")
        a = int(length * .3048)
        b = format(length * .3048 - a)
        print("Or,", a, "meter(s) and",format(float(b) * 100, '.2f'), "centimeter(s).")
    if conversion_unit_input == "cm" and conversion_unit_output == "ft":
        length = float(input("What is the length, in centimeters, that you wish to convert to feet?"))
        print("Your converted length is", float(format(length / 30.48, '.4f')), "feet.")
        a = int(length / 30.48)
        b = format(length / 30.48 - a)
        print("Or,", a, "Feet(s) and",format(float(b) * 12, '.2f'), "inch(es).")

def inches_centimeters():
    if conversion_unit_input == "cm" and conversion_unit_output == "in":
        length = float(input("What is the length, in centimeters, that you wish to convert to inches?"))
        print("Your converted length is", float(format(length / 2.54, '.4f')), "inches.")
        a = int(length / 30.48)
        b = format(length / 30.48 - a)
        print("Or,", a, "feet and",format(float(b) * 12, '.2f'), "inch(es).")
    if conversion_unit_input == "in" and conversion_unit_output == "cm":
        length = float(input("What is the length, in inches, that you wish to convert to centimeters?"))
        print("Your converted length is", float(format(length * 2.54, '.4f')), "centimeters.")
        a = int(length * 2.54 / 100)
        b = format(length * 2.54 / 100 - a)
        print("Or,", a, "meter(s) and",format(float(b) * 100, '.2f'), "centimeter(s).")

def inches_meters():
    if conversion_unit_input == "m" and conversion_unit_output == "in":
        length = float(input("What is the length, in meters, that you wish to convert to inches?"))
        print("Your converted length is", float(format(length / .0254, '.4f')), "inches.")
        a = int(length / .3048)
        b = format(length / .3048 - a)
        print("Or,", a, "feet and",format(float(b) * 12, '.2f'), "inch(es).")
    if conversion_unit_input == "in" and conversion_unit_output == "m":
        length = float(input("What is the length, in inches, that you wish to convert to meters?"))
        print("Your converted length is", float(format(length * .0254, '.4f')), "meters.")
        a = int(length * .0254)
        b = format(length * .0254 - a)
        print("Or,", a, "meter(s) and",format(float(b) * 100, '.2f'), "centimeter(s).")

def meters_centimeters():
    if conversion_unit_input == "m" and conversion_unit_output == "cm":
        length = float(input("What is the length, in meters, that you wish to convert to centimeters?"))
        print("Your converted length is", float(format(length * 100, '.4f')), "centimeters.")
        a = int(length)
        b = format(length - a)
        print("Or,", a, "meter(s) and",format(float(b) * 100, '.2f'), "centimeter(s).")
    if conversion_unit_input == "cm" and conversion_unit_output == "m":
        length = float(input("What is the length, in centimeters, that you wish to convert to meters?"))
        print("Your converted length is", float(format(length / 100, '.4f')), "meters.")
        a = int(length / 100)
        b = format(length / 100 - a, '.4f')
        print("Or,", a, "meter(s) and", format(float(b) * 100, '.2f'), "centimeter(s).")
#
#
#End definition of various conversion functions
def conversion_selector():
    if conversion_unit_input == conversion_unit_output:
        print("You can't convert to the same unit!")
    if conversion_unit_input == "ft" or "m" and conversion_unit_output == "m" or "ft":
        feet_meters()
    if conversion_unit_input == "ft" or "in" and conversion_unit_output == "in" or "ft":
        feet_inches()
    if conversion_unit_input == "ft" or "cm" and conversion_unit_output == "cm" or "ft":
        feet_centimeters()
    if conversion_unit_input == "m" or "in" and conversion_unit_output == "in" or "m":
        inches_meters()
    if conversion_unit_input == "in" or "cm" and conversion_unit_output == "cm" or "in":
        inches_centimeters()
    if conversion_unit_input == "m" or "cm" and conversion_unit_output == "m" or "cm":
        meters_centimeters()

conversion_selector()

print("---------------------------")
print("Please be aware that all values are rounded.")
print("---------------------------")
print("Thank you", name, "for using Andrew's Metric-Customary unit converter!")
