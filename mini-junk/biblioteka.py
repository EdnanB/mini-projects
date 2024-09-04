class Biblioteka:
    def __init__(self):
        self.knjige = {}

    def nova_knjiga(self):
        ime = input("Unesite ime nove knjige: ")
        autor = input("Unesite ime autora nove knjige: ")
        self.knjige[ime] = autor
        print(f"Dodata je nova knjiga: {ime} - {autor}")

    def izmena_knjige(self):
        ime = input("Unesite ime knjige koju želite izmeniti: ")
        if ime in self.knjige:
            novi_autor = input("Unesite novo ime autora: ")
            self.knjige[ime] = novi_autor
            print(f"Izmena je uspešno izvršena za knjigu: {ime}")
        else:
            print("Knjiga nije pronađena.")

    def brisanje_knjige(self):
        ime = input("Unesite ime knjige koju želite izbrisati: ")
        if ime in self.knjige:
            del self.knjige[ime]
            print(f"Knjiga {ime} je uspešno obrisana.")
        else:
            print("Knjiga nije pronađena.")

    def listanje_svih_knjiga(self):
        if not self.knjige:
            print("Nema unetih knjiga.")
        else:
            print("Lista svih knjiga:")
            for ime, autor in self.knjige.items():
                print(f"{ime} - {autor}")

def prikazi_meni(biblioteka):
    while True:
        print("\n----- MENI -----")
        print("1. Nova knjiga")
        print("2. Izmjena knjige")
        print("3. Brisanje knjige")
        print("4. Listanje svih knjiga")
        print("5. Izlaz iz programa")
        
        izbor = input("Izaberite opciju: ")
        if izbor == "1":
            biblioteka.nova_knjiga()
        elif izbor == "2":
            biblioteka.izmena_knjige()
        elif izbor == "3":
            biblioteka.brisanje_knjige()
        elif izbor == "4":
            biblioteka.listanje_svih_knjiga()
        elif izbor == "5":
            break
        else:
            print("Nepostojeća opcija. Molimo unesite ponovo.")

def main():
    biblioteka = Biblioteka()
    prikazi_meni(biblioteka)

main()
