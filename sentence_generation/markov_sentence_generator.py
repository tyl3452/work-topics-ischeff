# import random
# weather_chain = {
#     'sun': ['sun', 'sun', 'sun', 'sun', 'sun', 'sun', 'sun', 'sun', 'sun', 'rain'],
#     'rain': ['sun', 'rain']
# }
#
# weather = [random.choice(list(weather_chain.keys()))]
#
# for i in range(10):
#     weather.append(random.choice(weather_chain[weather[i]]))
#
# print(weather)

#get input - use your own song lyrics!
def input(text):
    with open(text) as f:
        # corpus = f.readlines()
        corpus = f.read()
        # corpus.split("\n")
    return corpus

def build_markov(corpus, state_size):
    corpus = corpus.split()#split the string input into a list of words
    markov = {}#create an empty dictionary to hold the model - keys and values are words
    for i in range(state_size, len(corpus)):
        current_word = corpus[i]
        previous_words = ' '.join(corpus[i-state_size:i])
        if previous_words in markov:
            markov[previous_words].append(current_word)
        else:
            markov[previous_words] = [current_word]
    return markov

#
#
# def build_model(source, state_size):
#     '''
#     Given some corpus and a state size, build a Markov chain model (as a dictionary).
#     '''
#     source = source.split()
#     model = {}
#     for i in range(state_size, len(source)):
#         current_word = source[i]
#         previous_words = ' '.join(source[i-state_size:i])
#         if previous_words in model:
#             model[previous_words].append(current_word)
#         else:
#             model[previous_words] = [current_word]
#
#     return model


# we can assume a line ends with a newline character.

if __name__ == "__main__":
    body = input('drake.txt')
    print(body)
    model = build_markov(body,2)#this seems to be making a model based on characters, not words
    print(model)
    # print(model[len(model)-1])
