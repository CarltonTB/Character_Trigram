from nltk.tokenize import word_tokenize, sent_tokenize

fobj = open("sentences/sentence_splitter_input.txt", "r")
sentences = sent_tokenize(fobj.read())
fobj.close()

fobj_write = open("sentences/sentences.txt", "w")
for s in sentences:
    print(s)
    fobj_write.write(s + "\n\n")