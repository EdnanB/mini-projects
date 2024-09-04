class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def prikazi_info(self):
        print(f"Proizvod: {self.naziv}, Cijena: {self.cijena}, Kolicina: {self.kolicina}")


class Korisnik:
    def __init__(self, korisnicko_ime, lozinka):
        self.korisnicko_ime = korisnicko_ime
        self.lozinka = lozinka
        self.korpa = []

    def dodaj_u_korpu(self, proizvod):
        self.korpa.append(proizvod)
        print(f"{proizvod.naziv} dodan u korpu.")

    def ukloni_iz_korpe(self, proizvod):
        if proizvod in self.korpa:
            self.korpa.remove(proizvod)
            print(f"{proizvod.naziv} uklonjen iz korpe.")
        else:
            print("Proizvod nije pronadjen u korpi.")

    def prikazi_korpu(self):
        if self.korpa:
            print("Stavke u vasoj korpi:")
            for proizvod in self.korpa:
                proizvod.prikazi_info()
        else:
            print("Vasa korpa je prazna.")

    def kupovina(self):
        ukupna_cijena = sum(proizvod.cijena for proizvod in self.korpa)
        print(f"Ukupna cijena: {ukupna_cijena}")
        self.korpa = []
        print("Hvala na kupovini!")

    def prijava(self, korisnicko_ime, lozinka):
        return self.korisnicko_ime == korisnicko_ime and self.lozinka == lozinka


class OnlineProdavnica:
    def __init__(self):
        self.korisnici = {}
        self.proizvodi = []

    def registracija_korisnika(self, korisnicko_ime, lozinka):
        if korisnicko_ime not in self.korisnici:
            self.korisnici[korisnicko_ime] = Korisnik(korisnicko_ime, lozinka)
            print("Korisnik uspjesno registrovan.")
        else:
            print("Korisnicko ime vec postoji.")

    def prijava_korisnika(self, korisnicko_ime, lozinka):
        if korisnicko_ime in self.korisnici:
            korisnik = self.korisnici[korisnicko_ime]
            if korisnik.prijava(korisnicko_ime, lozinka):
                print("Uspjesna prijava.")
                return korisnik
            else:
                print("Nevazece korisnicko ime ili lozinka.")
        else:
            print("Korisnik nije pronadjen.")

    def dodaj_proizvod(self, proizvod):
        self.proizvodi.append(proizvod)
        print(f"Proizvod {proizvod.naziv} dodan u prodavnicu.")

    def prikazi_proizvode(self):
        print("Dostupni proizvodi u prodavnici:")
        for proizvod in self.proizvodi:
            proizvod.prikazi_info()


def dodaj_proizvode_u_korpu(prodavnica, korisnik):
    while True:
        izbor = input("Unesite naziv proizvoda koji zelite dodati u korpu (ili 'kraj' za zavrsetak unosa): ")
        if izbor.lower() == 'kraj':
            break
        else:
            pronadjen = False
            for proizvod in prodavnica.proizvodi:
                if proizvod.naziv.lower() == izbor.lower():
                    korisnik.dodaj_u_korpu(proizvod)
                    pronadjen = True
                    break
            if not pronadjen:
                print("Proizvod nije pronadjen u prodavnici.")



prodavnica = OnlineProdavnica()


prodavnica.dodaj_proizvod(Proizvod("Laptop", 1000, 10))
prodavnica.dodaj_proizvod(Proizvod("Mis", 20, 50))
prodavnica.dodaj_proizvod(Proizvod("Tastatura", 50, 30))


prodavnica.registracija_korisnika("korisnik1", "lozinka1")


korisnik = prodavnica.prijava_korisnika("korisnik1", "lozinka1")


prodavnica.prikazi_proizvode()


dodaj_proizvode_u_korpu(prodavnica, korisnik)


korisnik.prikazi_korpu()


korisnik.kupovina()
