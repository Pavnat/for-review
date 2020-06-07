#CARD PARAMETERS
import random
from IPython.display import clear_output

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

decision = ""

class Card:
    
    def __init__(self,suit,rank):        
        self.suit = suit
        self.rank = rank
    
    def __str__(self):        
        return self.rank+" of "+self.suit

class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: "+deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0  
        self.aces = 0    
        
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_for_ace(self):
        if self.aces and self.value > 21:
            self.value -= 10
            self.aces -= 1
            
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

deck = Deck()
dealerhand = Hand()
playerhand = Hand()
bank = Chips()

def take_bet():
    while True:
        try:
            bank.bet = int(input("How much would you like to bet?"))
        except:
            print("Please write a numerical value")
            continue
        else:
            if bank.bet > bank.total:
                print(f"You have not enough chips")
                continue
            elif bank.bet < 1:
                print("Minimal bet is 1")
                continue
            else:
                break

def print_cards(player,dealer):
    clear_output()
    print("\nYOUR HAND: ", *playerhand.cards, sep='\n')
    print("\nDEALER'S HAND:")
    for card in dealerhand.cards:
        print(card)
def game_start():

    if bank.total == 0:
        bank.total = 100
    
    print(f'You have {bank.total} chips.')
    take_bet()
    game_round()

def checker():
    if (dealerhand.value>playerhand.value and dealerhand.value<22):
        print("------YOU LOSE------")
        bank.lose_bet()
    elif playerhand.value==dealerhand.value:
        print("------TIE------")
    elif dealerhand.value<playerhand.value or dealerhand.value>21:
        print("------YOU WIN------")
        bank.win_bet()

def hit(hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    print_cards(playerhand.cards,dealerhand.cards)

def game_round(): 
    global decision
    dealerhand.cards = []  
    dealerhand.value = 0  
    dealerhand.aces = 0 
    playerhand.cards = []  
    playerhand.value = 0  
    playerhand.aces = 0
    deck = Deck()
    deck.shuffle()
    playerhand.add_card(deck.deal())
    dealerhand.add_card(deck.deal())
    playerhand.add_card(deck.deal())
    
    print_cards(playerhand.cards,dealerhand.cards)
    
    while True:
        try:
            decision = input("\nPlease write H, to hit another card, or S, to stay").upper()
            if decision == 'QUIT':
                break
            elif decision == "H":
                hit(playerhand)
                if playerhand.value > 21:
                    print('------YOU LOSE------')
                    bank.lose_bet()
                    break
                continue
            elif decision == "S":
                while dealerhand.value<17:
                    hit(dealerhand)
                checker()
                break
            else:
                print("What now?")
        except:
            continue
    if decision == "QUIT":
         print('Thanks for playing')
    else:
        if bank.total < 1:
            print("You are out of chips. Bye")
        else:
            game_start()

game_start()