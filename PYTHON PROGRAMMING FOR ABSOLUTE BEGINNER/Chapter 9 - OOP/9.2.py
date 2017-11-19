# Card game - War

class Card(karty.Card):
    # War game card

    @property
    def value(self):
        v = Card.RANKS.index(self.rank) + 1
        return v

class Hand(karty.Card):
    def __init__(self, name):
        
    
        
        
