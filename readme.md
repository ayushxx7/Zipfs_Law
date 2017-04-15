Zipf's law states that given some corpus of natural language utterances, the frequency of any word is inversely proportional to its rank in the frequency table.

I was made aware of this law because of Vsauce <https://www.youtube.com/watch?v=fCn8zs912OE> and was quite frankly baffled and mindf*ked beyond thought. 

Once I was certain it was true for so many things, I decided to have my own version for verifying it. Enter South Park. I realised that South Park was probably really good source to do data analysis on and so I did. I used subs for the series from Season one to eighteen as my raw input.

SRT files are read, punctuations are removed and so are the [br] breaks in the subs (specific to my download I guess)

A csv file is made from the data using Counter function.

This csv file is used to plot a normal graph and a log graph of the frequency table from the csv.

Happy to say, the law is valid :) and I was able to verify it along with a learning a lot about regex, matplotlib, csv reader and the ease of Python as a whole :)
