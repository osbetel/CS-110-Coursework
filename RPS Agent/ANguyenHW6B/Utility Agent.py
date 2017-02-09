# Nguyen, Andrew
# August 13, 2015
# RPS Agent Assignment

def stat_upgrader():
    import os

    choice = int(input("Please select an option from the menu."
                   "\n1) Create a stat file from an existing user's log file."
                   "\n2) Erase a user's stat file, log file, and any other related files."
                   "\n3) Exit the program."))

    if choice == 1:

        userName = str(input("Please input the username of the player you'd like to create a stat file for:"))

        if os.path.isfile(userName+".txt") == True:

            file = open(userName+".txt", "r")
            fileLines = file.readlines()
            statLine = str(fileLines[1])
            stats = eval(statLine)
            #print(stats)

            #All code below writes the stats pulled from the log file dictionary into the stat file.
            statFile = open(userName+"Stats.txt", "w")

            statFile.write(userName+"'s Stat Log File\n")
            statFile.write(str(stats))
            statFile.write("\n-----------------------------\n")

            statFile.write("Sessions Played:")
            statFile.write(str(stats["Sessions"]))
            statFile.write("\n")

            statFile.write("Sessions Won:")
            statFile.write(str(stats["Session Wins"]))
            statFile.write("\n")

            statFile.write("Sessions Lost:")
            statFile.write(str(stats["Session Losses"]))
            statFile.write("\n")

            statFile.write("Games Played:")
            statFile.write(str(stats["Games"]))
            statFile.write("\n")

            statFile.write("Games Won:")
            statFile.write(str(stats["Game Wins"]))
            statFile.write("\n")

            statFile.write("Games Lost:")
            statFile.write(str(stats["Game Losses"]))
            statFile.write("\n")

            statFile.write("Rock played ")
            statFile.write(str(stats["R"]))
            statFile.write(" times.")
            statFile.write("\n")

            statFile.write("Paper played ")
            statFile.write(str(stats["P"]))
            statFile.write(" times.")
            statFile.write("\n")

            statFile.write("Scissors played ")
            statFile.write(str(stats["S"]))
            statFile.write(" times.")
            statFile.write("\n")

            statFile.write("-----------------------------\n")
            statFile.write("Session Start Timestamps\n")
            statFile.write("-----------------------------\n")
            with open(userName+".txt", "r") as file:
                for line in file:
                    if "SESSION START" in line:
                        line = file.readline()
                        statFile.write(line[:19]+"\n")
                        #print(line[:19])
        else:
            print("A log file for that username does not exist. Please enter another username.")
            print("--------------------------------------------")
            stat_upgrader()

    elif choice == 2:
        userName = str(input("Please input the username of the player you'd like to erase:"))
        os.remove(userName+".txt")
        os.remove(userName+"Stats.txt")

    elif choice == 3:
        exit()
stat_upgrader()