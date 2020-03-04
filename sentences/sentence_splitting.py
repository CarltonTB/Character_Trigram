from nltk.tokenize import word_tokenize, sent_tokenize
from os import path

if path.exists("sentences/sentence_splitter_input.txt"):
    fobj = open("sentences/sentence_splitter_input.txt", "r")
else:
    fobj = open("sentence_splitter_input.txt", "r")

sentences = sent_tokenize(fobj.read())
fobj.close()

if path.exists("sentences/sentences.txt"):
    fobj_write = open("sentences/sentences.txt", "w")
else:
    fobj_write = open("sentences.txt", "w")

for s in sentences:
    print(s)
    fobj_write.write(s + "\n\n")

fobj_write.close()