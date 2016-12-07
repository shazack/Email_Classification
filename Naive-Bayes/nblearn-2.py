import os
import sys
import string
from collections import defaultdict

class SpamorHam:
    def __init__(self):
        self.count_totalfiles = 0
        
    def read_all_files(self,directory):
        onlyfiles=[]
        for dirpath,_,filenames in os.walk(directory):
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


        print("spam")
        print(count_spam)
        print("ham")
        print(count_ham)

        # calculate prob of spam and ham
        #

        # print("prob of spam")
        # print(prob_spam)
        prob_spam = float(count_spam) / float(self.count_totalfiles)
        prob_ham = float(count_ham) / float(self.count_totalfiles)
        # print("prob of ham")
        # print(prob_ham)

        # calculate all the probabilities within the spam folder





        spam_freq = defaultdict(int)
        ham_freq = defaultdict(int)
        total_freq = {}
        count = 0
        spam_count = 0
        ham_count = 0
        for i in spam_files:
            with open(i, "r", encoding="latin1") as f:
                lines = f.read().splitlines()
                # print(lines)
                for i in lines:
                    tokenlist = i.split()
                    for token in tokenlist:
                        if token not in string.punctuation:
                            if token not in spam_freq:
                                spam_freq[token] = 1
                            else:
                                spam_freq[token] += 1
        for i in ham_files:
            with open(i, "r", encoding="latin1") as f:
                lines = f.read().splitlines()
                # print(lines)
                for i in lines:
                    tokenlist = i.split()
                    for token in tokenlist:
                        if token not in string.punctuation:
                            if token not in ham_freq and token not in string.punctuation:
                                ham_freq[token] = 1
                            else:
                                ham_freq[token] += 1

        # print("ham dictionary")
        # print(sum(ham_freq.values()))


        # spam_freq = collections.Counter()
        # for i in spam_files:
        #     with open(i, "r", encoding="latin1") as file:
        #         tokens = file.read().strip().split()
        #         for token in tokens:
        #             if token not in string.punctuation:
        #                 spam_freq.update(token)
        #
        # ham_freq = collections.Counter()
        # for i in ham_files:
        #     with open(i, "r", encoding="latin1") as file:
        #         tokens = file.read().strip().split()
        #         for token in tokens:
        #             if token not in string.punctuation:
        #                 ham_freq.update(token)




        # print(sum(ham_freq.values()))




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

        # print("total dictionary")
        # print(total_freq)


        spam_count = sum(spam_freq.values())
        ham_count = sum(ham_freq.values())

        prob_ham_words = {}
        prob_spam_words = {}
        # print("vocab")
        # print(len(total_freq))
        # writing into nboutput.txt
        print("distinct words")
        print(len(total_freq))

        with open("nbmodel-2.txt", "w") as f1:
            f1.write("spamtotal" + ":" + str(prob_spam))
            f1.write("\n")
            f1.write("hamtotal" + ":" + str(prob_ham))
            f1.write("\n")
            # for sword,sfreq in spam_freq.items():
            #     prob_word = (float(sfreq)+1.0) / (float(spam_count)+float(len(total_freq)))
            #     f1.write("spam"+":"+str(sword)+":"+str(prob_word))
            #     f1.write("\n")
            #
            # for hword,hfreq in ham_freq.items():
            #     prob_word = (float(hfreq)+1.0) / (float(ham_count)+float(len(total_freq)))
            #     f1.write("ham"+":"+str(hword)+":"+str(prob_word))
            #     f1.write("\n")


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
    s = SpamorHam()
    totalfiles = s.read_all_files("/Users/nisharazack/Documents/NLP/Assignment2/Spam or Ham/train/")
    s.count_totalfiles = len(totalfiles)
    print("Total number of Files")
    print(s.count_totalfiles)
    s.execute()


