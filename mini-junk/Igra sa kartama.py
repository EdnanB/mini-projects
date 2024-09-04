import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} od {self.suit}"

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Srce', 'Karo', 'Tref', 'Pik']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)  

    def deal(self, num_cards):
        if num_cards <= len(self.cards):
            return [self.cards.pop() for _ in range(num_cards)]
        else:
            return "Nema dovoljno karata za dijeljenje."

    def return_cards(self, returned_cards):
        self.cards.extend(returned_cards)
        random.shuffle(self.cards) 

    def __str__(self):
        return f"Spil od {len(self.cards)} karte"

def choose_cards_to_discard(hand):
    cards_to_discard = []
    while True:
        card_index = input("Unesite redni broj karte koju zelite odbaciti (ili 'kraj' za kraj): ")
        if card_index.lower() == 'kraj':
            break
        try:
            card_index = int(card_index)
            if 1 <= card_index <= len(hand) and card_index not in cards_to_discard:
                cards_to_discard.append(card_index)
            else:
                print("Nevazeci redni broj karte ili vec odabrana karta.")
        except ValueError:
            print("Nevazeci unos. Molimo unesite cijeli broj ili 'kraj' za zavrsetak odabira.")
    return cards_to_discard

deck = Deck()

hand = deck.deal(5)
print("Trenutna ruka:")
for card in hand:
    print(card)

change_cards = input("Zelite li zamijeniti neke karte (da/ne)? ").lower()
if change_cards == 'da':
    cards_to_discard = choose_cards_to_discard(hand)
    cards_to_keep = []
    index = 1
    for card in hand:
        if index not in cards_to_discard:
            cards_to_keep.append(card)
        index += 1
    
    discarded_cards = [hand[i - 1] for i in cards_to_discard]
    
    deck.return_cards(discarded_cards)
    
    new_cards = deck.deal(len(discarded_cards))
    hand = cards_to_keep + new_cards

print("Nova ruka:")
for card in hand:
    print(card)
