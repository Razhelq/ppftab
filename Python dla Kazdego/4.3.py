# Polish base from the course

# Wymieszane litery
# Wymieszane litery
# Komputer wybiera losowo słowo, a potem miesza w nim litery
# Gracz powinien odgadnąć pierwotne słowo

import random

# utwórz sekwencję słów do wyboru
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
# wybierz losowo jedno słowo z sekwencji
word = random.choice(WORDS)

tip_count = WORDS.index(word)

# utwórz zmienną, by później użyć jej do sprawdzenia, czy odpowiedź jest poprawna
correct = word

tips = ("this language", "some king of graf", "trudny?", "pytanie?", "kui wi")
notip = True

# utwórz 'pomieszaną' wersję słowa
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# rozpocznij grę
print(
    """
               Witaj w grze 'Wymieszane litery'!

       Uporządkuj litery, aby odtworzyć prawidłowe słowo.
    (Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
    """
)
print("Zgadnij, jakie to słowo:", jumble)

tries = 0
guess = input("\nTwoja odpowiedź: ")
tries += 1
while guess != correct and guess != "":
    print("Niestety, to nie to słowo.")
    if tries > 2 and notip:
        tip = input("Would you like to get a tip? ")
        tip = tip.lower()
        if tip == "yes":
            print(tips[tip_count])
            notip = False
            guess = input("Twoja odpowiedź: ")
            tries += 1
        else:
            guess = input("Twoja odpowiedź: ")
            tries += 1
    else:
        guess = input("Twoja odpowiedź: ")
        tries += 1
if guess == correct:
    if notip:
        print("Zgadza sie! Zgadłes i nie wykozystales podpowiedzi")
    else:
        print("Zgadza się! Zgadłeś!\n")

print("Dziękuję za udział w grze.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
