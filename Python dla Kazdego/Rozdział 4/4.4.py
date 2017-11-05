# Finding the correct word

from random import choice
WORDS = ("diablo", "starcraft", "warcraft", "overwatch", "heartstone", "Destiny")

word = choice(WORDS)
letters = len(word)

tries = 0

print("Hello, Yuu need to find the chosen word.")
print("The word has %d letters" % letters)
letter = input("What letter can it include? ")
tries += 1

while tries < 6:
    if letter in word:
        print("Yes, You're right")
        letter = input("What another letter can it include? ")
        tries += 1
    else:
        print("Sorry there in no latter like this.")
        letter = input("What another letter can it include? ")
        tries += 1

users_word = input("Now, guess a word: ")

if users_word.lower() == word:
    print("You are right mister!")
else:
    print("Sorry man.")