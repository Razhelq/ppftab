# The material from the book in polish
# NOT DONE NOT WORKING

# Turniej wiedzy
# Gra sprawdzająca wiedzę ogólną, odczytująca dane ze zwykłego pliku tekstowego

import sys, shelve

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
# Not finished
def welcome(title):
    """Przywitaj gracza i pobierz jego nazwę."""
    print("\t\t Witaj w turnieju wiedzy!\n")
    print("\t\t", title, "\n")

def fake():
    fake_scores = shelve.open("total_score.dat")
    for i in range(5):
        fake_scores[str(i)] = {"Grasz", "0"}        
        name, score = fake_scores[str(i)]
        print((i + 1), name, " got ", score, " points.")
    fake_scores.sync()
    fake_scores.close()
    
def highlights(new_score):
    try:
        total_score = shelve.open("total_score.dat", "w")
    except:
        fake()
        total_score = shelve.open("total_score.dat", "c")

    name = str(input("What is your name? "))
    new_score = {name : new_score}
    tries = 0
    
    total_scores = total_score
    total_scores = sorted(total_scores.values())
    
    print("Old best scores:")
    for i in range(5):
        name, score = total_scores[i]
        print((i + 1), name, " got ", score, " points.")          
          
    for i in range(5):
        name, score = total_scores[i]                
        if new_score[name] > score and tries == 0 and new_score[name] != 0:
            total_scores[i + 4] = total_scores[i + 3]
            total_scores[i + 3] = total_scores[i + 2]
            total_scores[i + 2] = total_scores[i + 1]
            total_scores[i + 1] = total_scores[i]
            total_scores[i] = new_score
            tries += 1

            
    print("!", total_score)
    total_scores = sorted(total_scores.values())
    print("!!!", total_scores)

    print("New best scores:")

    for i in range(5):
        name, score = total_scores[i]
        print((i + 1), name, " got ", score, " points.")

    total_score.sync()
    total_score.close()
 
def main():
    trivia_file = open_file("kwiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    #fake()

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

    trivia_file.close()

    print("To było ostatnie pytanie!")
    print("Twój końcowy wynik wynosi", score)
    
    highlights(str(score))
 
main()  
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
