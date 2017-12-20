#Simple adventure text game
#Player can move between various locations
#NOT FINISHED


import gry

class player(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        rep = ""
        rep += self.name
        return rep

class Forest(player):
    def choice(self):
        print("You entered mysterious Forest", self.name, "from the distance you can see small cabine, \
dark cave and dirty lake")
        yesno = gry.ask_yes_no("Would you like to discover this place or step back? (t for Yes / n for No)")
        choice = ""
        if yesno == "t":
            choice = input("Where do you want to go (cabine / cave / lake)").lower()
            while choice not in ("cabine", "cave", "lake"):
                choice = input("Where do you want to go (cabine / cave / lake)").lower()
            return choice
        else:
            choice = "back"
            return choice
        
    def cabine(self):
        print("It is dark and scary place. Something bad happened here...")
        yesno = gry.ask_yes_no("Would you like to check different places in the forest or step back? \
(t for Yes / n for No)")
        choice = ""
        if yesno == "t":
            choice = input("Where do you want to go (cave / lake)").lower()
            while choice not in ("cave", "lake"):
                choice = input("Where do you want to go (cave / lake)").lower()
            return choice
        else:
            choice = "back"
            return choice
        
    def cave(self):
        print("There are a lot of rats and spiders in here...")
        yesno = gry.ask_yes_no("Would you like to check different places in the forest or step back? \
(t for Yes / n for No)")
        choice = ""
        if yesno == "t":
            choice = input("Where do you want to go (cabine / lake)").lower()
            while choice not in ("cabine", "lake"):
                choice = input("Where do you want to go (cabine / lake)").lower()
            return choice
        else:
            choice = "back"
            return choice
        
    def lake(self):
        print("You can notice few dead fishes in the dirty water...")
        yesno = gry.ask_yes_no("Would you like to check different places in the forest or step back? \
(t for Yes / n for No)")
        choice = ""
        if yesno == "t":
            choice = input("Where do you want to go (cave / cabine)").lower()
            while choice not in ("cave", "lake"):
                choice = input("Where do you want to go (cave / cabine)").lower()
            return choice
        else:
            choice = "back"
            return choice

class Desert(player):
    def choice(self):
        print("You entered big desert", self.name, "from the distance you can see Oaza, \
deadly tomb and large piramid")
        yesno = gry.ask_yes_no("Would you like to discover this place or step back? (t for Yes / n for No)")
        choice = ""
        if yesno == "t":
            choice = input("Where do you want to go (oaza / tomb / piramid)").lower()
            while choice not in ("oaza", "tomb", "piramid"):
                choice = input("Where do you want to go (oaza / tomb / piramid)").lower()
            return choice
        else:
            choice = "back"
            return choice

    def oaza(self):
        print("Finally you can rest, drink water and eat fruity fruit")
        yesno = gry.ask_yes_no("Would you like to check different places in the desert or step back? \
(t for Yes / n for No)")
        choice = ""
        if yesno == "t":
            choice = input("Where do you want to go (tomb / piramid)").lower()
            while choice not in ("tomb", "piramid"):
                choice = input("Where do you want to go (tomb / piramid)").lower()
            return choice
        else:
            choice = "back"
            return choice
        
    def tomb(self):
        print("Someone died in here...")
        yesno = gry.ask_yes_no("Would you like to check different places in the desert or step back? \
(t for Yes / n for No)")
        choice = ""
        if yesno == "t":
            choice = input("Where do you want to go (oaza / piramid)").lower()
            while choice not in ("oaza", "piramid"):
                choice = input("Where do you want to go (oaza / piramid)").lower()
            return choice
        else:
            choice = "back"
            return choice

    def piramid(self):
        print("Another graveyard, let's better go outside.")
        yesno = gry.ask_yes_no("Would you like to check different places in the desert or step back? \
(t for Yes / n for No)")
        choice = ""
        if yesno == "t":
            choice = input("Where do you want to go (oaza / tomb)").lower()
            while choice not in ("oaza", "tomb"):
                choice = input("Where do you want to go (oaza / tomb)").lower()
            return choice
        else:
            choice = "back"
            return choice
        
class Mountains(player):
    def choice(self):
        print("You entered big mountains.", self.name, "from the distance you can see really high peak, \
mountain lake and big cliff")
        yesno = gry.ask_yes_no("Would you like to discover this place or step back? (t for Yes / n for No)")
        choice = ""
        if yesno == "t":
            choice = input("Where do you want to go (peak / lake / cliff)").lower()
            while choice not in ("peak / lake / cliff"):
                choice = input("Where do you want to go (peak / lake / cliff)").lower()
            return choice
        else:
            choice = "back"
            return choice
        
    def peak(self):
        print("The view is really nice, you can see the enviroment is very peacefull.")
        yesno = gry.ask_yes_no("Would you like to check different places in the mountains or step back? \
(t for Yes / n for No)")
        choice = ""
        if yesno == "t":
            choice = input("Where do you want to go (lake / cliff)").lower()
            while choice not in ("cave", "lake"):
                choice = input("Where do you want to go (lake / cliff)").lower()
            return choice
        else:
            choice = "back"
            return choice

    def lake(self):
        print("Clear and blue water reminds you your childhood and fishing with your grandpa.")
        yesno = gry.ask_yes_no("Would you like to check different places in the mountains or step back? \
(t for Yes / n for No)")
        choice = ""
        if yesno == "t":
            choice = input("Where do you want to go (peak / cliff)").lower()
            while choice not in ("cave", "lake"):
                choice = input("Where do you want to go (peak / cliff)").lower()
            return choice
        else:
            choice = "back"
            return choice

    def cliff(self):
        print("Watch out, if you would fall down here, our mission would be finished.")
        yesno = gry.ask_yes_no("Would you like to check different places in the mountains or step back? \
(t for Yes / n for No)")
        choice = ""
        if yesno == "t":
            choice = input("Where do you want to go (peak / lake)").lower()
            while choice not in ("cave", "lake"):
                choice = input("Where do you want to go (peak / lake)").lower()
            return choice
        else:
            choice = "back"
            return choice

class crossroad(object):
    def menu(self, player):
        forest = Forest(player)
        desert = Desert(player)
        mountains = Mountains(player)

        finish = gry.ask_yes_no("Would you like to finish the game? (t for Yes / n for No)")
        decision = ""
        while finish != "t":
            while decision not in ("desert", "forest", "mountains"):
                decision = input("Where would you like to go? (desert / forest / mountains)")
            choice = ""
            while choice != "back":
                choice = ""
                if decision == "desert":
                    choice = desert.choice()
                    if choice == "oaza":
                        choice = desert.oaza()
                    elif choice == "piramid":
                        choice =desert.piramid()
                    elif choice == "tomb":
                        choice =desert.tomb()
                    decision == ""
                elif decision == "forest":
                    choice = forest.choice()
                    if choice == "cabine":
                        choice =forest.cabine()
                    elif choice == "cave":
                        choice =forest.cave()
                    elif choice == "lake":
                        choice =forest.lake()
                    decision == ""
                elif decision == "mountains":
                    choice = mountains.choice()
                    if choice == "cliff":
                        mountains.cliff()
                    elif choice == "peak":
                        mountains.peak()
                    elif choice == "lake":
                        mountains.lake()
                    decision == ""
                decision = ""
            finish = gry.ask_yes_no("Would you like to finish the game? (t for Yes / n for No)")
                
                    

        
class game(object):
    print("You woke up in the destroyed car on the crossroad. You don't remember anything.")
    name = input("What is your name traveler? ")
    player = player(name)
    print("The crossroad directs to the three places: forest, desert and mountains.")
    crossroad = crossroad()
    crossroad.menu(player)

game()
                     
                         
                         
        




























    
    
