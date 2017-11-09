<<<<<<< HEAD
#Write ou all given words in random order without repetirions

import random

words = ['starcraft', 'diablo', 'overwatch', 'heartstone', 'witcher']
new_words = []

count_words = len(words)
written = 0

while written != count_words:
    word = random.choice(words)
    if word not in new_words:
        new_words.append(word)
        written += 1
        print(word)



=======
#Write ou all given words in random order without repetirions

import random

words = ['starcraft', 'diablo', 'overwatch', 'heartstone', 'witcher']
new_words = []

count_words = len(words)
written = 0

while written != count_words:
    word = random.choice(words)
    if word not in new_words:
        new_words.append(word)
        written += 1
        print(word)



<<<<<<< HEAD

>>>>>>> 5.1
=======
>>>>>>> 5.1
