def analyze_file(filename):
    #runs function open and stores result in f, open takes the filename and what to do with it, which is r in this case for reading. by using with, if things fail the program cleans up on its own
    with open(filename, "r") as f:
    #text is a string that was made from the using the read function on f, which reads a file to the end unless you give an int of how many characters to read
        text = f.read()
        #using f and the name property to print the file name
        print("File name:", f.name)
        # text.splitlines splits the text by new line characters, which get put into a list. Getting the length of the list tells us how many lines there are.
        print("Lines:" , len(text.splitlines()))
        # text.split splits the text by each white space, putting each word into the list and by using the len() function we can find how many words there are.
        print("Words:", len(text.split()))
        #len tells us how long the string is, which in this case is how many characters there are.
        print("Characters:", len(text))

if __name__ == "__main__":
    try:
        analyze_file("sample.txt")
    except:
        print("this file doesn't exist, did you type it right?")

    