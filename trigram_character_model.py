# Author: Carlton Brady
import re


def read_training_set():
    fobj = open("training_set.txt", "r")
    lines = fobj.readlines()
    word_exp = re.compile(' [\w\'\.\*]+ ')
    number_exp = re.compile('[0-9]+')

    trigram_dict = {}
    total_trigrams = 0

    bigram_dict = {}
    total_bigrams = 0

    unigram_dict = {}
    total_unigrams = 0

    charset = set()
    for line in lines:
        word_match = word_exp.search(line)
        count_match = number_exp.search(line)
        word = str(word_match.group())
        print(word)
        count = int(count_match.group())
        print(count)

        # Update trigram dict
        i = 0
        while i < len(word) - 2:
            trigram = word[i] + word[i+1] + word[i+2]
            charset.add(word[i])
            if trigram_dict.get(trigram) is None:
                trigram_dict.update({trigram: count})
            else:
                trigram_dict.update({trigram: trigram_dict.get(trigram) + count})
            total_trigrams += count
            i += 1

        # Update bigram dict
        j = 0
        while j < len(word)-1:
            bigram = word[j] + word[j+1]
            if bigram_dict.get(bigram) is None:
                bigram_dict.update({bigram: count})
            else:
                bigram_dict.update({bigram: bigram_dict.get(bigram) + count})
            total_bigrams += count
            j += 1

        k = 0
        # Update unigram dict
        while k < len(word):
            unigram = word[k]
            if unigram_dict.get(unigram) is None:
                unigram_dict.update({unigram: count})
            else:
                unigram_dict.update({unigram: unigram_dict.get(unigram) + count})
            total_unigrams += count
            k += 1

    print(total_trigrams)
    print(total_bigrams)
    print(total_unigrams)
    fobj.close()
    return trigram_dict, total_trigrams, charset


trigram_dict, total_trigrams, charset = read_training_set()



