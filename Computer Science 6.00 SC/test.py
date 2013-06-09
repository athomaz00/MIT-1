from random import *

class Card(object):

    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["C","D","H","S"]

    def __init__(self, rank, suit):
             self.rank = rank
             self.suit = suit
    def __str__(self):
             rep = self.rank + self.suit
             return rep

      
class Deck(object) :

    def __init__(self):     
        self.cards=[]

    def __str__(self): 
            if self.cards:
                rep=""
                for card in self.cards:
                    rep += str(card) + " "
            else:
                rep= "Empty"
            return rep
        
    def addCard(self,card) : 
        self.cards.append(card)         

    def populate(self):    
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.addCard(Card(rank,suit))
        
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def removeCard(self, card1):
        for card in self.cards:
            if card.rank == card1.rank and card.suit == card1.suit:
                self.cards.remove(card)


    def isEmpty(self):
        if self.cards == []:
            return 1

    
    def deal(self, hands, nCards=999): 
          nHands = len(hands) 
          for i in range(nCards): 
            if self.isEmpty():
                  break      # break if out of cards 
            else:
                card = self.cards[0]
                print card
                hand = hands[i % nHands]
                print i
                hand.addCard(card)
                self.removeCard(card)

    def printHands(self):
           print self

class Hand(Deck): 

    def __init__(self, name=""): 
        self.cards = [] 
        self.name = name

    def __str__(self): 
            s = "Hand " + self.name 
            if self.isEmpty(): 
              return s + " is empty\n" 
            else: 
              return s + " contains\n" + Deck.__str__(self)
            
    def addCard(self,card) : 
        self.cards.append(card)         
            
    def printHands(self):
           print self
           
class CardGame: 

           
   def __init__(self):
       
    self.deck = Deck()
    print(self.deck)
    self.deck.populate()
    print(self.deck)
    self.deck.shuffle()

    def printHands(self, names):
        for name in names:
            print "Hand " + name+ " contains"
            print OldMaidHand(name)

class OldMaidGame(CardGame): 

    def printHands(self, names):
       for name in names:
           print "Hand " + name+ " contains"
           print OldMaidHand(name)

    def removeAllMatches(self): 
        count = 0 
        for hand in self.hands: 
          count = count + hand.removeMatches() 
        return count

    def playOneTurn(self, i): 
        if self.hands[i].isEmpty(): 
          return 0 
        neighbor = self.findNeighbor(i) 
        pickedCard = self.hands[neighbor].popCard() 
        self.hands[i].addCard(pickedCard) 
        print "Hand", self.hands[i].name, "picked", pickedCard 
        count = self.hands[i].removeMatches() 
        self.hands[i].shuffle() 
        return count

    def play(self, names):
        # remove Queen of Clubs
        card1 = Card("Q","C")
        print card1
        self.deck.removeCard(card1)
        print "Queen of Clubs removed."
        print self.deck

        # make a hand for each player 
        self.hands = [] 
        for name in names : 
            self.hands.append(OldMaidHand(name))
            self.printHands(names)

        # deal the cards 
        print (self.deck)
        self.deck.deal(self.hands,51)
        print "---------- Cards have been dealt" 
        self.printHands(self.hands) 

        # remove initial matches 
        matches = self.removeAllMatches() 
        print "---------- Matches discarded, play begins" 
        self.printHands(names)
        

        # play until all 50 cards are matched 
        turn = 0 
        numHands = len(self.hands) 
        while matches < 25: 
          matches = matches + self.playOneTurn(turn) 
          turn = (turn + 1) % numHands 

        print "---------- Game is Over" 
        self.printHands(names)
    
class OldMaidHand(Hand): 

  def removeMatches(self): 
    count = 0 
    originalCards = self.cards[:] 
    for card in originalCards: 
      match = Card(3 - card.suit, card.rank) 
      if match in self.cards: 
        self.cards.removeCard(card) 
        self.cards.remove(match) 
        print "Hand %s: %s matches %s" % (self.name,card,match) 
        count = count + 1 
    return count




game = OldMaidGame()
game.play(["Allen","Jeff","Chris"]) 
