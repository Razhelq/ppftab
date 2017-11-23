#Simple adventure text game
#Player can move between various locations
#NOT FINISHED


import gry

class Forest(object):
    def __str__(self, player):
        print("You entered mysterious Forest", self.player, "from the distance you can see small cabine, \
dark cave and dirty lake")
        yesno = gry.ask_yes_no("Would you like to discover this place or step back? (t for Yes / n for No)")
        choice = "back"
        if yesno == "t":
            choice = input("Where do you want to go (cabine / cave / lake)").lower()
            while choice not in ("cabine", "cave", "lake"):
                choice = input("Where do you want to go (cabine / cave / lake)").lower()
            return choice
        else:
            return choice
        
    def Cabine(self, player):
        print("It is dark and scary place. Something bad happened here...")
        yesno = gry.ask_yes_no("Would you like to check different places in the forest or step back? \
(t for Yes / n for No)")
        choice = "back"
        if yesno == "t":
            choice = input("Where do you want to go (cave / lake)").lower()
            while choice not in ("cave", "lake"):
                choice = input("Where do you want to go (cave / lake)").lower()
            return choice
        else:
            return choice
        
    def Cave(self):
        print("There are a lot of rats and spiders in here...")
        yesno = gry.ask_yes_no("Would you like to check different places in the forest or step back? \
(t for Yes / n for No)")
        choice = "back"
        if yesno == "t":
            choice = input("Where do you want to go (cabine / lake)").lower()
            while choice not in ("cabine", "lake"):
                choice = input("Where do you want to go (cabine / lake)").lower()
            return choice
        else:
            return choice
        
    def Lake(self):
        print("You can notice few dead fishes in the dirty water...")
        yesno = gry.ask_yes_no("Would you like to check different places in the forest or step back? \
(t for Yes / n for No)")
        choice = "back"
        if yesno == "t":
            choice = input("Where do you want to go (cave / cabine)").lower()
            while choice not in ("cave", "lake"):
                choice = input("Where do you want to go (cave / cabine)").lower()
            return choice
        else:
            return choice        

class Desert(object):
     def __str__(self, player):
        print("You entered big desert", self.player, "from the distance you can see Oaza, \
deadly tomb and large piramid")
        yesno = gry.ask_yes_no("Would you like to discover this place or step back? (t for Yes / n for No)")
        choice = "back"
        if yesno == "t":
            choice = input("Where do you want to go (oaza / tomb / piramid)").lower()
            while choice not in ("cabine", "cave", "lake"):
                choice = input("Where do you want to go (oaza / tomb / piramid)").lower()
            return choice
        else:
            return choice
    def Oaza(self):
        print("Finally you can rest, drink water and eat fruity fruit")
        yesno = gry.ask_yes_no("Would you like to check different places in the forest or step back? \
(t for Yes / n for No)")
        choice = "back"
        if yesno == "t":
            choice = input("Where do you want to go (tomb / piramid)").lower()
            while choice not in ("cave", "lake"):
                choice = input("Where do you want to go (tomb / piramid)").lower()
            return choice
        else:
            return choice
    def Tomb(self):
        print("Someone died in here...")
        yesno = gry.ask_yes_no("Would you like to check different places in the forest or step back? \
(t for Yes / n for No)")
        choice = "back"
        if yesno == "t":
            choice = input("Where do you want to go (oaza / piramid)").lower()
            while choice not in ("cave", "lake"):
                choice = input("Where do you want to go (oaza / piramid)").lower()
            return choice
        else:
            return choice

    def Piramid(self):
        print("Another graveyard, let's better go outside.")
        yesno = gry.ask_yes_no("Would you like to check different places in the forest or step back? \
(t for Yes / n for No)")
        choice = "back"
        if yesno == "t":
            choice = input("Where do you want to go (oaza / tomb)").lower()
            while choice not in ("cave", "lake"):
                choice = input("Where do you want to go (oaza / tomb)").lower()
            return choice
        else:
            return choice
        
class Desert(object):
    def Peak(self):

    def Lake(self):

    def Cliff(self):

class game(object):
    
