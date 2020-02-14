import random
from itertools import product
class Deck():
    suit = ('kypa', 'pika', 'karo', 'spatiq')
    ranks = ('dve', 'tri', 'chetiri', 'pet', 'shest', 'sedem', 'osem',
             'devet', 'deset', 'vale', 'dama', 'popa', 'asak')
    values = {'dve':2, 'tri':3, 'chetiri':4, 'pet':5, 'shest':6, 'sedem':7,
             'osem':8,'devet':9, 'deset':10, 'vale':11,
             'dama':12, 'popa':13, 'asak':1,}
    def __init__(self):
        self.deck1 = list(product(Deck.suit,Deck.ranks))
        random.shuffle(self.deck1)
    def draw_card(self):
        if len(self.deck1) == 0:
            return 0
        else:
            return self.deck1.pop()
    def shuffle_deck(self):
        random.shuffle(self.deck1)
    def __str__(self):
        return str(self.deck1)

class Card(Deck):
    def __init__(self,deck):
        self.card = deck.draw_card()
        if self.card == 0:
            raise Exception('Vsichki karti sa razdadeni')
        self.suit = self.card[0]
        self.rank = self.card[1]
        self.value = self.values[self.rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    def getval(self):
        return self.value  
    
def self_val():
    a = int(input('Vuvedi chislo: \n'))
    if not a in range(1,201):
        print('Vuvedi chislo ot 1 do 200')
        exit()
    b = random.randint(1,200)
    return a,b

def game(lst,deck):
    lst.append(Card(deck))
    return lst[-1].value

player,computer = self_val()
pcount,ccount = 0,0

pllst = []
cmplst = []
dec = Deck()

while True:
    try:
        pcount += game(pllst,dec)
        if pcount == player:
            print(f'Ti specheli!!!!')
            break
        ccount += game(cmplst,dec)
        if ccount == computer:
            print(f'Ti zagubi, nomera na kompiutura e{computer}')
            break

    except Exception:
        if pcount > ccount:
            print(f'Ti specheli, tvoq rezultat {pcount} e \
po-visok ot tozi na kompiutura {ccount}')
        else:
            print(f'Ti zagubi, tvoq rezultat {pcount} e \
po-nisuk ot tozi na kompiutura {ccount}')
        break
