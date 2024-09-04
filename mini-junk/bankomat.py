import time

class Card:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        

class Bankomat:
    def __init__(self):
        self.card = None
        print("Molimo stavite karticu u bankomat.")
    def set_card(self, card):
        self.card = card
        print("Kartica uspjesno stavljena. Let's proceed...")
        time.sleep(2)
    def withdraw(self, suma):
        if self.card is None:
            print("Greška: Kartica nije ubačena u bankomat.")
        elif suma > self.card.balance:
            print("Greška: Nedovoljno sredstava na kartici.")
        else:
            self.card.balance -= suma
            print(f"Izvadili ste {suma} KM sa kartice {self.card.name}. Novo stanje: {self.card.balance} KM.")

kartica = Card("Visa", 100)
bankomat = Bankomat()
time.sleep(2)

bankomat.set_card(kartica)
balance = int(input("Molimo unesite vas zeljeni iznos: "))
bankomat.withdraw(balance)  


