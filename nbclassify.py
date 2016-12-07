import os
import sys
import math
import re
import operator
import numpy
import functools
import math
import string
from collections import defaultdict


class Spam_Ham:
    def __init__(self):
        self.count_totalfiles = 0
        self.correctspam = 0
        self.correctham = 0
        self.totspam = 0
        self.totham = 0
        self.cspam = 0
        self.cham = 0
        self.count = 0
        self.accuracy = 0

    def read_all_files(self, directory):
        onlyfiles = []
        for dirpath, _, filenames in os.walk(directory):
            for f in filenames:
                if f.endswith(".txt"):
                    onlyfiles.append(os.path.abspath(os.path.join(dirpath, f)))
        return onlyfiles

    def execute(self):
        prior_list = []
        with open("nbmodel-2.txt") as file:
            lines = file.read().split("\n")
            for i in lines:
                each = i.split(":")
                prior_list.append(each)

        spam_dict = defaultdict(float)
        ham_dict = defaultdict(float)
        all_dict = defaultdict(list)

        for i in prior_list:
            if i[0] == "spamtotal":
                prob_spam = i[1]
            if i[0] == "hamtotal":
                prob_ham = i[1]
            if i[0] == "spam":
                if len(i[2]) > 0:
                    spam_dict[i[1]] = i[2]
            if i[0] == "ham":
                if len(i[2]) > 0:
                    ham_dict[i[1]] = i[2]
            if i[0] == "spam" or i[0] == "ham":
                all_dict[i[1]] = i[2], i[0]

        result = 0.0
        tokens = []
        prob_word_list = []
        results_dict = defaultdict(str)
        message_given_ham = 0.0
        message_given_spam = 0.0
        delimiters = ['\n', ' ', ',', '.', '?', '!', ':', '-', ')', '(', '$']
        for i in totalfiles:
            with open(i, "r", encoding="latin1") as file:
                tokens = []
                prob_word_list = []

                tokens = file.read().strip().split()

                for token in tokens:
                    # add the probability to list to multiply the independent probs only if its already present in the list
                    if token in spam_dict:
                        prob_word_list.append(float(spam_dict[token]))

                log_message_given_spam = sum([math.log(word) for word in prob_word_list])

                prob_word_list = []

                for token in tokens:
                    # add the probability to list to multiply the independent probs only if its already present in the list
                    if token in ham_dict:
                        if len(ham_dict[token]) > 0:
                            prob_word_list.append((float(ham_dict[token])))

                log_message_given_ham = sum([math.log(word) for word in prob_word_list])

                log_prob_spam = math.log(float(prob_spam))
                log_prob_ham = math.log(float(prob_ham))

                log_result_spam = log_prob_spam + log_message_given_spam
                log_result_ham = log_prob_ham + log_message_given_ham

                with open("nboutput-2.txt", "w") as f:
                    if log_result_spam >= log_result_ham:
                        f.write("spam" + " " + str(i))
                        results_dict[i] = "spam"
                    else:
                        f.write("ham" + " " + str(i))
                        results_dict[i] = "ham"
                    f.write("\n")
        # prob(spam | message ) = prob_spam* message_given_spam / prob_spam * message_given_spam + prob_ham *message_given_ham

        orig_dict = defaultdict(str)

        spam_files = []
        ham_files = []
        for i in totalfiles:
            if i.find("spam.txt") > 0:
                orig_dict[i] = "spam"
            elif i.find("ham.txt") > 0:
                orig_dict[i] = "ham"

        for k, v in results_dict.items():
            if k in orig_dict:
                if v == orig_dict[k]:
                    self.count += 1
                if v == "spam":
                    self.cspam += 1
                if v == "ham":
                    self.cham += 1

        self.accuracy = float(self.count) / float(len(results_dict))
        self.correctspam = 0
        self.correctham = 0
        self.totspam = 0
        self.totham = 0

        for k, v in results_dict.items():
            if k in orig_dict:
                if v == orig_dict[k] and v == "spam":
                    self.correctspam += 1
                if v == orig_dict[k] and v == "ham":
                    self.correctham += 1

        for k, v in orig_dict.items():
            if v == "spam":
                self.totspam += 1
            if v == "ham":
                self.totham += 1

    def evaluate(self):
        # calculate precision, recall and recall
        preham = self.correctham / self.cham
        prespam = self.correctspam / self.cspam

        recallham = self.correctham / self.totham
        recallspam = self.correctspam / self.totspam

        f1ham = 2 * ((preham * recallham) / (preham + recallham))
        f1spam = 2 * ((prespam * recallspam) / (prespam + recallspam))

        # prespam = round(prespam,2)
        # preham = round(preham,2)
        # recallham = round(recallham,2)
        # recallspam = round(recallspam,2)
        # f1ham = round(recallham,2)
        # f1spam = round(recallspam,2)
        # accuracy = round(accuracy,2)
        print("Precision, Recall, F1")
        print("Ham")
        print(preham, recallham, f1ham)
        print("Spam")
        print(prespam, recallspam, f1spam)
        print("Weighted avg")
        print(self.accuracy)


if __name__ == "__main__":
    # count the total number of files
    s = Spam_Ham()
    totalfiles = s.read_all_files("/Users/nisharazack/Documents/NLP/Assignment2/Spam or Ham/dev/")
    s.count_totalfiles = len(totalfiles)
    s.execute()
    s.evaluate()


