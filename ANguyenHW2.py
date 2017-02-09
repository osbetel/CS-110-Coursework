#Written by Andrew Nguyen; July 10, 2015
#I did attempt the extra credit portion of this lab.

#This program is written as a marketing tool to help determine how much the total cost of software will be
#, granting discounts based on bulk buying.
#2-10 packages = 10%
#11-20 = 20%
#21-30 = 30%
#31 or more = 40%
#FIRST PACKAGE IS ALWAYS $99!

print("Welcome to Over8ted Software's Interactive Pricing Program!")
print("--------------------")

name = input("What is your name?")

print("The pricing schedule is as follows:\n2-10 packages = 10% \n11-20 = 20% \n21-30 = 30% \n31 or more = 40%")
print("--------------------")
input("Press Enter to continue...")
print("The first software package will always be $99; all subsequent packages will be discounted at whatever discount"
      "\nbracket they fall into. Eg: If you buy 22 packages, the first will be $99, 2-10 will be discounted by 10%,"
      "\n11-20 will be discounted 20%, and the last two will be discounted 30%. Prices do not include tax.")
print("--------------------")
packages = int(input("How many software packages would you like to purchase today? Please enter only a number."))

#Begin definition of pricing and student discount functions.
def pricing():
    global subtotal
    global total_cost
    print("--------------------")
    if packages == 1:
        print("Your subtotal is $99.")
        print("You will be taxed at a rate of 9.6% sales tax.")
        print("After tax, your total is $108.50")
        subtotal = float(format(99, '.2f'))
        total_cost = float(format(108.50, '.2f'))
    if 2 <= packages <= 10 and packages != 1:
        print("Your subtotal is $"+str(format(((packages - 1) * 99 * .9)+99.00, '.2f')))
        print("You will be taxed at a rate of 9.6% sales tax.")
        print("After tax, your total cost is $"+str(format((((packages - 1) * 99 * .9)+99.00) * 1.096, '.2f')))
        subtotal = float(format(((packages - 1) * 99 * .9)+99.00, '.2f'))
        total_cost = float(format((((packages - 1) * 99 * .9)+99.00) * 1.096, '.2f'))
        #First 10 packages have a subotal cost of $900.90, factoring in the 10% discount on 2-10
    if 11 <= packages <= 20 and packages != 1:
        print("Your subtotal is $"+str(format(((packages - 10) * 99 * .8)+900.90, '.2f')))
        print("You will be taxed at a rate of 9.6% sales tax.")
        print("After tax, your total cost is $"+str(format((((packages - 10) * 99 * .8)+900.90) * 1.096, '.2f')))
        subtotal = float(format(((packages - 10) * 99 * .8)+900.90, '.2f'))
        total_cost = float(format((((packages - 10) * 99 * .8)+900.90) * 1.096, '.2f'))
        #subotal cost of first 20 packages is $1692.90
    if 21 <= packages <= 30 and packages != 1:
        print("Your subtotal is $"+str(format(((packages - 20) * 99 * .7)+1692.90, '.2f')))
        print("You will be taxed at a rate of 9.6% sales tax.")
        print("After tax, your total cost is $"+str(format((((packages - 20) * 99 * .7)+1692.90) * 1.096, '.2f')))
        subtotal = float(format(((packages - 20) * 99 * .7)+1692.90, '.2f'))
        total_cost = float(format((((packages - 20) * 99 * .7)+1692.90) * 1.096, '.2f'))
        #subotal cost of first 30 packages is $2385.90
    if packages >= 31 and packages != 1:
        print("Your subtotal is $"+str(format(((packages - 30) * 99 * .6)+2385.90, '.2f')))
        print("You will be taxed at a rate of 9.6% sales tax.")
        print("After tax, your total cost is $"+str(format((((packages - 30) * 99 * .6)+2385.90) * 1.096, '.2f')))
        subtotal = float((format(((packages - 30) * 99 * .6)+2385.90, '.2f')))
        total_cost = float((format((((packages - 30) * 99 * .6)+2385.90) * 1.096, '.2f')))
        #Includes cost of all prior packages + all subsequent packages ordered.

def student_discount():
    discount = input("""Are you a student of North Seattle College or an affiliated educational institution of NSC?
    \nPlease enter "y" for yes, or "n" for no.""")
    if name == "NSC":
        discount = "y"
    if name == "North Seattle College":
        discount = "y"
    if discount == "y":
        print("As a student or related institution of NSC, you will receive a discount of 5% off your total purchase! (Tax not included)")
        print("Your final bill, after your eligible discounts, is $"+str(format(subtotal * .95 * 1.096,'.2f')))
    else:
        print("Your final bill will be $"+str(total_cost))

#Begin callback of functions.
pricing()
print("--------------------")
student_discount()
print("--------------------")
print("Thank you,", name, ",for your purchase of", packages, "software packages!")
print("--------------------")

#Test 1: I tested the purchase of 23 packages under the name Andrew, with the student discount included.
    #from manual calculations, I figured the final sum to be $1979.11 which is exactly what the program returned.
    #Calculations were done using the pricing table for bulk buying, and then factoring in the 5% discount to the SUBTOTAL
    #finally, tax was added in to achieve $1979.11.

#Test 2: I tested the purchase of 14 packages under the name NSC, while responding "n" to the question of whether the user
    #was a student at NSC or affiliated institution. The calculation was the same process as before, but
    #this time, even with the "n" response, the discount was still take, and the final total was $1267.87, which is what I got as well.

#Test 3: This final test was simply a plain person buying 45 packages with no educational discount. Just a standard subtotal * tax
    #operation. The final total came back as $3591.48, which is also what I got from manual calculation
    #This concludes my testing of this program.

#Final notes: The input for # of packages to purchase only accepts whole numbers. And even then, only positive numbers.
    #if I were to extend this program, it may include an option for returning products back (in which case I would use the
    #negative numbers). It also does not accept floating point numbers (which makes no sense anyway as you can't purchase
    #a fraction of a product).