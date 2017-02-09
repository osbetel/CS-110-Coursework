# Nguyen, Andrew
# July 31st, 2015
# RPS Agent Assignment

import datetime
import os
import time
import random
userGameScore = 0
machineGameScore = 0
agentBias = 0
stats = {"Sessions":0, "Session Wins":0, "Session Losses":0,
                    "Games":0, "Game Wins":0, "Game Losses":0,
                    "Game Ties":0, "R":0, "P":0, "S":0}
userChoice = "n/a"
machineChoice = "n/a"
machineName = "Agent Rips"
userName = input("Hello, welcome to the Rock-Paper-Scissors simulator!\nMy name is Agent Rips; what is your name?")
print("-------------------------------------------------------")


def menu():

    if os.path.exists(userName+".txt") == True:

        try:
            with open(userName+".txt", "r") as file:
                #firstLine = print(file.readline())
                lineList = file.readlines()
                file.close()
                timeLine = str(lineList[-2])
                timeStamp = str(timeLine[:-8])

                gameLine = str(lineList[-4])
                gameRecord = str(gameLine[-18:-1])

                sessionLine = str(lineList[-3])
                sessionRecord = str(sessionLine[-18:-1])

                global stats
                statString = str(lineList[1])          # Read dictionary as string
                stats = dict(eval(statString))         # Evaluate that string back into a dictionary form; redundant?
                #print(lastLine)
                #print(timeStamp)

            print("Welcome back", userName+"!"
                  "\nThe last time you played was on", timeStamp+"!")
            print("Last time you played, the Game Score was", gameRecord)
            print("And the overall Session Score was", sessionRecord)
            print("In total, you have lost", stats["Game Losses"], "times and won", stats["Game Wins"], "times.")
            print("-------------------------------------------------------")

            R = stats["R"]
            P = stats["P"]
            S = stats["S"]
            if R > (P and S):
                print("I've noticed you tend to choose Rock more often...")
            elif P > (R and S):
                print("I've noticed you tend to choose Paper more often...")
            elif S > (R and P):
                print("I've noticed you tend to choose Scissors more often...")

            prevSessionUser = int(gameRecord[5])
            prevSessionMachine = int(gameRecord[-2])
            #print(prevSessionUser)
            #print(prevSessionMachine)

            # Machine responses based on previous session scores (user wins)
            if (prevSessionUser - prevSessionMachine) == 1:
                print("We had a pretty close game last time. But in the end you still won out.")
            elif (prevSessionUser - prevSessionMachine) == 2:
                print("You beat me quite well last time, but I'll get you this time for sure!")
            elif (prevSessionUser - prevSessionMachine) == 3:
                print("You are so good at this; I'm dreading this upcoming game with you...")
            elif (prevSessionUser - prevSessionMachine) >= 4:
                print("Do I even dare to face you in a game of RPS? I'll just lose again...")

            # Machine comments based on previous session scores (machine wins)
            elif (prevSessionMachine - prevSessionUser) == 1:
                print("By the way, nice try last time. But it seems I'm still superior to you!")
            elif (prevSessionMachine - prevSessionUser) == 2:
                print("Last time we played, I still beat you by a couple games. You're not very good...")
            elif (prevSessionMachine - prevSessionUser) == 3:
                print("Oh? Are you back to receive another beating?")
            elif (prevSessionMachine - prevSessionUser) >= 4:
                print("I don't see why you're here though. You're so bad it's not worth it to play you.")

            print("-------------------------------------------------------")
        except IndexError:
            print("An error occurred with the log file. It will be erased and a new one will be created.")
            print("-------------------------------------------------------")
            os.remove(userName+".txt")
            menu()

        while True:
            try:
                statChoice = str(input("Would you like to see a list of your current Game Stats? Y/N?"))
                if statChoice == "Y":
                    print("-------------------------------------------------------")
                    print("-------------------------------------------------------")
                    print("Sessions Played:", stats["Sessions"])
                    print("Sessions Won:", stats["Session Wins"])
                    print("Sessions Lost:", stats["Session Losses"])
                    print("Games Played:", stats["Games"])
                    print("Games Won:", stats["Game Wins"])
                    print("Games Lost:", stats["Game Losses"])
                    print("Rock played", stats["R"], "times.")
                    print("Paper played", stats["P"], "times.")
                    print("Scissors played", stats["S"], "times.")
                    print("-------------------------------------------------------")
                    print("-------------------------------------------------------")
                    break

                elif statChoice == "N":
                    break
                elif statChoice != "Y" or statChoice != "Y":
                    print("Please type an acceptable form of input. Capital Y or N only please.")
                    print("-------------------------------------------------------")
            except Exception as err:
                print(err)

        playChoice = str(input("Would you like to play a game of RPS today? Y/N?"))
        print("-------------------------------------------------------")
        if playChoice == "Y":
            with open(userName+".txt", "a") as file:
                file.write("\nSESSION START\n"+str(datetime.datetime.now()))
                file.write("\n-------------------------------------------------------\n")
            pass
        elif playChoice == "N":
            exit()
        elif playChoice != "Y" or playChoice != "N":
            print("Please enter a valid form of input."
                  "\n-------------------------------------------------------")
            menu()

    else:
        print("It seems you are a new player! A log file will be created for you to keep track of all your"
              "\ngame statistics! Enjoy the game! \n-------------------------------------------------------")
        file = open(userName+".txt", "w")
        file.write(userName+"'s RPS Stat Log File")
        statDict = {"Sessions":0, "Session Wins":0, "Session Losses":0,
                    "Games":0, "Game Wins":0, "Game Losses":0,
                    "Game Ties":0, "R":0, "P":0, "S":0}
        file.write("\n"+str(statDict))
        file.write("\n-------------------------------------------------------\n")
        file.write("\nSESSION START\n"+str(datetime.datetime.now()))
        file.write("\n-------------------------------------------------------\n")
        file.close()

    while True:
        try:
            menu_choice = int(input("Please select an option by inputting the corresponding number:"
                        "\n1)Play a standard 5-round game of RPS!"
                        "\n2)Play a game of RPS with an AI Bias towards one choice."
                        "\n-------------------------------------------------------\n"))
            if menu_choice == 1:
                main()
            if menu_choice == 2:        #For the extra credit portion of HW4
                global agentBias
                agentBias = 1
                main()

        except ValueError:
            print("That is an invalid form of input. Please try again.")


def main():

    # define variables local to main() scope.
    roundCount = 0
    userRecord = 0
    machineRecord = 0
    tieRecord = 0
    machineStreak = 0
    userStreak = 0

    # define all major functions here
    def user_choice():
        global stats
        global userChoice
        while True:
            try:
                userChoice = input("What do you choose? Rock (R), Paper (P), or Scissors (S)!?"
                               " Make your choice by entering the capital letter in parentheses after each choice.")
                if userChoice == "R":
                    stats["R"] += 1
                    return userChoice
                elif userChoice == "P":
                    stats["P"] += 1
                    return userChoice
                elif userChoice == "S":
                    stats["S"] += 1
                    return userChoice
                else:
                    print("Please enter only R, P, or S to select your choice."
                          "\n-------------------------------------------------------")
            except ValueError:
                print("Please type a legitimate form of input.")
            except Exception as err:
                print(err)

    def machine_choice():
        global machineChoice
        global stats

        if agentBias == 0:
            x = random.randint(1,3)
            #print("3...")
            #time.sleep(1)
            #print("2...")
            #time.sleep(1)
            #print("1...")
            #time.sleep(1)
            print("...The opponent has made a choice; time to choose yours!")
            print("-------------------------------------------------------")

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
            print("-------------------------------------------------------")

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
        global userChoice
        global machineChoice
        userStat = open(userName+".txt", "a")

        def stat_tracker():

            # Create a list of the user's game states for that PARTICULAR SESSION. Eg: Session 1, 2, etc.
            userDataList = [userName, roundCount, userChoice, machineChoice, round_result, str(datetime.datetime.now())]
            #print(round_result)
            #print(userDataList)
            userStat.write(str(userDataList)+"\n")

        if round_result == "MW":
            machineRecord += 1
            machineStreak += 1
            userStreak = 0
            stats["Game Losses"] += 1
            if machineStreak > 1:
                print("Machine has a winning streak of", machineStreak, "wins!")

        if round_result == "UW":
            userRecord += 1
            userStreak += 1
            machineStreak = 0
            stats["Game Wins"] += 1
            if userStreak > 1:
                print("User has a winning streak of", userStreak, "wins!")

        if round_result == "T":
            tieRecord += 1
            roundCount -= 1
            userStreak = 0
            machineStreak = 0
            stats["Game Ties"] += 1

        print("Machine has won", machineRecord,"time(s) and User has won", userRecord, "time(s)."
            "\nThere have been", tieRecord, "tie(s) so far.\n")

        # Begin AI Responses based on win streaks.
        if machineStreak == 2:
            print("My my, I've won twice in a row? I must be very good at this game!\n")
            userStat.write("My my, I've won twice in a row? I must be very good at this game!\n")
        if machineStreak == 3:
            print("Either I am excellent at predicting your choices, or you simply suck at this game!\n")
            userStat.write("Either I am excellent at predicting your choices, or you simply suck at this game!\n")
        if machineStreak == 4:
            print("This is getting boring; you don't give me a challenge at all. I'm leaving.\n")
            userStat.write("This is getting boring; you don't give me a challenge at all. I'm leaving.\n")

        if userStreak == 2:
            print("I don't usually lose so easily! You probably just have beginner's luck.\n")
            userStat.write("I don't usually lose so easily! You probably just have beginner's luck.\n")
        if userStreak == 3:
            print("You must be cheating somehow because there's no way I am this bad at such a simple game!\n")
            userStat.write("You must be cheating somehow because there's no way I am this bad at such a simple game!\n")
        if userStreak == 4:
            print("That's it! You're definitely a cheater! I'm going to find someone else to play with!\n")
            userStat.write("That's it! You're definitely a cheater! I'm going to find someone else to play with!\n")

        stat_tracker()

    def gameSentinel():

        print("-------------------------------------------------------")
        newgameSentinel = str(input("Would you like to play again? Y/N?"
                                        "\nInput a capital Y or N to select."))
        print("-------------------------------------------------------")

        global machineGameScore
        global userGameScore
        global stats

        if newgameSentinel == "Y":
            if userRecord > machineRecord:
                userGameScore += 1
            if machineRecord > userRecord:
                machineGameScore += 1


            print("The current Game record is User:", str(userRecord), "and Machine:", str(machineRecord)+".")
            print("The current Session record is User:", str(userGameScore), "and Machine:", str(machineGameScore)+".")
            with open(userName+".txt", "a") as file:
                file.write("GAME END. GAME SCORE: USER:"+str(userRecord)+" MACHINE:"+str(machineRecord)+".\n")
                file.write(str(datetime.datetime.now()))
                file.write("\n-------------------------------------------------------\n")
            main()

        elif newgameSentinel == "N":
            stats["Sessions"] += 1
            if userRecord > machineRecord:
                userGameScore += 1
            if machineRecord > userRecord:
                machineGameScore += 1
            if userGameScore > machineGameScore:
                stats["Session Wins"] += 1
            if machineGameScore > userGameScore:
                stats["Session Losses"] += 1

            print("The final session record is User:", userGameScore, "and Machine:", str(machineGameScore)+".")
            with open(userName+".txt", "a") as file:
                file.write("GAME END. GAME SCORE: USER:"+str(userRecord)+" MACHINE:"+str(machineRecord)+".\n")
                file.write("SESSION END. SESSION SCORE: USER:"+str(userGameScore)+" MACHINE:"+str(machineGameScore)+".\n")
                file.write(str(datetime.datetime.now()))
                file.write("\n-------------------------------------------------------")
                file.close()

            with open(userName+".txt", "r+") as file:
                dictLine = file.readlines()
                dictLine[1] = str(stats)+"\n"
                file.close()
            with open(userName+".txt", "w") as file:
                file.writelines(dictLine)




        elif newgameSentinel != "Y" or newgameSentinel != "N":
            print("""Only enter either "Y" or "N" please.""")
            gameSentinel()

# END DEFINITION OF FUNCTIONS


    # Begin code local to the scope of main().
    # loops infinitely; when roundCount == 5, loop breaks. Ties do not modify the roundCount. Only wins and losses do.
    while True:
        global stats
        # roundCount variable serves to regulate how many rounds of gameplay occur, *accounting for tie games*.
        roundCount += 1
        print("Round", roundCount, "Start!")
        stats["Games"] += 1
        print("-------------------------------------------------------"
              "\n-------------------------------------------------------")

        # Originally "choice_comparison(machine, user)." Other functions used as parameters instead.
        choice_comparison(machine_choice(), user_choice())
        # Begin verification of results and tally scores, streaks, and ties.
        verify()

        if roundCount == 5:
            break
        if machineStreak == 4 or userStreak == 4:
            break

    gameSentinel()

    print("Your current overall RPS stats are as follows:")
    print("-------------------------------------------------------")
    print("Sessions Played:", stats["Sessions"])
    print("Sessions Won:", stats["Session Wins"])
    print("Sessions Lost:", stats["Session Losses"])
    print("Games Played:", stats["Games"])
    print("Games Won:", stats["Game Wins"])
    print("Games Lost:", stats["Game Losses"])
    print("Rock played", stats["R"], "times.")
    print("Paper played", stats["P"], "times.")
    print("Scissors played", stats["S"], "times.")
    print("-------------------------------------------------------")

    exit()

menu()