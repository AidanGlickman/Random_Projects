# What is the Longest Word You Can Make With a 7-Segment Display?
#### Probably a common interview question, I saw it in [a Tom Scott video](https://www.youtube.com/watch?v=zp4BMR88260&t=340s).

## What It Does
* Finds the longest word in a word list that does not have letters specified in a regular expression.
* Prints Them out in the form of a 7 segment display

## Things Used
* Regex to make sure that only 7-segment printable letters are printed
* [This wordlist](https://github.com/dwyl/english-words)
* Custom segmap.txt file to map letters to 7-Segment display instructions