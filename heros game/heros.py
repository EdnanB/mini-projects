import random
import time

class Oruzje:
    def __init__(self, naziv, tip):
        self.naziv = naziv
        self.tip = tip

class Heroj:
    def __init__(self, zdravlje):
        self.zdravlje = zdravlje
        self.ranac = []
        self.aktivno_oruzje = None

    def uzmi_oruzje(self, oruzje):
        if isinstance(self, Carobnjak) and oruzje.tip != "carolija":
            print("Carobnjak moze uzeti samo caroliju")
            return

        if len(self.ranac) >= 2:
            print("Ranac je pun, nemoguce dodati vise oruzja")
            return

        self.ranac.append(oruzje)

    def baci_oruzje(self):
        if not self.ranac:
            raise Exception("Ranac je prazan, nemoguce baciti oruzje")
        return self.ranac.pop(0)

    def promeni_oruzje(self):
        if not self.ranac:
            print("Ranac je prazan, nemoguce promijeniti oruzje")
            return
        self.aktivno_oruzje = self.ranac[0]

    def napadni(self, cudoviste):
        if self.aktivno_oruzje is None:
            raise Exception("Heroj nema aktivno oruzje za napad")

        if isinstance(self, Carobnjak):
            if self.aktivno_oruzje.tip == "carolija":
                tip_napada = "Carobnjak napada pomocu Carolije"
                steta = 20
            else:
                tip_napada = "Carobnjak napada"
                steta = 0
            log(self, cudoviste, tip_napada, self.aktivno_oruzje, steta)
            return tip_napada, steta
        else:
            if self.aktivno_oruzje:
                if self.aktivno_oruzje.tip == "koplje":
                    tip_napada = f"{self.__class__.__name__} napada sa {self.aktivno_oruzje.naziv}"
                    steta = 15
                else:
                    tip_napada = f"{self.__class__.__name__} napada sa {self.aktivno_oruzje.naziv}"
                    steta = 10
            else:
                tip_napada = f"{self.__class__.__name__} nema oruzje za napad"
                steta = 0
            log(self, cudoviste, tip_napada, self.aktivno_oruzje, steta)
            return tip_napada, steta

class Cudoviste:
    def __init__(self, zdravlje):
        self.zdravlje = zdravlje

    def napadni(self, heroj):
        pass

class Zmaj(Cudoviste):
    def __init__(self, zdravlje):
        super().__init__(zdravlje)
        self.aktivno_oruzje = None

    def napadni(self, heroj):
        tipovi_napada = ["Udara", "Bljuje vatru"]
        napad = random.choice(tipovi_napada)
        if napad == "Udara":
            steta = 5
        else:
            steta = 20
        log(self, heroj, napad, None, steta) 
        return napad, steta 

    def promeni_oruzje(self):
        pass

class Pauk(Cudoviste):
    def __init__(self, zdravlje):
        super().__init__(zdravlje)

    def napadni(self, heroj):
        tipovi_napada = ["Udara", "Ujeda"]
        napad = random.choice(tipovi_napada)
        if napad == "Udara":
            steta = 5
        else:
            steta = 8
        log(self, heroj, napad, None, steta)
        return napad, steta    

    def promeni_oruzje(self):
        pass

class Carobnjak(Heroj):
    def __init__(self, zdravlje):
        super().__init__(zdravlje)

class Ratnik(Heroj):
    def __init__(self, zdravlje):
        super().__init__(zdravlje)

def borba(heroj, cudoviste):
    while heroj.zdravlje > 0 and cudoviste.zdravlje > 0:
        time.sleep(2)
        broj = random.randint(0, 100)
        if isinstance(heroj, Pauk):
            napad, steta = heroj.napadni(cudoviste)
            heroj.zdravlje -= steta
            log(heroj, cudoviste, "napad", None, steta)
        else:
            if broj < 50:
                napad, steta = cudoviste.napadni(heroj)
                heroj.zdravlje -= steta
                log(cudoviste, heroj, "napad", None, steta)
            else:
                cudoviste.promeni_oruzje()
                heroj.promeni_oruzje()
                napad, steta = heroj.napadni(cudoviste)
                cudoviste.zdravlje -= steta
                log(heroj, cudoviste, "napad", heroj.aktivno_oruzje, steta)

    if heroj.zdravlje <= 0:
        return cudoviste
    else:
        return heroj

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

def generiraj_duel(heroji):
    carolija = Oruzje("Carolija", "carolija")
    for heroj in heroji:
        if isinstance(heroj, Carobnjak):
            heroj.uzmi_oruzje(carolija)
        elif isinstance(heroj, Ratnik):
            oruzje = Oruzje("Koplje" if random.random() < 0.5 else "Mac", "koplje" if random.random() < 0.5 else "mac")
            heroj.uzmi_oruzje(oruzje)
    return random.sample(heroji, 2)

def duel():
    heroji = [Carobnjak(150), Ratnik(120), Zmaj(100), Pauk(80)]

    print("Prvi mec:")
    time.sleep(2)
    heroji_za_prvi_duel = generiraj_duel(heroji)
    pobijednik_prvog_duela = borba(heroji_za_prvi_duel[0], heroji_za_prvi_duel[1])
    gubitnik_prvog_duela = heroji_za_prvi_duel[1] if pobijednik_prvog_duela == heroji_za_prvi_duel[0] else heroji_za_prvi_duel[0]
    log(pobijednik_prvog_duela, gubitnik_prvog_duela, "pobjednik")
    prikazi_log()
    print()

    print("Drugi mec:")
    time.sleep(2)
    heroji_za_drugi_duel = generiraj_duel([heroj for heroj in heroji if heroj not in heroji_za_prvi_duel])
    pobijednik_drugog_duela = borba(heroji_za_drugi_duel[0], heroji_za_drugi_duel[1])
    gubitnik_drugog_duela = heroji_za_drugi_duel[1] if pobijednik_drugog_duela == heroji_za_drugi_duel[0] else heroji_za_drugi_duel[0]
    log(pobijednik_drugog_duela, gubitnik_drugog_duela, "pobjednik")
    prikazi_log()
    print()

duel()