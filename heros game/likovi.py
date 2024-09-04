import random
from logika import log

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
        
        self.aktivno_oruzje = random.choice(self.ranac)

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
        else:
            if self.aktivno_oruzje.tip == "koplje":
                tip_napada = f"{self.__class__.__name__} napada sa {self.aktivno_oruzje.naziv}"
                steta = 15
            elif self.aktivno_oruzje.tip == "mac":
                tip_napada = f"{self.__class__.__name__} napada sa {self.aktivno_oruzje.naziv}"
                steta = 10
            else:
                tip_napada = f"{self.__class__.__name__} nema odgovarajuce oruzje za napad"
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
    
    def uzmi_oruzje(self, oruzje):
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
    
    def uzmi_oruzje(self, oruzje):
        pass

class Carobnjak(Heroj):
    def __init__(self, zdravlje):
        super().__init__(zdravlje)

class Ratnik(Heroj):
    def __init__(self, zdravlje):
        super().__init__(zdravlje)
        self.tipovi_oruzja = {
            "koplje": 15,
            "mac": 10
        }

    def napadni(self, cudoviste):
        if self.aktivno_oruzje is None:
            raise Exception("Ratnik nema aktivno oruzje za napad")

        if self.aktivno_oruzje.tip in self.tipovi_oruzja:
            tip_napada = f"{self.__class__.__name__} napada sa {self.aktivno_oruzje.naziv}"
            steta = self.tipovi_oruzja[self.aktivno_oruzje.tip]
        else:
            tip_napada = f"{self.__class__.__name__} nema odgovarajuce oruzje za napad"
            steta = 0

        log(self, cudoviste, tip_napada, self.aktivno_oruzje, steta) 
        return tip_napada, steta