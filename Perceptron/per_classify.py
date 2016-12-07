import os
import collections
import sys
from random import sample
from collections import defaultdict
import json
from pprint import pprint


class Perceptrontest:
    def __init__(self):
        self.activation = 0
        self.onlyfiles = []
        w = {}
        self.weight = defaultdict(lambda: 0, w)
        self.result = []

    def read_all_files(self, directory):

        for dirpath, _, filenames in os.walk(directory):
            for f in filenames:
                if f.endswith(".txt"):
                    self.onlyfiles.append(os.path.abspath(os.path.join(dirpath, f)))
        return self.onlyfiles

    def read_model(self):
        prior_list = []
        with open("per_model.txt", "r", encoding="latin1") as file:
            lines = file.read().split("\n")
            b, self.bias = lines[0].split(":")
            print("bias")
            print(self.bias)
            for i in lines[1:]:
                each = i.split(":")
                # print(each)
                if len(each) > 1:
                    self.weight[each[0]] = each[1]

    def test_model(self):
        weight_sum = 0

        for file in self.onlyfiles:
            weight_sum = 0
            with open(file, "r", encoding="latin1") as f:
                tokens = f.read().strip().split()
                for word in tokens:
                    if word in self.weight:
                        weight_sum += float(self.weight[word])
                self.activation = weight_sum + float(self.bias)
                if self.activation > 0:
                    label = "spam"
                else:
                    label = "ham"
                self.result.append((label, file))
        # print(self.result)
        with open("per_output.txt", "w", encoding="latin1") as f:
            for i in self.result:
                f.write(i[0] + " " + i[1])
                f.write("\n")


if __name__ == "__main__":
    p = Perceptrontest()
    #directory = "/Users/nisharazack/Documents/NLP/Assignment 2/Spam or Ham/train/"
    d = "/Users/nisharazack/Documents/NLP/Assignment2/Spam or Ham/dev/4/"
    totalfiles = p.read_all_files(d)
    count_totalfiles = len(totalfiles)
    print(count_totalfiles)
    p.read_model()
    p.test_model()
    countspam = 0
    countham = 0
    count = 0
    hamtot = 0
    spamtot = 0
    bespam = 0
    beham = 0
    for k, v in p.result:
        # print(k,v)
        if v.find("ham.txt") > 0 and k == "ham":
            countham += 1
            count += 1
        if v.find("spam.txt") > 0 and k == "spam":
            countspam += 1
            count += 1
        if v.find("ham.txt") > 0:
            hamtot += 1
        if v.find("spam.txt") > 0:
            spamtot += 1
        if k == "ham":
            beham += 1
        if k == "spam":
            bespam += 1

    print(countspam)
    print(countham)
    accuracy = float(count) / float(count_totalfiles)
    print("Accuracy")
    print(accuracy)
    print("Perceptron Recall Spam")
    respam = countspam / spamtot
    print(respam)
    print("Perceptron Recall Ham")
    reham = countham / hamtot
    print(reham)
    print("Perceptron Precision Spam")
    prespam = countspam / bespam
    print(prespam)
    print("Perceptron Precision Ham")
    preham = countham / beham
    print(preham)
    print("Perceptron F1 score Spam")
    f1spam = (2 * prespam * respam) / (prespam + respam)
    print(f1spam)
    print("Perceptron F1 score Ham")
    f1ham = (2 * preham * reham) / (preham + reham)
    print(f1ham)




