class Oblik:
    def __init__(self, x, y, boja, ime):
        self.x = x
        self.y = y
        self.boja = boja
        self.ime = ime


class Kvadrat(Oblik):
    def __init__(self, x, y, boja, ime):
        super().__init__(x, y, boja, ime)
        self.stranica = abs(x * 2)

    def izracunaj_povrsinu(self):
        return self.stranica ** 2

    def informacije_o_stranici(self):
        return (f"Stranica kvadrata je {self.stranica} jedinica, sto je {self.stranica} cm.")


class Pravougaonik(Oblik):
    def __init__(self, x, y, boja, ime):
        super().__init__(x, y, boja, ime)
        self.sirina = abs(x * 2)
        self.visina = abs(y * 2)

    def izracunaj_povrsinu(self):
        return self.sirina * self.visina

    def informacije_o_stranici(self):
        return (f"Sirina pravougaonika je {self.sirina} jedinica, sto je {self.sirina} cm, " \
               f"a visina pravougaonika je {self.visina} jedinica, sto je {self.visina} cm.")


def odredi_oblik(x, y):
    if x != y:
        return Pravougaonik(x, y, "crveni", "Pravougaonik")
    else:
        return Kvadrat(x, y, "plavi", "Kvadrat")


x_unos = int(input("Unesite vrijednost za x: "))
y_unos = int(input("Unesite vrijednost za y: "))

oblik = odredi_oblik(x_unos, y_unos)
print(f"Kreiran je {oblik.boja} {oblik.ime} sa x = {oblik.x}, y = {oblik.y}")
print(f"Povrsina oblika je: {oblik.izracunaj_povrsinu()} cm.")
print(oblik.informacije_o_stranici())
