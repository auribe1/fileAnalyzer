# fileAnalyzer

A simple Python text file analyzer that reads a `.txt` file, normalizes the text, counts word frequency, and exports results to `output.txt` and `output.csv`.

## What it does
- Reads an input text file
- Normalizes text (lowercase + strips punctuation)
- Splits into words
- Filters stopwords
- Counts word frequency
- Writes:
  - `output.txt` (human-readable)
  - `output.csv` (spreadsheet-friendly)
- Includes unit tests for core helper functions

## How to run
1. Put the text you want to analyze into `sample.txt` (or point to another file).
2. Update `inputPath` in `analyzer.py` to the path of your input file (planned improvement: CLI args).
3. (Optional) Update `STOP_WORDS` to filter additional words.
4. Run:

```bash
python analyzer.py


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

Source file:,C:\Users\Ariel\OneDrive\Desktop\ReEntry\fileReading\sample.txt

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
