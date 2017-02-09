# INCOMPLETE
# I was not able to finish this one.

def main():

    # Query User for name of file created in Ex. 2 (request that no file extension be given)
    ex2_file_output = str(input("What is the name of the output file created in exercise 2?"
                            "\nPlease omit the file extension name."))+".txt"

    # Open for reading the requested file with proper name & extension
    input_file = open(ex2_file_output, 'r')
    print(input_file.read())
    # Open for append, the requested file with proper name & extension
    # Read lines from the file, counting number of words in each line
    num_words = 0
    num_lines = 0
    line = input_file.readline()

    while line != "":
        for num in line:
            words = line.split( )
            num_lines += 1
            num_words += words
            line = input_file.readline()

    print(num_words)
    print(num_lines)


    # Append to file for each line: "Line #__ contains __words."


    # Append to file: "Total number of words: __ "


    # Append your name to file.


    # Close the files.



    # ...

# Call the main function.
main()
