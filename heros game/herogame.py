import random
import time

class Oruzje:
    def __init__(self, naziv, tip):
        self.naziv = naziv
        self.tip = tip

class Heroj:
    def __init__(self, health):
        self.health = health
        self.ranac = []
        self.aktivno_oruzje = None

    def uzmi_oruzje(self, oruzje):
        if isinstance(self, Carobnjak) and oruzje.tip != "carolija":
            print("Čarobnjak može uzeti samo čaroliju")
            return

        if len(self.ranac) >= 2:
            print("Ranac je pun, nemoguće dodati više oružja")
            return

        self.ranac.append(oruzje)

    def baci_oruzje(self):
        if not self.ranac:
            raise Exception("Ranac je prazan, nemoguće baciti oružje")
        return self.ranac.pop(0)

    def promeni_oruzje(self):
        if not self.ranac:
            raise Exception("Ranac je prazan, nemoguće promijeniti oružje")
        self.aktivno_oruzje = self.ranac[0]

    def napadni(self, cudoviste):
        if self.aktivno_oruzje is None:
            raise Exception("Heroj nema aktivno oružje za napad")

        if isinstance(self, Carobnjak):
            damage = 20 if self.aktivno_oruzje.tip == "carolija" else 0
        else: 
            if self.aktivno_oruzje.tip == "koplje":
                damage = 15
            elif self.aktivno_oruzje.tip == "mac":
                damage = 10
            else:
                raise Exception("Neprepoznatljiv tip oružja")

        cudoviste.health -= damage
        log(self, cudoviste, "napad", self.aktivno_oruzje, damage)

        return "Napad", damage  

class Cudoviste:
    def __init__(self, health):
        self.health = health

    def napadni(self, heroj):
        pass

class Zmaj(Cudoviste):
    def __init__(self, health):
        super().__init__(health)
        self.aktivno_oruzje = None

    def napadni(self, heroj):
        attack_types = ["Udara", "Bljuje vatru"]
        attack = random.choice(attack_types)
        if attack == "Udara":
            damage = 5
        else:
            damage = 20
        return attack, damage  
 

    def promeni_oruzje(self):
        pass

class Pauk(Cudoviste):
    def __init__(self, health):
        super().__init__(health)

    def napadni(self):
        attack_types = ["Udara", "Ujeda"]
        attack = random.choice(attack_types)
        if attack == "Udara":
            damage = 5
        else:
            damage = 8
        return attack, damage  

class Carobnjak(Heroj):
    def __init__(self, health):
        super().__init__(health)

class MacEvalac(Heroj):
    def __init__(self, health):
        super().__init__(health)

def borba(heroj, cudoviste):
    while heroj.health > 0 and cudoviste.health > 0:
        time.sleep(2)
        broj = random.randint(0, 100)
        if broj < 50:
            attack, damage = cudoviste.napadni(heroj)
            heroj.health -= damage
            log(cudoviste, heroj, "napad", None, damage)
        else:
            cudoviste.promeni_oruzje()
            heroj.promeni_oruzje()
            attack, damage = heroj.napadni(cudoviste)
            cudoviste.health -= damage
            log(heroj, cudoviste, "napad", heroj.aktivno_oruzje, damage)
            time.sleep(2)

    if heroj.health <= 0:
        return cudoviste
    else:
        return heroj

def log(napadac, zrtva, akcija, oruzje=None, steta=None):
    with open("log.txt", "a") as file:
        if akcija == "napad":
            oruzje_naziv = oruzje.naziv if oruzje is not None else "Nema oružja"
            file.write(f"{napadac.__class__.__name__} je napao {zrtva.__class__.__name__} pomoću {oruzje_naziv} i naneo {steta} štete\n")
        elif akcija == "pobednik":
            if zrtva is None:
                file.write(f"{napadac.__class__.__name__} je pobedio u duelu sa Nekim\n")
            else:
                file.write(f"{napadac.__class__.__name__} je pobedio u duelu sa {zrtva.__class__.__name__}\n")


def prikazi_log():
    with open("log.txt", "r") as file:
        sadrzaj = file.read()
        print(sadrzaj)

def finale(heroj1, heroj2):
    print("Finale!")
    time.sleep(2)
    pobednik = borba(heroj1, heroj2)
    gubitnik = heroj2 if pobednik == heroj1 else heroj1
    print(f"Pobednik finala je {pobednik.__class__.__name__}")
    log(pobednik, gubitnik, "pobednik")

def duel(heroj1, heroj2):
    print("Prvi duel:")
    time.sleep(2)
    pobednik_prvog_duela = borba(heroj1, heroj2)
    gubitnik_prvog_duela = heroj2 if pobednik_prvog_duela == heroj1 else heroj1
    log(pobednik_prvog_duela, gubitnik_prvog_duela, "pobednik")
    
    print("Drugi duel:")
    time.sleep(2)
    pobednik_drugog_duela = borba(heroj1, heroj2) 
    gubitnik_drugog_duela = heroj2 if pobednik_drugog_duela == heroj1 else heroj1
    log(pobednik_drugog_duela, gubitnik_drugog_duela, "pobednik")

    finale(pobednik_prvog_duela, pobednik_drugog_duela)

carobnjak = Carobnjak(150)
carolija = Oruzje("Carolija", "carolija")

carobnjak.uzmi_oruzje(carolija)

zmaj = Zmaj(100)
pauk = Pauk(80)

duel(carobnjak, zmaj)
prikazi_log()