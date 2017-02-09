# Nguyen, Andrew
# July 31st, 2015
# RPS Agent Assignment


import time
import random
userGameScore = 0
machineGameScore = 0
agentBias = 0
machineName = "Agent Rips"
userName = input("Hello, welcome to the Rock-Paper-Scissors simulator!\nMy name is Agent Rips; what is your name?")

def menu():
    menu_choice = int(input("Please select an option by inputting the corresponding number:"
                        "\n1)Play a standard 5-round game of RPS!"
                        "\n2)Play a game of RPS with an AI Bias towards one choice."
                        "\n-------------------------------------------------------\n"))

    if menu_choice == 1:
        main()
    if menu_choice == 2:        #For the extra credit portion on requesting agent bias.
        global agentBias
        agentBias = 1
        main()

def main():

    #define variables local to main() scope.
    roundCount = 0
    userRecord = 0
    machineRecord = 0
    tieRecord = 0
    machineStreak = 0
    userStreak = 0

    #define all major functions here
    def user_choice():
        while True:
            try:
                userChoice = input("What do you choose? Rock (R), Paper (P), or Scissors (S)!?"
                               " Make your choice by entering the capital letter in parentheses after each choice.")
                if userChoice == "R":
                    return userChoice
                elif userChoice == "P":
                    return userChoice
                elif userChoice == "S":
                    return userChoice
                else:
                    print("Please enter only R, P, or S to select your choice."
                          "\n----------")
            except ValueError:
                print("Please type a legitimate form of input.")
            except Exception as err:
                print(err)

    def machine_choice():

        if agentBias == 0:
            x = random.randint(1,3)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            print("...The opponent has made a choice; time to choose yours!")
            print("------------------------------")

            if x == 1:
                machineChoice = "R"
                return machineChoice
            elif x == 2:
                machineChoice = "P"
                return machineChoice
            elif x == 3:
                machineChoice = "S"
                return machineChoice

        #This second decision structure is only if the user wants to play with an agent bias in the menu() function.
        if agentBias == 1:
            x = random.randint(1,4)
            y = random.randint(1,3)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            print("...The opponent has made a choice; time to choose yours!")
            print("------------------------------")

            if y == 1:
                if x == 1:
                    machineChoice = "R"
                    return machineChoice
                elif x == 2:
                    machineChoice = "P"
                    return machineChoice
                elif x == 3:
                    machineChoice = "S"
                    return machineChoice
                elif x == 4:
                    machineChoice = "R"
                    return machineChoice
            if y == 2:
                if x == 1:
                    machineChoice = "R"
                    return machineChoice
                elif x == 2:
                    machineChoice = "P"
                    return machineChoice
                elif x == 3:
                    machineChoice = "S"
                    return machineChoice
                elif x == 4:
                    machineChoice = "P"
                    return machineChoice
            if y == 3:
                if x == 1:
                    machineChoice = "R"
                    return machineChoice
                elif x == 2:
                    machineChoice = "P"
                    return machineChoice
                elif x == 3:
                    machineChoice = "S"
                    return machineChoice
                elif x == 4:
                    machineChoice = "S"
                    return machineChoice


    def choice_comparison(machine, user):
        global round_result
        global roundCount
        if machine == "R" and user == "R":
            round_result = "T"
            print("***")
            print("Both parties chose Rock!")
            print("This round is a tie! Rematch!")
            print("***")
        if machine == "P" and user == "P":
            round_result = "T"
            print("***")
            print("Both parties chose Scissors!")
            print("This round is a tie! Rematch!")
            print("***")
        if machine == "S" and user == "S":
            round_result = "T"
            print("***")
            print("Both parties chose Paper!")
            print("This round is a tie! Rematch!")
            print("***")

        if machine == "R" and user == "P":
            round_result = "UW"
            print("**********")
            print(userName, "chose Paper and Agent Rips chose Rock!")
            print(userName, "wins this round!")
            print("**********")
        if machine == "P" and user == "S":
            round_result = "UW"
            print("**********")
            print(userName, "chose Scissors and Agent Rips chose Paper!")
            print(userName, "wins this round!")
            print("**********")
        if machine == "S" and user == "R":
            round_result = "UW"
            print("**********")
            print(userName, "chose Rock and Agent Rips chose Scissors!")
            print(userName, "wins this round!")
            print("**********")

        if machine == "R" and user == "S":
            round_result = "MW"
            print("*************")
            print(userName, "chose Scissors and Agent Rips chose Rock!")
            print("Agent Rips wins this round!")
            print("*************")
        if machine == "P" and user == "R":
            round_result = "MW"
            print("*************")
            print(userName, "chose Rock and Agent Rips chose Paper!")
            print("Agent Rips wins this round!")
            print("*************")
        if machine == "S" and user == "P":
            round_result = "MW"
            print("*************")
            print(userName, "chose Paper and Agent Rips chose Scissors!")
            print("Agent Rips wins this round!")
            print("*************")

        return round_result

    def verify():
        nonlocal roundCount
        nonlocal userRecord
        nonlocal machineRecord
        nonlocal tieRecord
        nonlocal machineStreak
        nonlocal userStreak

        if round_result == "MW":
            machineRecord += 1
            machineStreak += 1
            userStreak = 0
            if machineStreak > 1:
                print("Machine has a winning streak of", machineStreak, "wins!")

        if round_result == "UW":
            userRecord += 1
            userStreak += 1
            machineStreak = 0
            if userStreak > 1:
                print("User has a winning streak of", userStreak, "wins!")

        if round_result == "T":
            tieRecord += 1
            roundCount -= 1
            userStreak = 0
            machineStreak = 0

        print("Machine has won", machineRecord,"time(s) and User has won", userRecord, "time(s)."
            "\nThere have been", tieRecord, "tie(s) so far.\n")

        #Begin AI Responses based on win streaks.
        if machineStreak == 2:
            print("My my, I've won twice in a row? I must be very good at this game!\n")
        if machineStreak == 3:
            print("Either I am excellent at predicting your choices, or you simply suck at this game!\n")
        if machineStreak == 4:
            print("This is getting boring; you don't give me a challenge at all. I'm leaving.\n")

        if userStreak == 2:
            print("I don't usually lose so easily! You probably just have beginner's luck.\n")
        if userStreak == 3:
            print("You must be cheating somehow because there's no way I am this bad at such a simple game!\n")
        if userStreak == 4:
            print("That's it! You're definitely a cheater! I'm going to find someone else to play with!\n")

    #END DEFINITION OF FUNCTIONS


    #Begin code local to the scope of main().
    #loops infinitely; when roundCount == 5, loop breaks. Ties do not modify the roundCount. Only wins and losses do.
    while True:
        #roundCount variable serves to regulate how many rounds of gameplay occur, *accounting for tie games*.
        roundCount += 1
        print("Round", roundCount, "Start!")
        print("------------------------------"
              "\n------------------------------")

        #Originally "choice_comparison(machine, user)." Other functions used as parameters instead.
        choice_comparison(machine_choice(), user_choice())
        #Begin verification of results and tally scores, streaks, and ties.
        verify()

        if roundCount == 5:
            break
        if machineStreak == 4 or userStreak == 4:
            break


    print("-----------------------------")
    newgameSentinel = input("Would you like to play again? Y/N?"
                                    "\nInput a capital Y or N to select.")
    print("-----------------------------")
    if newgameSentinel == "Y":
        global machineGameScore
        global userGameScore
        if userRecord > machineRecord:
            userGameScore += 1
        if machineRecord > userRecord:
            machineGameScore += 1
        print("The overall game record is User:", userGameScore, "and Machine:", str(machineGameScore)+".")
        main()
    else:
        print("The final game record is User:", userGameScore, "and Machine:", str(machineGameScore)+".")



menu()