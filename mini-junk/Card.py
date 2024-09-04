class Card:
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def pay(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Iznos od {amount} je uspjesno placen. Novo stanje na kartici: {self.balance}.")
        else:
            print("Nemate dovoljno sredstava na kartici.")

class Visa(Card):
    def __init__(self, number, balance):
        super().__init__(number, balance)

    def pay(self, amount):
        tax = amount * 0.05
        total_amount = amount + tax
        if total_amount <= self.balance:
            self.balance -= total_amount
            print(f"Iznos od {amount} je uspjesno placen (ukljucujuci porez). Novo stanje na kartici: {self.balance}.")
        else:
            print("Nemate dovoljno sredstava na kartici.")

class Master(Card):
    def __init__(self, number, balance):
        super().__init__(number, balance)

    def pay(self, amount):
        tax = amount * 0.08
        total_amount = amount + tax
        if total_amount <= self.balance:
            self.balance -= total_amount
            print(f"Iznos od {amount} je uspjesno placen (ukljucujuci porez). Novo stanje na kartici: {self.balance}.")
        else:
            print("Nemate dovoljno sredstava na kartici.")


visa_card = Visa("123456789", 500)
amount = int(input("Molimo unesite cijenu: "))
master_card = Master("987654321", 500)
visa_card.pay(amount)
master_card.pay(amount)
