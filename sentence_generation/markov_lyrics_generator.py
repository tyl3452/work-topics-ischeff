#get input - use your own song lyrics!
import random
def input(text):
    with open(text) as f:
        corpus = f.read()
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

def generate_text(model, state_size, min_length):

    #Let's assume that each line starts with a capital letter
    def get_new_starter():
        return random.choice([s.split(' ') for s in model.keys() if s[0].isupper()])
    text = get_new_starter()

    i = state_size
    while True:
        key = ' '.join(text[i-state_size:i])
        if key not in model:
            text += get_new_starter()
            i += 1
            continue

        next_word = random.choice(model[key])
        text.append(next_word)
        i += 1
        if i > min_length and text[-1][-1] == '.':
            break
    return ' '.join(text)

if __name__ == "__main__":
    body = input('drake.txt')
    print(body)
    model = build_markov(body,10)#this seems to be making a model based on characters, not words
    print(model)
    print(generate_text(model,10,100))
    # body = input('beatles.txt')
    # print(body)
    # model = build_markov(body,2)#this seems to be making a model based on characters, not words
    # print(model)
    # print(generate_text(model,2,100))
    # body = input('adele.txt')
    # print(body)
    # model = build_markov(body,2)#this seems to be making a model based on characters, not words
    # print(model)
    # print(generate_text(model,2,100))
