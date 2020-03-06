# CISC689 HW1
Author: Carlton Brady (solo)


### Project Structure

The "sentences" directory contains the code and files for using the python nltk sentence splitter
and analysing the results (HW1 Q1 and Q2).
Files:
sentence_splitter_input.txt - the provided text to run the splitter on  
sentence_splitting.py - the script that runs the nltk sentence splitter on the text  
sentences.txt - the resulting sentences output by the nltk sentence splitter  

The "trigram" directory contains the code and files for creating the trigram character model and
showing next character predictions for a word or list of words.  
Files:  
training_set.txt - the training set provided for the assignment  
trigram_character_model.py - the script that constructs the trigram model with stupid backoff  


The "states" directory contains the code and files for extracting gross state product and nicknames from the
state wikipedia pages.  
Files:  
state_parsing.py - the script that parses the wikipedia source 
files and outputs all of the state information