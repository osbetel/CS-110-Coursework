def main():

    contents = open("stones.txt", "r").read()
    print(contents)

# This portion is the function that searches the "source" (content variable) for a desired string.
    def search_strings(source, word):
        index = 0
        if word in source:
            string = word[0]
            for search in source:
                if search == string:
                    if source[index:index+len(word)] == word:
                        return index
                index += 1
        return -1

    print("""Your string "computer" starts at character #"""+str(search_strings(contents, "computer"))+".")
    print("""Your string "computers" starts at character #"""+str(search_strings(contents, "computers"))+".")
    print("""Your string thinking" starts at character #"""+str(search_strings(contents, "thinking"))+".")
    print("""Your string get a life" starts at character #"""+str(search_strings(contents, "get a life"))+".")

main()

