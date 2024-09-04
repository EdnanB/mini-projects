class Employee:
    def __init__(self, ime, prezime, id, pozicija):
        self.ime = ime
        self.prezime = prezime
        self.id = id
        self.pozicija = pozicija

    def __str__(self):
        return f"Ime: {self.ime}, Prezime: {self.prezime}, ID: {self.id}, Pozicija: {self.pozicija}"

class Company:
    def __init__(self):
        self.zaposleni = []

    def dodaj_zaposlenog(self, zaposlen):
        self.zaposleni.append(zaposlen)
        print(f"Zaposleni '{zaposlen.ime} {zaposlen.prezime}' uspjesno dodan.")

    def obrisi_zaposlenog(self, id):
        for zaposlen in self.zaposleni:
            if zaposlen.id == id:
                self.zaposleni.remove(zaposlen)
                print(f"Zaposleni '{zaposlen.ime} {zaposlen.prezime}' uspjesno obrisan.")
                return
        print("Zaposleni sa tim ID-jem nije pronadjen.")

    def izlistaj_zaposlene(self):
        if not self.zaposleni:
            print("Nema unesenih zaposlenih.")
        else:
            for zaposlen in self.zaposleni:
                print(zaposlen)

kompanija = Company()

while True:
    unos = input("Da li zelite unijeti novog zaposlenika? (da/ne): ").lower()
    
    if unos == 'da':
        ime = input("Unesite ime zaposlenika: ")
        prezime = input("Unesite prezime zaposlenika: ")
        id = int(input("Unesite ID zaposlenika: "))
        pozicija = input("Unesite poziciju zaposlenika: ")

        novi_zaposleni = Employee(ime, prezime, id, pozicija)
        kompanija.dodaj_zaposlenog(novi_zaposleni)
    elif unos == 'ne':
        break
    else:
        print("Pogresan unos. Molimo vas da unesete 'da' ili 'ne'.")


kompanija.izlistaj_zaposlene()


while True:
    id_zaposlenika_za_brisanje = input("Unesite ID zaposlenika kojeg zelite obrisati (ili unesite 'kraj' za zavrsetak): ")
    
    if id_zaposlenika_za_brisanje.lower() == 'kraj':
        break
    
    try:
        id_zaposlenika_za_brisanje = int(id_zaposlenika_za_brisanje)
        kompanija.obrisi_zaposlenog(id_zaposlenika_za_brisanje)
    except ValueError:
        print("Pogresan unos. Molimo vas da unesete broj ID-a ili 'kraj'.")
    

    kompanija.izlistaj_zaposlene()
