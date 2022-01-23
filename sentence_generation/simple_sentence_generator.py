# This is designed to be the SIMPLEST possible sentence generator
# Since it doesn't use any ML techniques
# Maybe we can use this as a basic demo?
import random
import time
# Below is the 'corpus' (I hesitate to use that word since this is so limited)
# of words that the model can draw on. The model has five words.
article = ["A", "The", "One"]
noun = ["apple", "carrot", "rabbit"]
verb = ["began", "started"]
verb1 = ["to cook", "to sink", "to swim", "to fly", "to speak"]
adverb = ["quickly", "slowly", "rapidly"]
# Now, we randomly choose a word from each list! (Since the list are pre-broken down into
# related clusters--there are better terms for this--it obviously simplifies things further.)
a = random.choice(article)
b = random.choice(noun)
c = random.choice(verb)
d = random.choice(verb1)
e = random.choice(adverb)
# Now, we very crudely combine the words together!
sentence = a + " " + b + " " + c + " " + d + " " + e + "."
print(sentence)
