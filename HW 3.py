#Written by Andrew Nguyen; July 15, 2015
#This program is written in order to model the growth of population over time.
#This is HW and Lab # 3 for Professor Zimmerman's Summer 2015 CSC 110 class.


#Begin definition of variables...
#This is the function that queries for required inputs from the user.
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
            if choice == 3:
                break
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
             growth_rate = float(input("By what percentage does your population change every year?")) / 100
             print("-------------------------------------------------")
             break
        except ValueError:
            print("Please enter a numerical value. Words and symbols are not accepted. Decimal numbers DO work.")
            print("-------------------------------------------------")

    while True:
        try:
            if choice == 2:
                break
            if choice == 3:
                break
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




    print("-------------------------------------------------")

    x = 0       #I used x simply to denote the year in the population growth equation,
                #y = initial * (rate)^x, where x is the # of years elapsed



#Function to calculate data.
#This is the function that does the calculation of the population over the time intervals.
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



#Function to display only the last year of population growth.
def final_pop():
    global next_pop
    global x
    next_pop = start_pop * (1 + growth_rate) ** num_years       #The standard pop growth formula.
    print("-------------------------------------------------")
    print("Your base population is", str(round(start_pop)) + ".")
    print("End of year",num_years, '\t\t', round(next_pop), '\t\t', format((next_pop / num_years), '.2f'))
    print("In comparison, the exact value returned from the population growth equation, rounded to 4 decimal places, is", format(next_pop, '.4f'))


#Function to calculate doubling time of a population.
def doubling_time():
    global next_pop
    global x
    while True:
        next_pop = start_pop * (1 + growth_rate) ** x       #The standard pop growth formula.
        if next_pop >= 2 * start_pop:
            break
        else:
            x += 1
            doubling_time()



#Function to choose which portion of the program to access:
#The standard list of pop growth, the final pop growth, or the doubling time.
def fcn_chooser():
    global choice
    while True:
        try:
            choice = int(input("""What would you like to do?\n1) Generate a list of population growth over time and intervals.
2) Calculate the final population given a total time period and growth rate.\n3) Calculate the amount of time passed before the starting population doubles.
4) Exit the program.\n\nPlease enter the corresponding number of the action you wish to perform."""))
            print("-------------------------------------------------")
            return choice
        except ValueError:
            print("Please enter only a corresponding numerical value: 1, 2, 3, or 4.")
            print("-------------------------------------------------")


def main():
    fcn_chooser()
    if choice == 1:
        var_def()
        print("The total number of years passed is", str(num_years) + ".")
        print("Calculations are displayed in intervals of", str(interval) + ".")
        print("Your annual growth rate is", str(format(growth_rate*100, '.2f')) + "%.")
        print("                                                 ")
        print("                                                 ")
        print("Year\t\t\t\tPop.\t\t\tAvg. Change")
        calculate_pop()
        if next_pop == start_pop:
            print("-------------------------------------------------")
            print("There was no average change in population.")
        print("*************************************************")
        print("*************************************************")
        print("*************************************************")
        main()
    if choice == 2:
        var_def()
        print("The total number of years passed is", str(num_years) + ".")
        print("Your annual growth rate is", str(format(growth_rate*100, '.2f')) + "%.")
        print("                                                 ")
        print("                                                 ")
        print("Year\t\t\t\tPop.\t\t\tAvg. Change")
        final_pop()
        if next_pop == start_pop:
            print("-------------------------------------------------")
            print("There was no average change in population.")
        print("*************************************************")
        print("*************************************************")
        print("*************************************************")
        main()
    if choice == 3:
        var_def()
        doubling_time()
        print("The total time required for the starting population to double is", x, "years.")
        print("Your final population, which may be slightly greater than an exact doubling, is", str(round(next_pop)) + ".")
        print("For comparison, the value after", x, "years returned by the population growth equation is", format(next_pop, '.4f')+".")
        print("*************************************************")
        print("*************************************************")
        print("*************************************************")
        main()
    if choice == 4:
        pass


print("Welcome to Andrew's Population Calculation Tool! You can use this tool to calculate the growth of populations given"
      "\na starting population, rate, time period, and intervals to display. It can also be used to show only the final"
      "\nresult after the time is up, or the amount of time required for the population to double."
      "\n\n-------------------------------------------------\n")
main()

#TEST CASES
    #Calculation of human population starting at 7 billion with a rate of 1.1% annual.
        #result of this test gave a value of "20903239624" or ~20.9 billion people.
    #Error trapping
        #tests were performed mostly when "var_def()" was executed but also performed in the beginning
        #when the "fcn_chooser()" function was being used. All aspects have an error handler in place to catch any errors
        #and loop around for proper input.
    #Doubling function tests
        #the doubling function receives input in the form of growth rate and base pop, and from there, it simply loops
        #until the final population value is > or = to double the starting value. Then, it prints the final value as
        #well as the direct output of the equation.

#NOTES
    #Instead of placing a sentinel in each individual function, I tried to imagine how a real-world scenario would need
    #a program like this. I chose to add the sentinel to the main function and have all the sub functions loop back into
    #the main function. My logic being that someone may need data from one portion (eg: the doubling time) in order to
    #calculate something from another (eg: the final pop).

    #I also chose to extend the functionality by allowing the user to choose whether they wanted the full list of
    #calculations displayed, or just the final one. For all intents and purposes, only actions 2), 3), and 4) were required
    #for this program. But I wanted to keep all functionality. So I added the "fcn_chooser()" to adjust for that.

    #In testing, I found that the growth rate operation also functions with negative values for population decrease.