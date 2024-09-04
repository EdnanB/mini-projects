class BankAccount:
    def __init__(self, broj_racuna, ime_vlasnika, pocetno_stanje=0):
        self.broj_racuna = broj_racuna
        self.ime_vlasnika = ime_vlasnika
        self.stanje = pocetno_stanje
        self.transakcije = []

    def uplata(self, iznos):
        if iznos <= 0:
            print("Unesite ispravan iznos za uplatu.")
            return
        self.stanje += iznos
        self.transakcije.append(f"Uplata: +{iznos} KM")

    def isplata(self, iznos):
        if iznos <= 0:
            print("Unesite ispravan iznos za isplatu.")
            return
        if iznos > self.stanje:
            print("Nemate dovoljno novca na racunu.")
            return False 
        else:
            self.stanje -= iznos
            self.transakcije.append(f"Isplata: -{iznos} KM")
            return True  

    def prikazi_stanje(self):
        print(f"Trenutno stanje na racunu ({self.broj_racuna}), vlasnik: {self.ime_vlasnika}: {self.stanje} KM")

    def prikazi_transakcije(self):
        print(f"Transakcije za racun broj {self.broj_racuna}, vlasnik: {self.ime_vlasnika}:")
        for transakcija in self.transakcije:
            print(transakcija)


racun = BankAccount("123456789", "Ednan")
racun.prikazi_stanje()

while True:
    unos_depozita = input("Unesite iznos za uplatu: ")
    try:
        unos_depozita = float(unos_depozita)
        racun.uplata(unos_depozita)
        racun.prikazi_stanje()
        break
    except ValueError:
        print("Molimo unesite ispravan broj.")

while True:
    odgovor = None
    while True:
        unos_isplate = input("Unesite iznos za isplatu: ")
        try:
            unos_isplate = float(unos_isplate)
            uspjesna_isplata = racun.isplata(unos_isplate)
            racun.prikazi_stanje()
            if not uspjesna_isplata:
                break
            else:
                odgovor = input("Želite li nastaviti s transakcijama? (da/ne): ")
                if odgovor.lower() == "ne":
                    break
                elif odgovor.lower() == "da":
                    break
                else:
                    print("Molimo unesite 'da' ili 'ne'.")
        except ValueError:
            print("Molimo unesite ispravan broj.")

    if odgovor is None or odgovor.lower() == "ne":
        break

racun.prikazi_transakcije()