# Simplified Card game - War

import karty, gry

class Card(karty.Card):
    # War game card

    ACE_VALUE = 1
    
    @property
    def value(self):
        v = Card.RANKS.index(self.rank) + 1
        return v


class Deck(karty.Deck):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(rank, suit))


class Hand(karty.Hand):
    def __init__(self, name):
        super(Hand, self).__init__()
        self.name = name

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        t = 0
        for card in self.cards:
            t += card.value

        contains_ace = False
        for card in self.cards:
            if card.value == Card.ACE_VALUE:
                t += 13

        return t
            
class Player(Hand):
    def lose(self):
        print(self.name , "lose.")

    def win(self):
        print(self.name , "win.")


class Game(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            player = Player(name)
            self.players.append(player)

        self.deck = Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        self.deck.deal(self.players, per_hand = 1)
        
        scores = []
        for player in self.players:
            print(player, player.name, player.total)
            scores.append([player.total, player.name])    

        scores.sort(reverse = True)

        print(scores[0][1], "won with score: ", scores[0][0])

        for player in self.players:
            if player.name == scores[0][1]:
                player.win()
            else:
                player.lose()
        

def main():
    print("Welcome in to the War game")
    names = []
    number = gry.ask_number("How many players (1 - 10: ", low = 1, high = 10)
    for i in range(number):
        name = input("Name of the player: ")
        names.append(name)
        
    game = Game(names)
    
    again = None
    while again != "n":
        game.play()
        again = gry.ask_yes_no("\Do you wanna play again? Type 't' for yes or 'n' for no.")

main()
input("Press any key to finish the game.")
    
        

        

        
