# fileAnalyzer
Simple text file analyzer in python.

What it does

The file analyzer reads from a sample.txt file, which currently contains part of the Bee Movie, normalizes the text by making it lower case and stripping punctuation, splitting it into a list of words, and then storing the count of each word in a dictionary, which is then used to output into an output CSV and output text file.

How to run it
1. update sample.txt with whatever file you want to read.
2. update the stop words to remove any particular words you'd like to ignore.
3. run python analyzer.py sample.txt --top 20 --out output.csv --outtxt output.txt in your terminal. (Could also run python analyzer.py sample.txt and everything will be default.)
the arguments can be customized, first you can change the number of words you want to see, the csv file to output to, the text output file.

Example output

Terminal will print the name of the file you read in this case "File name: sample.txt"
Inside the output.txt file:

File name: sample.txt

that : 20 

and : 18

out : 14 

for : 12 

youre : 12 

Inside the output.csv file:

Source file:, Input File path goes here

word,count

that,20

and,18

out,14

for,12

youre,12

Features:
- stopwords
- punctuation stripping
- file reading
- CSV export
- unit tests
