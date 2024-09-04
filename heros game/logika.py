def log(napadac, zrtva, akcija, oruzje=None, steta=None):
    with open("log.txt", "a") as file:
        if akcija == "napad":
            if oruzje:
                oruzje_naziv = oruzje.naziv
            else:
                oruzje_naziv = "Nema oruzja"
            file.write(f"{napadac.__class__.__name__} je napao {zrtva.__class__.__name__} pomocu {oruzje_naziv} i nanio {steta} stete\n")
        elif akcija == "pobjednik":
            if zrtva is None:
                file.write(f"{napadac.__class__.__name__} je pobijedio u duelu sa Nekim\n")
            else:
                file.write(f"{napadac.__class__.__name__} je pobijedio u duelu sa {zrtva.__class__.__name__}\n")

def prikazi_log():
    with open("log.txt", "r") as file:
        sadrzaj = file.read()
        print(sadrzaj)
