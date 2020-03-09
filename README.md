# CISC689 HW1
Author: Carlton Brady (solo)  
Python version: 3.6.3  
Note: all .py files have been submitted with .txt extensions as requested. They are listed below.  
Note: Answers to the homework questions are in the Carlton_Brady_CISC689_HW1_continued.pdf file.  

### Project Structure
The "sentences" directory contains the code and files for using the python nltk sentence splitter
and analysing the results (HW1 Q1 and Q2).  
Files:  
sentence_splitter_input.txt - the provided text to run the splitter on  
sentences.txt - the resulting sentences output by the nltk sentence splitter  
sentence_splitting.py - the script that runs the nltk sentence splitter on the text  

Running the code:  
run the "sentence_splitting.py" script  

The "trigram" directory contains the code and files for creating the trigram character model and
showing next character predictions for a word or list of words (Q3).  
Files:  
training_set.txt - the training set provided for the assignment  
trigram_character_model.py - the script that constructs the trigram model with stupid backoff and displays predictions  

Running the code:  
run the "trigram_character_model.py" script to see results for default words "hello", "weather", "mystique", and "catcher"  
to see the results for other words, pass them as space separated arguments on the command line like so:  
python trigram_character_model.py the rockets in space  

The "states" directory contains the code and files for extracting gross state product and nicknames from the
state wikipedia pages (Q4).  
Files:  
state_parsing.py - the script that parses the wikipedia source files and outputs all of the state information  
state_info.tsv - file where the gross state product and nicknames for all of the states are written  
arizona.txt - state wikipedia page source file  
california.txt - state wikipedia page source file  
florida.txt - state wikipedia page source file  
idaho.txt - state wikipedia page source file  
maryland.txt - state wikipedia page source file  
nevada.txt - state wikipedia page source file  
new_jersey.txt - state wikipedia page source file  
northo_carolina.txt - state wikipedia page source file  
pennsylvania.txt - state wikipedia page source file  
vermont.txt - state wikipedia page source file  

Running the code:  
run the "state_parsing.py" script and it will print out all of the extracted state info 
and write it to the state_info.tsv file.  