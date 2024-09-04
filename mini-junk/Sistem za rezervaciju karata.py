class Ticket:
    def __init__(self, dogadjaj, datum, cijena, dostupnost, broj_karata):
        self.dogadjaj = dogadjaj
        self.datum = datum
        self.cijena = cijena
        self.dostupnost = dostupnost
        self.broj_karata = broj_karata

    def prikazi_informacije(self):
        print(f"Dogadjaj: {self.dogadjaj}")
        print(f"Datum: {self.datum}")
        print(f"Cijena: {self.cijena} KM")
        print(f"Dostupnost: {'Dostupno' if self.dostupnost else 'Nedostupno'}")
        print(f"Broj dostupnih karata: {self.broj_karata}")
        print()

class TicketSystem:
    def __init__(self):
        self.karte = []

    def dodaj_kartu(self, karta):
        self.karte.append(karta)
        print(f"Karta za dogadjaj '{karta.dogadjaj}' je dodana.")

    def pretrazi_karte(self, dogadjaj=None):
        if dogadjaj:
            rezultati_pretrage = [karta for karta in self.karte if karta.dogadjaj.lower() == dogadjaj.lower()]
            if rezultati_pretrage:
                print(f"Karte za dogadjaj '{dogadjaj}':")
                for karta in rezultati_pretrage:
                    karta.prikazi_informacije()
            else:
                print(f"Karte za dogadjaj '{dogadjaj}' nisu pronadjene.")
        else:
            print("Svi dostupni dogadjaji:")
            for karta in self.karte:
                print(f"- {karta.dogadjaj}")

    def detalji_o_dogadjaju(self, dogadjaj):
        for karta in self.karte:
            if karta.dogadjaj.lower() == dogadjaj.lower():
                karta.prikazi_informacije()
                return
        print(f"Dogadjaj '{dogadjaj}' nije pronadjen.")

    def kupi_kartu(self, dogadjaj):
        for karta in self.karte:
            if karta.dogadjaj.lower() == dogadjaj.lower() and karta.dostupnost and karta.broj_karata > 0:
                print(f"Kupljena je karta za dogadjaj '{dogadjaj}'.")
                karta.dostupnost = False
                karta.broj_karata -= 1
                return
            elif karta.dogadjaj.lower() == dogadjaj.lower() and karta.broj_karata == 0:
                print(f"Karte za dogadjaj '{dogadjaj}' su rasprodate.")
                return
        print(f"Karte za dogadjaj '{dogadjaj}' trenutno nisu dostupne ili je unesen pogresan dogadjaj.")


sistem_karata = TicketSystem()

while True:
    unos_dogadjaja = input("Unesite naziv dogadjaja (ili 'kraj' za zavrsetak unosa): ")
    
    if unos_dogadjaja.lower() == 'kraj':
        break

    datum_dogadjaja = input("Unesite datum dogadjaja: ")
    cijena_karte = float(input("Unesite cijenu karte: "))
    dostupnost_karata = int(input("Unesite broj dostupnih karata: "))

    nova_karta = Ticket(unos_dogadjaja, datum_dogadjaja, cijena_karte, True, dostupnost_karata)
    sistem_karata.dodaj_kartu(nova_karta)


sistem_karata.pretrazi_karte()

while True:
    unos_detalja = input("Unesite naziv dogadjaja za prikaz detalja (ili 'kraj' za zavrsetak): ")
    
    if unos_detalja.lower() == 'kraj':
        break

    sistem_karata.detalji_o_dogadjaju(unos_detalja)

    odgovor = input("zelite li videti informacije o drugim dogadjajima? (da/ne): ")
    if odgovor.lower() != 'da':
        break


while True:
    dogadjaj_za_kupovinu = input("Unesite naziv dogadjaja za koji zelite kupiti kartu (ili 'kraj' za zavrsetak): ")

    if dogadjaj_za_kupovinu.lower() == 'kraj':
        break

    sistem_karata.kupi_kartu(dogadjaj_za_kupovinu)
    sistem_karata.pretrazi_karte(dogadjaj_za_kupovinu)
