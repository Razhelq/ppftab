# The material from the book in polish
# NOT DONE NOT WORKING

# Turniej wiedzy
# Gra sprawdzająca wiedzę ogólną, odczytująca dane ze zwykłego pliku tekstowego

import sys, pickle

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

def highlights(new_score):
    total_score = open("total_score.dat", "rb+")
    

    scores = pickle.load(total_score)
    print("Old best scores:")
    for i in range(5):
        score = total_score.readline(i)
        scores.append(score)
        print("Score ", (i + 1), "is", score)
          
    print(scores)

    for i in range(5):
        if new_score > scores[i]:
            scores[i + 2] = scores[i + 1]
            scores[i + 3] = scores[i + 2]
            scores[i + 4] = scores[i + 3]
            scores[i] = new_score

    print("New best scores:")

    for i in range(5):
        score = total_score.readline(i)
        scores.append(score)
        print("Score ", (i + 1), "is", score)

    print(scores)
    

    pickle.dump(scores, total_score, True)
                     
    total_score.close

def fake():
    fake_scores = open("total_score.dat", "ab")
    scores = ["0", "0", "0", "0", "0"]
    pickle.dump(scores, fake_scores, True)
    fake_scores.close()
 
def main():
    trivia_file = open_file("kwiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    fake()

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
