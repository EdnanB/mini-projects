class Car:
    def __init__(self, marka, model, godina, kilometri=0, stanje='iskljucen'):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina
        self.predjeni_kilometri = kilometri
        self.stanje = stanje

    def pokreni_auto(self):
        if self.stanje == 'ukljucen':
            print("Automobil je vec pokrenut.")
        else:
            self.stanje = 'ukljucen'
            print("Automobil je uspjesno pokrenut.")

    def zaustavi_auto(self):
        if self.stanje == 'iskljucen':
            print("Automobil je vec zaustavljen.")
        else:
            self.stanje = 'iskljucen'
            print("Automobil je uspjesno zaustavljen.")

    def trenutno_stanje(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Predjeni kilometri: {self.predjeni_kilometri}, Stanje: {self.stanje}")


vozila = []


while True:
    marka = input("Unesite marku automobila (ili 'kraj' za zavrsetak unosa): ")
    if marka.lower() == 'kraj':
        break
    model = input("Unesite model automobila: ")
    godina = input("Unesite godinu proizvodnje automobila: ")
    kilometri = float(input("Unesite broj predjenih kilometara: "))
    
    auto = Car(marka, model, godina, kilometri)
    vozila.append(auto)


print("Dostupna vozila:")
for i in range(len(vozila)):
    print(f"{i + 1}. {vozila[i].marka} {vozila[i].model}")


odabrana_vozila = input("Unesite brojeve vozila za prikaz informacija (razdvojene razmakom): ").split()


for broj in odabrana_vozila:
    try:
        index = int(broj) - 1
        odabrano_vozilo = vozila[index]
        odabrano_vozilo.trenutno_stanje()
        print()
    except (ValueError, IndexError):
        print(f"Vozilo sa rednim brojem {broj} nije pronadjeno.")


for broj in odabrana_vozila:
    try:
        index = int(broj) - 1
        odabrano_vozilo = vozila[index]
        odabrano_vozilo.pokreni_auto()
        odabrano_vozilo.trenutno_stanje()
        
        odabrano_vozilo.zaustavi_auto()
        odabrano_vozilo.trenutno_stanje()
        print()
    except (ValueError, IndexError):
        print(f"Vozilo sa rednim brojem {broj} nije pronadjeno.")
