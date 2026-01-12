import string
import csv
from pathlib import Path

#list of words we don't want
STOPWORDS = {
    "the", "a", "an", "and" "or", "but", "to", "of", "in", "is", "are", "was", "were", "be", "been", "by", "from", "you", "i", "what", "it"
}

#return each w if for each w in words, w is not in the stop words
def filterWords(words, stop_words=STOPWORDS):
    return [w for w in words if w not in stop_words and len(w) > 2]

def saveToCSV(results, CSVPath, sourcefile = None):
    #opens a CSV file to write to
    with open(CSVPath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if(sourcefile is not None):
            #if the source file is passed in we can put it at the top of the file then put in a new line
            writer.writerow(["Source file:", sourcefile])
            writer.writerow([])

        #this is the hearding or first row
        writer.writerow(["word", "count"])
        #this is going to grab the results which are comma separated and write them to the file
        writer.writerows(results)


def countWords(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    return counts

def normalizeText(text):

    #this says to replace the first string, x, with the second, y, and delete the characters in the third string which is all punctuation.
    translator = str.maketrans("", "", string.punctuation)
    #actually using the translation table
    nText = text.translate(translator)
    return nText

def analyze_file(filepath, top_n = 5):
    #we pass in the whole path which makes it hard to do this wrong.
    path = Path(filepath)
    #opens and closes the file found and reads it, makes lower case, and stores in text.
    text = path.read_text().lower()    
    #using f and the name property to print the file name
    print("File name:", path.name)
    text = normalizeText(text)
    #for every word, which is the text split up, look for it in the dictionary, set its count to plus 1 the previous amount which is 0 if not found.
    counts = countWords(words = filterWords(text.split()))

#lambda is basically a one word function here that tells sorted to sort using the second value of tuple x as the key for sorting, which in this case is the count number
    sorted_words = sorted(counts.items(), key= lambda x: x[1], reverse= True)
    #returns the sorted words up to the one indexed top_n
    return sorted_words[:top_n]

if __name__ == "__main__":


    try:
       inputPath = Path(r"C:\Users\Ariel\OneDrive\Desktop\ReEntry\fileReading\sample.txt")

       outPath = inputPath.parent / "output.txt"
       outCSV = inputPath.parent / "output.csv"
       #passing in the absolute file path, saying r"" tells the computer that it can handle single \ instead of double. the second value is the number of words we want from our list.
       results = analyze_file(inputPath,top_n=5)
       #function takes our results and file path of csv file and writes to it
       saveToCSV(results, outCSV, inputPath)
       print("wrote to :", outCSV)
       #open output txt and write to it using utf8 encoding. If it doesn't already exist, it makes the file for you.
       with open(outPath, "w", encoding="utf-8") as f:
        f.write(f"File name: {inputPath.name}\n\n")
        #for each touple, write to the file using the following format: word : count new line
        for word, count in results:
            f.write(f"{word:} : {count} \n")

        
    #case the reading file was not found.
    except FileNotFoundError:
        print("this file doesn't exist, did you type it right?")

    
    