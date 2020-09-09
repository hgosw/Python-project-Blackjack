import random


suits =('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
from IPython.display import clear_output

class Card:
    
    def __init__(self,suits,rank):
        self.suits = suits 
        self.rank = rank
        

    def __str__(self):
        return self.rank +' of '+ self.suits





class Deck:
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                created_card= Card(suit,rank)
                self.deck.append(created_card)
    
    def __str__(self):
        for i in self.deck:
            print(i.suits, i.rank)

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()






class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces+=1
    def __str__(self):
        print(*self.cards,sep='\n')

    def adjust_for_ace(self):
        while self.value >21 and self.aces:
            self.value -=10
            self.aces -=1
        







class Chips:
    
    def __init__(self):
        self.total = 100 
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter bet amount: "))
        except ValueError:
            print('Enter a number!')
        else:
            if  chips.bet > chips.total:
                print("Enter a NUMBER! less or equal to Total amount")
            else:
                break


def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing 
    while True:
        
        z = input("Enter Hit or Stand 'h' or 's': ")

        if z[0].lower() == "h":
            hit(deck,hand)
        elif z[0].lower() == "s":
            print("Player stands!")
            playing = False
        else:
            print("Please enter 'h' or 's'!")
            continue 
        break




def show_some(player,dealer):
    print("\nDealers hand: ")
    print(dealer.cards[1],"\nHidden card")
    print("\nPlayers hand: ")
    print('\t',player.value,*player.cards, sep='\n')
    
    
def show_all(player,dealer):
    print("\nDealers hand:")
    print('\n',dealer.value ,*dealer.cards,sep='\n')
    print("\nPlayers hand:")
    print('\n',player.value ,*player.cards,sep='\n')





def player_busts(player,dealer,chips):
    print("Player Busts")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player wins!')
    chips.win_bet()
    

def dealer_busts(player,dealer,chips):
    print('Dealer Busts!')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print('Dealer wins!')
    chips.lose_bet()
    
    
def push(player,dealer):
    if player.value == dealer.value:
        print('Push!')




while True:
    
    clear_output()
    print("Welcome to black jack")
    playing = True
    
   
    d = Deck()
    d.shuffle()
    ply = Hand()        
    ply.add_card(d.deal())
    ply.add_card(d.deal())
    
    deal = Hand()        
    deal.add_card(d.deal())
    deal.add_card(d.deal())
        
    
    ply_chip = Chips()
    deal_chip = Chips()
    
    
    take_bet(ply_chip)
    
    show_some(ply,deal)
    
    while playing:
        
        
        hit_or_stand(d,ply)
        clear_output()
        
        
        show_some(ply,deal)
        
        
        if ply.value > 21:
            clear_output()
            player_busts(ply,deal,ply_chip)
            break

    
    if ply.value <22:
        clear_output()
        while deal.value <=17:
            
            hit(d,deal)
            if deal.value > 21:
                clear_output()
                dealer_busts(ply,deal,ply_chip)
                
                
    
        
    show_all(ply,deal)
    
    if ply.value == 21:
        print('\n')
        player_wins(ply,deal,ply_chip)

    elif deal.value > ply.value and deal.value < 22:
        print('\n')
        dealer_wins(ply,deal,ply_chip)
    
    elif ply.value > deal.value and ply.value < 22:
        print('\n')
        player_wins(ply,deal,ply_chip)
    
    elif deal.value == ply.value:
        clear_output()
        show_all(ply,deal)
        print('\n')
        push(ply,deal)
    
    
    print(f"\nPlayers chips {ply_chip.total}")
    
    g = input("Would you like to play again 'y'or 'n'")
    if g == 'y':
          continue 
    else:
          break
            












