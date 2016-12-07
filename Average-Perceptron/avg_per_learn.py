import os
import collections
import sys
#from random import sample
import random
from collections import defaultdict
import json
from collections import Counter

class Perceptron:
    def __init__(self):
        self.maxiter = 30
        w = {}
        self.weight = defaultdict(lambda: 0, w)
        self.bias = 0
        self.onlyfiles = []
        self.y = 0
        self.activation = 0
        self.pred = 0
        self.u = defaultdict(lambda: 0, w)
        self.c = 1
        self.avg_bias = 0

    def read_all_files(self,directory):

        for dirpath,_,filenames in os.walk(directory):
            for f in filenames:
                if f.endswith(".txt"):
                    self.onlyfiles.append(os.path.abspath(os.path.join(dirpath, f)))
        return self.onlyfiles

    def is_spam(self,file):
        if file.find("spam.txt") > 0:
            y = 1
        elif file.find("ham.txt") > 0:
            y = -1
        return y
    # def vocab(self):
    #     for file in self.files

    def build_model(self):
        weight_sum = 0
        ylabel = defaultdict(int)
        allwords = {}
        filewords = {}
        temp = 0
        c = self.c

        for file in self.onlyfiles:
            # label value computation spam -> 1 ham -> -1
            ylabel[file] = self.is_spam(file)
            with open(file, "r", encoding="latin1") as f:
                tokens = f.read().strip().split()
                # print(tokens,file,self.y)
                filewords[file] = tokens
                #self.weight = defaultdict(lambda: 0, w)
                for word in tokens:
                    if word not in allwords:
                        self.weight[word] = 0
                        self.u[word] = 0

        # print(self.weight)
        # print(self.u)
        # print(filewords)


        for iter in range(0,self.maxiter):
            random.shuffle(self.onlyfiles)
            for file in self.onlyfiles:
                weight_sum = 0
                #label value computation spam -> 1 ham -> -1
                self.y = ylabel[file]
                for word in filewords[file]:
                    weight_sum += self.weight[word]
                #calculate activation function

                self.activation = weight_sum + self.bias
                self.pred = self.y * self.activation
                # print(self.activation)
                # print(self.pred)
                # print(self.weight)
                # print("\n")
                if self.pred <= 0:
                    for word in filewords[file]:
                        self.weight[word] = self.weight[word] + self.y
                        self.u[word] = self.u[word] + self.y * c
                    self.bias = self.bias + self.y
                    self.avg_bias = self.avg_bias + self.y * c
                c += 1
        for k,v in self.u.items():
            #print(self.weight[k],c,k)
            self.u[k] = self.weight[k] - (1/c)*(v)

        self.avg_bias = self.bias - (1/c)*self.avg_bias
        # print(self.u)
        # print(self.weight)
        print(self.avg_bias)
        #



if __name__ == "__main__":

    p = Perceptron()

    #count the total number of files
    #directory = sys.argv[1]

    directory = "/Users/nisharazack/Documents/NLP/Assignment2/Spam or Ham/train/"
    d = "/Users/nisharazack/Documents/NLP/Assignment 2/Spam or Ham/sample/"
    totalfiles = p.read_all_files(directory)
    count_totalfiles = len(totalfiles)
    print(count_totalfiles)
    p.build_model()
    #print(p.weight)
    #print(p.bias)
    bias = {"bias":p.bias}

    with open("per_model-2.txt", "w", encoding="latin1") as f1:
        f1.write("bias" + ":" + str(p.avg_bias))
        f1.write("\n")
        for k, v in p.u.items():
            f1.write(str(k) + ":" + str(v))
            f1.write("\n")


