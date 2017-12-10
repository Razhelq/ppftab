# The material form the book in polish

# Opiekun zwierzaka
# Wirtualny pupil, którym należy się opiekować

class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        rep = "The valuse of your pet:\n"
        rep += "The hunger = " + str(self.hunger)
        rep += "\nThe boredom = " + str(self.boredom)
        return rep

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęśliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "podenerwowany"
        else:
            m = "wściekły"
        return m
    
    def talk(self):
        print("Nazywam się", self.name, "i jestem", self.mood, "teraz.\n")
        self.__pass_time()
    
    def eat(self, food = 4):
        print("""
How much food would you like to serve to you pet?
\n 1. Type 1 for one snack.
\n 2. Type 2 for 2 snacks.
\n 3. Type 3 for 3 snacks.
\n 4. Type 4 for 4 snacks.
\n 5. Type 5 for 5 snacks.
""", end = " ")
        food = int(input("Wybierasz: "))
        print("Mniam, mniam.  Dziękuję.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("""
How log would you like to play with your pet?
\n 1. Type 1 for one minute.
\n 2. Type 2 for 2 minutes.
\n 3. Type 3 for 3 minutes.
\n 4. Type 4 for 4 minutes.
\n 5. Type 5 for 5 minutes.
""", end = " ")
        fun = int(input("Wybierasz: "))
        print("Hura!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Jak chcesz nazwać swojego zwierzaka?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Opiekun zwierzaka
    
        0 - zakończ
        1 - słuchaj swojego zwierzaka
        2 - nakarm swojego zwierzaka
        3 - pobaw się ze swoim zwierzakiem
        4 - show the values of your pet
        """)
    
        choice = input("Wybierasz: ")
        print()

        # wyjdź z pętli 
        if choice == "0":
            print("Do widzenia.")

        # słuchaj swojego zwierzaka
        elif choice == "1":
            crit.talk()
        
        # nakarm swojego zwierzaka
        elif choice == "2":
            crit.eat()
         
        # pobaw się ze swoim zwierzakiem
        elif choice == "3":
            crit.play()

        elif choice == "4":
            print(crit)

        # nieznany wybór 
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.") 
