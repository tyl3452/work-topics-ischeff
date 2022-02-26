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
