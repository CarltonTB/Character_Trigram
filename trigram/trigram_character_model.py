# Author: Carlton Brady (solo)
# CISC689 HW1 Q3
import re
import sys
from os import path


class StupidBackOffTrigramModel:

    def __init__(self, trigram_dict, total_trigrams, bigram_dict, total_bigrams,
                 unigram_dict, total_unigrams, charset):
        self.trigram_dict = trigram_dict
        self.total_trigrams = total_trigrams
        self.bigram_dict = bigram_dict
        self.total_bigrams = total_bigrams
        self.unigram_dict = unigram_dict
        self.total_unigrams = total_unigrams
        self.charset = charset

    def get_next_char_probability(self, prev_chars, next_char):
        if len(prev_chars) != 2:
            print("Error: please only provide the previous 2 characters")
            return
        else:
            # calculate trigram probability
            trigram_count = self.trigram_dict.get(prev_chars + next_char)
            if trigram_count is not None:
                probability = trigram_count / self.total_trigrams
            else:
                # backoff to bigram
                bigram_count = self.bigram_dict.get(prev_chars[len(prev_chars)-1] + next_char)
                if bigram_count is not None:
                    probability = 0.4 * (bigram_count / self.total_bigrams)
                else:
                    # backoff to unigram
                    unigram_count = self.unigram_dict.get(next_char)
                    if unigram_count is not None:
                        probability = 0.4 * 0.4 * (unigram_count / self.total_unigrams)
                    else:
                        print("Error: character not found in the model")
                        return

            return probability

    def get_probabilities_for_all_possible_next_chars(self, prev_chars):
        probabilities_dict = {}
        for char in self.charset:
            probabilities_dict.update({char: self.get_next_char_probability(prev_chars, char)})
        return probabilities_dict

    def get_next_char_ranks_and_probabilities(self, prev_chars):
        next_char_probs = self.get_probabilities_for_all_possible_next_chars(prev_chars)
        probs_dict_copy = next_char_probs.copy()
        rank_order = []
        while len(probs_dict_copy) != 0:
            top_char = max(probs_dict_copy, key=probs_dict_copy.get)
            rank_order.append(top_char)
            probs_dict_copy.pop(top_char)
        return rank_order, next_char_probs

    def print_top_next_char_ranks(self, trigram):
        if len(trigram) != 3:
            print("Error: trigram input must be 3 characters long")
            return
        ranks, next_char_probs = self.get_next_char_ranks_and_probabilities(trigram[:2])
        print("Top 3 most likely next characters for bigram " + "'" + trigram[:2] + "':")
        i = 0
        while i < 3:
            print(str(i + 1) + ". ", "'" + ranks[i] + "'" + ", probability=" + str(next_char_probs.get(ranks[i])))
            i += 1
        print("Actual next character:", "'" + trigram[len(trigram)-1] + "'" + ", rank=" +
              str(ranks.index(trigram[len(trigram)-1])+1) + ",", "probability=" + str(next_char_probs.get(trigram[len(trigram)-1])))

    def print_word_results(self, word):
        word = " " + word + " "
        i = 0
        while i < len(word)-2:
            self.print_top_next_char_ranks(word[i]+word[i+1]+word[i+2])
            i += 1

    def print_results_for_word_list(self, word_list):
        for word in word_list:
            print("Input word:", word)
            self.print_word_results(word)
            print("\n")


def create_model_from_training_set():
    print("Creating trigram model...")
    if path.exists("training_set.txt"):
        fobj = open("training_set.txt", "r")
    else:
        fobj = open("trigram/training_set.txt", "r")
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
        count = int(count_match.group())
        # print(word)
        # print(count)

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

    # print("total trigrams: ", total_trigrams)
    # print("total bigrams: ", total_bigrams)
    # print("total unigrams: ", total_unigrams)
    fobj.close()
    print("Model complete!\n")
    return StupidBackOffTrigramModel(trigram_dict, total_trigrams, bigram_dict,
                                     total_bigrams, unigram_dict, total_unigrams, charset)


if __name__ == "__main__":
    sb_trigram_model = create_model_from_training_set()
    if len(sys.argv) > 1:
        sb_trigram_model.print_results_for_word_list(sys.argv[1:])
    else:
        # input_words = input("Enter a one or more words separated by a space to see the trigram model output:\n")
        # word_list = input_words.split(" ")
        word_list = ["hello", "weather", "mystique", "catcher"]
        sb_trigram_model.print_results_for_word_list(word_list)

