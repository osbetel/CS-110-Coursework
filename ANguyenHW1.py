#Written by Andrew Nguyen
#Monday, July 6, 2015
#This is a program intended to calculate the final cost
#of a meal, factoring in different tax percentages and tax cost.
#Note: Tip is not calculated after tax. Both tax and tip are calculated separately
#from the base cost, and then added to the total.
def tax_and_tip():
    print("Andrew's Tax, Tip, and Final Cost Calculator")
    print("--------------------------------------------")

    base_cost = float(input("What is the base cost of your meal in dollars and cents?"
                      "\nOnly enter the number with no dollar sign."))
    print("--------------------------------------------")

    print("Your base cost is $"+str(format(base_cost, '.2f')))
    print("At a rate of 7%, the tax on your meal will be $"+str(format(base_cost * .07, '.2f')))
    print("--------------------------------------------")

    tip15 = base_cost * 1.15
    tip18 = base_cost * 1.18
    tip20 = base_cost * 1.20

    print("Your total cost with tax and a 15% tip is: $"+str(format(tip15 + base_cost * .07, '.2f')))
    print("Your total cost with tax and a 18% tip is: $"+str(format(tip18 + base_cost * .07, '.2f')))
    print("Your total cost with tax and a 20% tip is: $"+str(format(tip20 + base_cost * .07, '.2f')))
    print("--------------------------------------------")


tax_and_tip()

#I have tested the program several times and verified the outputted values with a calculator.
#These values include $100 with $7 tac, and a total of $122, $125, $127, for each of the respective tip rates.
#Another tested value is $200 with $14 of tax, and totals of $244, $250, $254.

#It was unnecessary to define the program as a single function, and then call it back at the end, but
#I prefer to do it like that whenever possible.