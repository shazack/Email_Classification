import os
import collections
import sys

class SpamorHam:
    def __init__(self):
        self.count_totalfiles = 0
    def read_all_files(self,directory):
        onlyfiles = []
        for dirpath, _, filenames in os.walk(directory):
            for f in filenames:
                if f.endswith(".txt"):
                    onlyfiles.append(os.path.abspath(os.path.join(dirpath, f)))
        return onlyfiles

    def execute(self):
        spam_files = []
        ham_files = []
        for i in totalfiles:
            if i.find("spam.txt") > 0:
                spam_files.append(i)

            elif i.find("ham.txt") > 0:
                ham_files.append(i)

        count_spam = len(spam_files)
        count_ham = len(ham_files)

        # calculate prob of spam and ham
        prob_spam = float(count_spam) / float(self.count_totalfiles)
        prob_ham = float(count_ham) / float(self.count_totalfiles)
        # print("prob of ham")
        # print(prob_ham)

        # calculate all the probabilities within the spam folder

        spam_freq = {}
        ham_freq = {}
        total_freq = {}
        count = 0
        spam_count = 0
        spam_freq = collections.Counter()
        for i in spam_files:
            with open(i, "r", encoding="latin1") as file:
                for line in file:
                    spam_freq.update(line.split())

        ham_freq = collections.Counter()
        for i in ham_files:
            with open(i, "r", encoding="latin1") as file:
                for line in file:
                    ham_freq.update(line.split())

        for i in totalfiles:
            with open(i, "r", encoding="latin1") as f:
                lines = f.read().splitlines()
                for i in lines:
                    tokenlist = i.split()
                    for token in tokenlist:
                        if token not in total_freq:
                            total_freq[token] = 1
                        else:
                            total_freq[token] += 1

        spam_count = sum(spam_freq.values())
        ham_count = sum(ham_freq.values())

        prob_ham_words = {}
        prob_spam_words = {}

        print("distinct words")
        print(len(total_freq))

        with open("nbmodel.txt", "w") as f1:
            f1.write("spamtotal" + ":" + str(prob_spam))
            f1.write("\n")
            f1.write("hamtotal" + ":" + str(prob_ham))
            f1.write("\n")

            for word, freq in total_freq.items():
                if word in ham_freq:
                    prob_word_ham = (float(ham_freq[word]) + 1.0) / (float(ham_count) + float(len(total_freq)))
                    f1.write("ham" + ":" + str(word) + ":" + str(prob_word_ham))
                    f1.write("\n")
                else:
                    prob_word_ham = (1 / (float(ham_count) + float(len(total_freq))))
                    f1.write("ham" + ":" + str(word) + ":" + str(prob_word_ham))
                    f1.write("\n")

                if word in spam_freq:
                    prob_word_spam = (float(spam_freq[word]) + 1.0) / (float(spam_count) + float(len(total_freq)))
                    f1.write("spam" + ":" + str(word) + ":" + str(prob_word_spam))
                    f1.write("\n")
                else:
                    prob_word_spam = (1 / (float(spam_count) + float(len(total_freq))))
                    f1.write("spam" + ":" + str(word) + ":" + str(prob_word_spam))
                    f1.write("\n")


if __name__ == "__main__":
    # count the total number of files
    s = SpamorHam()
    totalfiles = s.read_all_files("/Users/nisharazack/Documents/NLP/Assignment2/Spam or Ham/train/")
    s.count_totalfiles = len(totalfiles)
    print("Total number of Files")
    print(s.count_totalfiles)
    s.execute()


