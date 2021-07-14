import random
SUITS = ["DIAMONDS", "SPADES", "HEARTS", "CLUBS"]
VALUES = ["ACE", "TWO" , "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]

class Card:

    # Card constructor
    def __init__(self, suit, val):
        self.suit= suit
        self.val = val
    
    # Returns the suit of the card.
    def suit(self):
        return self.suit
    
    # Returns the value of the card.
    def value(self):
        return list(self.val)
        
class Deck:
   
    # Creates a sorted deck of playing cards. 13 values, 4 suits.
    def __init__(self,card):
        self.deck = []
        self.card = card
        
    def build(self):
        su = self.card.suit
        va = self.card.value()
        for s in su:
            for v in va:
                ace_clubs = v + " Of " + s
                self.deck.append(ace_clubs)
        
        
    # Returns the number of Cards in the Deck
    def num_cards(self):
        return len(self.deck)
    
    # Shuffles the deck of cards.
    def shuffle(self):
        return random.shuffle(self.deck)
    
    # Returns the top Card in the deck, then puts it back.
    def peek(self):
        top_card = self.deck.pop()
        self.deck.append(top_card)
        return top_card
    
    # Draws and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self):
        return self.deck.pop()
    
    # Adds the input card to the deck. If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card):
        if(len(self.deck)>=52):
            print("Cannot add anymore")
        else:
            self.deck.append(card)
    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self):
        print(self.deck)

c = Card(SUITS, VALUES)
obj = Deck(c)
obj.build()
print("DISPLAYING THE DECK: ")
obj.print_deck()
print("NUMBER OF CARDS: ")
print(obj.num_cards())
print("SHUFFLING THE DECK....")
obj.shuffle()
print("PEEKING THE TOP CARD AND PUTTING IT BACK")
print(obj.peek())
print("ADDING A NEW CARD..")
obj.add_card("TWO OF CLUBS")
print("DRAWING THE TOP CARD")
print(obj.draw())
print("ADDING A NEW CARD..")
obj.add_card("TWO OF CLUBS")
print("DISPLAYING THE DECK: ")
obj.print_deck()
