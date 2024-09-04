class Book:
    def __init__(self, naslov, autor, isbn):
        self.naslov = naslov
        self.autor = autor
        self.isbn = isbn
        self.iznajmljena = False

    def prikazi_knjigu(self):
        print(f"Naslov: {self.naslov}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        status = "Iznajmljena" if self.iznajmljena else "Dostupna"
        print(f"Status iznajmljivanja: {status}")

class Library:
    def __init__(self):
        self.kolekcija = []

    def dodaj_knjigu(self, knjiga):
        self.kolekcija.append(knjiga)
        print(f"Knjiga '{knjiga.naslov}' uspjesno dodana u biblioteku.")

    def obrisi_knjigu(self, isbn):
        for knjiga in self.kolekcija:
            if knjiga.isbn == isbn:
                self.kolekcija.remove(knjiga)
                print(f"Knjiga '{knjiga.naslov}' uspjesno obrisana iz biblioteke.")
                return
        print("Knjiga sa tim ISBN-om nije pronadjena u biblioteci.")

    def pretrazi_po_naslovu(self, naslov):
        pronadjene_knjige = [knjiga for knjiga in self.kolekcija if knjiga.naslov.lower() == naslov.lower()]
        if pronadjene_knjige:
            print(f"Knjige sa naslovom '{naslov}':")
            for knjiga in pronadjene_knjige:
                knjiga.prikazi_knjigu()
        else:
            print("Nijedna knjiga sa tim naslovom nije pronadjena.")

    def pretrazi_po_autoru(self, autor):
        pronadjene_knjige = [knjiga for knjiga in self.kolekcija if knjiga.autor.lower() == autor.lower()]
        if pronadjene_knjige:
            print(f"Knjige autora '{autor}':")
            for knjiga in pronadjene_knjige:
                knjiga.prikazi_knjigu()
        else:
            print("Nijedna knjiga tog autora nije pronadjena.")


biblioteka = Library()

knjiga1 = Book("Gospodja Bovari", "Gustave Flaubert", "123456789")
knjiga2 = Book("Na Drini cuprija", "Ivo Andric", "987654321")
knjiga3 = Book("Prokleta Avlija", "Mesa Selimovic", "135792468")

biblioteka.dodaj_knjigu(knjiga1)
biblioteka.dodaj_knjigu(knjiga2)
biblioteka.dodaj_knjigu(knjiga3)

biblioteka.pretrazi_po_naslovu("Gospodja Bovari")
biblioteka.pretrazi_po_autoru("Ivo Andric")

biblioteka.obrisi_knjigu("135792468")

biblioteka.pretrazi_po_autoru("Mesa Selimovic")
