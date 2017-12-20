#Book material in polish

# Jaka to liczba?
#
# Komputer wybiera losowo liczbę z zakresu od 1 do 100.
# Gracz próbuje ją odgadnąć, a komputer go informuje,
# czy podana przez niego liczba jest: za duża, za mała,
# prawidłowa.

import random

def greetings():
    print("\tWitaj w grze 'Jaka to liczba'!")
    print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
    print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")

def winner(the_number, tries):
    print("Odgadłeś! Ta liczba to", the_number)
    print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!\n")  
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

def ask_number(question, the_number):
    guess = int(input(question))
    tries = 1
    while guess != the_number:
        if guess in range(0, 101):
            if guess > the_number:
                print("Za duża...")
                guess = int(input(question))
                tries += 1
            else:
                print("Za mała...")
                guess = int(input(question))
                tries += 1
        else:
            print("The number from 1 to 100 mister!")
            guess = int(input(question))
            tries = 1
    return guess, tries
    

def main():
    the_number = random.randint(0, 100)
    question = "What is the number? "
    greetings()
    guess, tries = ask_number(question, the_number)
    winner(the_number, tries)

main()
    
    
