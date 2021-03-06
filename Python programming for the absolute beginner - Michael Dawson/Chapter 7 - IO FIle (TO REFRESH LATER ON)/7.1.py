# The material from the book in polish

# Turniej wiedzy
# Gra sprawdzająca wiedzę ogólną, odczytująca dane ze zwykłego pliku tekstowego

import sys

def open_file(file_name, mode):
    """Otwórz plik."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie można otworzyć pliku", file_name, "Program zostanie zakończony.\n", e)
        input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Zwróć kolejny wiersz pliku kwiz po sformatowaniu go."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def name():
    user_name = input("What's your name? ")
    return user_name

def fake():
    fake = ("scores.dat", "wb")    
    for i in range(5):
        fake[i] = ["Gość", "0"]
    return fake
    fake.close()

def highlights(score, user_name):
    try:
        scores = open("scores.dat", "rb+")
    except:
        fake()
        
    scores = open("scores.dat", "rb+")
    highlights = []

    for i in range(5):
        highlights += scores[i]
 
    sorted(highlight.keys())
    
    for i in range(5):
        if score > highlights[i[1]]:
            highlights[i + 4] = highlights[i + 3]
            highlights[i + 3] = highlights[i + 2]
            highlights[i + 2] = highlights[i + 1]
            highlights[i + 1] = highlights[i]
            highlights[i] = [score, user_name]

    for i in range(5):
        print(str(i), "score:")
        print(highlights[i])

    scores.close()     
     
def next_block(the_file):
    """Zwróć kolejny blok danych z pliku kwiz."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explanation = next_line(the_file)

    point = next_line(the_file)

    return category, question, answers, correct, explanation, point

def welcome(title):
    """Przywitaj gracza i pobierz jego nazwę."""
    print("\t\t Witaj w turnieju wiedzy!\n")
    print("\t\t", title, "\n")
 
def main():
    trivia_file = open_file("kwiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # pobierz pierwszy blok
    category, question, answers, correct, explanation, point = next_block(trivia_file)
    while category:
        # zadaj pytanie
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # uzyskaj odpowiedź
        answer = input("Jaka jest Twoja odpowiedź?: ")

        # sprawdź odpowiedź
        if answer == correct:
            print("\nOdpowiedź prawidłowa!", end=" ")
            score += int(point)
        else:
            print("\nOdpowiedź niepoprawna.", end=" ")
        print(explanation)
        
        print("Wynik:", score, "\n\n")

        # pobierz kolejny blok
        category, question, answers, correct, explanation, point = next_block(trivia_file)

    
    
    user_name = name()
    highlights(score, user_name)    

    trivia_file.close()

    print("To było ostatnie pytanie!")
    print("Twój końcowy wynik wynosi", score)
 
main()  
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
