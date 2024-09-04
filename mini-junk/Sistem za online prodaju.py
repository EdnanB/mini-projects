class Product:
    def __init__(self, naziv, cijena):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = 0

class ShoppingCart:
    def __init__(self):
        self.proizvodi = []

    def dodaj_proizvod(self, proizvod, kolicina):
        if proizvod in self.proizvodi:
            index = self.proizvodi.index(proizvod)
            self.proizvodi[index].kolicina += kolicina
        else:
            proizvod.kolicina = kolicina
            self.proizvodi.append(proizvod)

    def ukloni_proizvod(self, naziv_proizvoda, kolicina):
        for proizvod in self.proizvodi:
            if proizvod.naziv.lower() == naziv_proizvoda.lower():
                if proizvod.kolicina > kolicina:
                    proizvod.kolicina -= kolicina
                    print(f"Iz korpe je uklonjeno {kolicina} komada proizvoda '{proizvod.naziv}'.")
                    return
                elif proizvod.kolicina == kolicina:
                    self.proizvodi.remove(proizvod)
                    print(f"Iz korpe je uklonjen proizvod '{proizvod.naziv}'.")
                    return
                else:
                    print(f"Neispravna kolicina za uklanjanje proizvoda '{proizvod.naziv}'.")
                    return
        print("Proizvod nije pronadjen u korpi.")

    def ukupna_cijena(self):
        ukupno = 0
        for proizvod in self.proizvodi:
            ukupno += proizvod.cijena * proizvod.kolicina
        return ukupno

def prikazi_proizvode():
    print("\nPonuđeni proizvodi:")
    print("1 - Laptop - 1430 KM")
    print("2 - Mis - 25 KM")
    print("3 - Tastatura - 47 KM")
    print("4 - Monitor - 750 KM")
    print("5 - Slusalice - 220 KM")
    print("6 - Zvučnici - 140 KM")

proizvod1 = Product("Laptop", 1430)
proizvod2 = Product("Mis", 25)
proizvod3 = Product("Tastatura", 47)
proizvod4 = Product("Monitor", 750)
proizvod5 = Product("Slusalice", 220)
proizvod6 = Product("Zvucnici", 140)

korpa = ShoppingCart()

while True:
    print("\nIzaberite opciju:")
    print("1 - Dodaj proizvod")
    print("2 - Ukloni proizvod")
    print("3 - Pregled korpe")
    print("4 - Zavrsi kupovinu")

    opcija = input("Unesite opciju: ")

    if opcija == "1":
        prikazi_proizvode()
        odabrani_proizvod = input("Odaberite proizvod koji zelite dodati (unosite broj): ")
        kolicina = int(input("Unesite kolicinu proizvoda: "))

        if odabrani_proizvod == "1":
            korpa.dodaj_proizvod(proizvod1, kolicina)
        elif odabrani_proizvod == "2":
            korpa.dodaj_proizvod(proizvod2, kolicina)
        elif odabrani_proizvod == "3":
            korpa.dodaj_proizvod(proizvod3, kolicina)
        elif odabrani_proizvod == "4":
            korpa.dodaj_proizvod(proizvod4, kolicina)
        elif odabrani_proizvod == "5":
            korpa.dodaj_proizvod(proizvod5, kolicina)
        elif odabrani_proizvod == "6":
            korpa.dodaj_proizvod(proizvod6, kolicina)
        else:
            print("Neispravan unos.")

    elif opcija == "2":
        prikazi_proizvode()
        naziv_proizvoda = input("Unesite naziv proizvoda koji zelite ukloniti: ")
        kolicina = int(input("Unesite kolicinu proizvoda koji zelite ukloniti: "))
        korpa.ukloni_proizvod(naziv_proizvoda, kolicina)

    elif opcija == "3":
        print("\nPregled korpe:")
        for proizvod in korpa.proizvodi:
            print(f"{proizvod.naziv} - Kolicina: {proizvod.kolicina} - Cijena: {proizvod.cijena * proizvod.kolicina} KM")
        print("Ukupna cijena u korpi:", korpa.ukupna_cijena(), " KM")

    elif opcija == "4":
        print("\nZavrsena kupovina.")
        print("Pregled korpe:")
        for proizvod in korpa.proizvodi:
            print(f"{proizvod.naziv} - Kolicina: {proizvod.kolicina} - Cijena: {proizvod.cijena * proizvod.kolicina} KM")
        print("Ukupna cijena svih proizvoda:", korpa.ukupna_cijena())
        break

    else:
        print("Unesite validnu opciju.")
