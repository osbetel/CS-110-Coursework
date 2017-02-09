def main():
    input_file = open('stones.txt', 'r')
    output_file = open(input("What would you like to name your output file?"), 'w')
    print("-----------------------------")

    line = input_file.readline()

    while line != "":

            if "stone" in line:
                stone_hit = line
                print(line)
                output_file.write(stone_hit)

            if "Stones" in line:
                Stones_hit = line
                print(line)
                output_file.write(Stones_hit)

            line = input_file.readline()

    input_file.close()
    output_file.close()

main()
