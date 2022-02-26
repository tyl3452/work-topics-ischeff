# This is designed to be done with elementary/middle school students
# especially in the context of an ELA lesson (since we never do enough grammar!)

# There are only seven types of sentences in the English language: one simple, three compound
# two complex, and one compound-complex. (You can see definitions here: https://www.dailywritingtips.com/7-patterns-of-sentence-structure/)

# The goal of this lab is to generate a sentence by randomly picking the elements of a given sentence structure.

import random

articles = ["A", "The", "One", "Some"]
nouns = ["apple", "carrot", "rabbit", "banana", "basketball", "chess", "sun", "wind"]
verbs = ["cooks", "blows", "bounces", "walks", "jumps", "calls", "stays", "runs", "abides"]

def simple_sentence():
    sentence = random.choice(articles) + " " + random.choice(nouns) + " " + random.choice(verbs) + "."
    return sentence

# def compound_sentence():
#     # add code here to generate a compound sentence
#
# def complex_sentence():
#     # add code here to generate a complex sentence
#
# def compound_complex_sentence():
#     # add code here to generate a compound-complex sentence

if __name__ == "__main__":
    simple_sentence = simple_sentence()
    print(simple_sentence)
    # compound_sentence = compound_sentence()
    # print(compound_sentence)
    # complex_sentence = complex_sentence()
    # print(complex_sentence)
    # compound_complex_sentence = compound_complex_sentence()
    # print(compound_sentence)
