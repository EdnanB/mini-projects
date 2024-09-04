class Ucenik:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
        self.evidencija_ocjena = []

    def dodaj_ocjenu(self, ocjena):
        self.evidencija_ocjena.append(ocjena)

    def izracunaj_prosjek(self):
        if not self.evidencija_ocjena:
            return 0
        return sum(self.evidencija_ocjena) / len(self.evidencija_ocjena)


class Gradebook:
    def __init__(self):
        self.Uceniki = []

    def dodaj_ucenika(self, Ucenik):
        self.Uceniki.append(Ucenik)
        print(f"Ucenik {Ucenik.ime} {Ucenik.prezime} je dodan/na u knjigu ocjena.")

    def pronadji_ucenika(self, ime, prezime):
        for Ucenik in self.Uceniki:
            if Ucenik.ime == ime and Ucenik.prezime == prezime:
                return Ucenik
        return None

    def dodaj_ocjenu_uceniku(self, ime, prezime):
        Ucenik = self.pronadji_ucenika(ime, prezime)
        if Ucenik:
            while True:
                ocjena = float(input(f"Unesite ocjenu za ucenika {ime} {prezime}: "))
                if ocjena < 1 or ocjena > 5:
                    print("Ocjena mora biti izmedju 1 i 5.")
                else:
                    Ucenik.dodaj_ocjenu(ocjena)
                    print(f"Dodana ocjena {ocjena} uceniku {ime} {prezime}.")
                    break
        else:
            print(f"Ucenik {ime} {prezime} nije pronadjen.")

    def prosjek_ucenika(self, ime, prezime):
        Ucenik = self.pronadji_ucenika(ime, prezime)
        if Ucenik:
            prosjek = Ucenik.izracunaj_prosjek()
            print(f"Prosjek ocjena za ucenika {ime} {prezime}: {prosjek:.2f}")
        else:
            print(f"Ucenik {ime} {prezime} nije pronadjen.")

    def ispisi_sve(self):
        for Ucenik in self.Uceniki:
            print(f"Ucenik: {Ucenik.ime} {Ucenik.prezime}")
            print(f"Ocjene: {Ucenik.evidencija_ocjena}")
            print(f"Prosjek: {Ucenik.izracunaj_prosjek():.2f}\n")


gradebook = Gradebook()

while True:
    print("\nIzaberite opciju:")
    print("1 - Dodaj ucenika")
    print("2 - Dodaj ocjenu uceniku")
    print("3 - Izracunaj prosjek ucenika")
    print("4 - Ispisi sve")
    print("5 - Napusti program")

    opcija = input("Unesite opciju: ")

    if opcija == "1":
        ime = input("Unesite ime ucenika: ")
        prezime = input("Unesite prezime ucenika: ")
        novi_Ucenik = Ucenik(ime, prezime)
        gradebook.dodaj_ucenika(novi_Ucenik)

    elif opcija == "2":
        ime = input("Unesite ime ucenika: ")
        prezime = input("Unesite prezime ucenika: ")
        gradebook.dodaj_ocjenu_uceniku(ime, prezime)

    elif opcija == "3":
        ime = input("Unesite ime ucenika: ")
        prezime = input("Unesite prezime ucenika: ")
        gradebook.prosjek_ucenika(ime, prezime)

    elif opcija == "4":
        gradebook.ispisi_sve()

    elif opcija == "5":
        print("Napustanje programa. Dovidjenja!")
        break

    else:
        print("Unesite validnu opciju.")
