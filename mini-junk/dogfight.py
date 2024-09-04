import random
import time

class Avion:
    def __init__(self, ime, zdravlje, municija):
        self.ime = ime
        self.zdravlje = zdravlje
        self.municija = municija

    def pucaj(self, meta):
        municija = random.randint(0, 10)
        meta.zdravlje -= municija * 2
        self.municija -= municija
        return self.municija <= 0 or self.zdravlje <= 0

avion1 = Avion("Ilyushin", 100, 100)
avion2 = Avion("Spitfire", 100, 100)

avioni = (avion1, avion2)

print(f"Runda\tIme\t\tZdravlje/Municija\t:\tIme\t\tZdravlje/Municija")
print(f"*****************************************************************************************")
broj_rundi = 0
pobjednik = None
while True:
    broj_rundi += 1
    zavrseno = False
    for i in range(len(avioni)):
        napadac = avioni[abs(i - 1)]
        meta = avioni[i]
        if napadac.pucaj(meta):
            zavrseno = True
            
        print(f"{broj_rundi}\t{napadac.ime}\t{napadac.zdravlje}/{napadac.municija}\t\t\t\t{meta.ime}\t{meta.zdravlje}/{meta.municija}")
        time.sleep(1)

    if zavrseno:
        pobjednik = avion1 if avion1.zdravlje > avion2.zdravlje else avion2
        break

if pobjednik:
    print(f"\n\t\t\tPobjednik je avion: {pobjednik.ime}!")
else:
    print("Igra završena neriješeno.")

