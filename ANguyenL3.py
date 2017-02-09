#Written by Andrew Nguyen; July 15, 2015
#This program is written in order to model the growth of population over time.
#This is Lab # 3 for Professor Zimmerman's Summer 2015 CSC 110 class.


#Begin definition of variables...
def var_def():
    global start_pop
    global num_years
    global interval
    global growth_rate
    global x
    while True:
        try:
            start_pop = int(input("What is your starting population?"))
            print("-------------------------------------------------")
            if start_pop <= 0 :         #To handle negative inputs.
                print("Negative values or values of zero are not accepted; please enter another number.")
                print("-------------------------------------------------")
            else:
                break
        except ValueError:      #To handle the error when someone inputs a string instead of an integer.
            print("Please enter an integer value. Decimals and words are not accepted.")
            print("-------------------------------------------------")

    while True:
        try:
            num_years = int(input("What is the total number of years you would like to calculate growth from?"))
            print("-------------------------------------------------")
            if num_years <= 0 :
                print("Negative values or values of zero are not accepted; please enter another number.")
                print("-------------------------------------------------")
            else:
                break
        except ValueError:
            print("Please enter an integer value. Decimals and words are not accepted.")
            print("-------------------------------------------------")

    while True:
        try:
            interval = int(input("""What is the interval of time you'd like to display? If you do not know, enter "1."
Eg: an interval of "2" would give you the final population results of years 0, 2, 4, 6, etc."""))
            print("-------------------------------------------------")
            if interval <= 0:
                print("Negative values or values of zero are not accepted; please enter another number.")
                print("-------------------------------------------------")
            else:
                break
        except ValueError:
            print("Please enter an integer value. Decimals and words are not accepted.")
            print("-------------------------------------------------")

    growth_rate = float(input("By what percentage does your population grow every year?")) / 100
    print("-------------------------------------------------")

    x = 0       #I used x simply to denote the year in the population growth equation,
                #y = initial * (rate)^x, where x is the # of years elapsed

#Function to calculate data.
def calculate_pop():
    global next_pop
    global x
    next_pop = start_pop * (1 + growth_rate) ** x       #The standard pop growth formula.
    print("-------------------------------------------------")
    if x == 0:
        print("Your base population is", str(round(start_pop)) + ".")
        #To print the base population at the beginning, and only print it ONCE in the loop.
    if interval > 1 and x != 0:
        print("End of year",x, '\t\t', round(next_pop), '\t\t', format((next_pop / num_years), '.2f'))
        #This portion handles the output if intervals are greater than 1 year.
    else:
        print("End of year",x, '\t\t', round(next_pop), '\t\t', format((next_pop / num_years), '.2f'))
        #Handles output for intervals of 1 year.
    while x != num_years:       #Repetition structure to loop until x (years elapsed) equals num_years (years to be calculated).
        if x == num_years:
            break
        if x > num_years:
            break
        else:
            x += interval
            calculate_pop()

def main():
    var_def()
    print("The total number of years passed is", str(num_years) + ".")
    print("Calculations are displayed in intervals of", str(interval) + ".")
    print("Your annual growth rate is", str(format(growth_rate*100, '.2f')) + "%.")
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    print("Year\t\t\t\tPop.\t\t\tAvg. Change")
    calculate_pop()
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    if next_pop == start_pop:
        print("There was no average change in population.")
main()