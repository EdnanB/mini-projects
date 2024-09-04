class Room:
    def __init__(self, broj_sobe, tip_sobe):
        self.broj_sobe = broj_sobe
        self.tip_sobe = tip_sobe
        self.status = "slobodna"
        self.gost = None

    def rezervisi(self, ime_gosta):
        self.status = "zauzeta"
        self.gost = ime_gosta
        print(f"Soba {self.broj_sobe} je rezervisana za gosta {ime_gosta}.")

    def oslobodi(self):
        self.status = "slobodna"
        self.gost = None
        print(f"Soba {self.broj_sobe} je oslobodjena.")

class Hotel:
    def __init__(self):
        self.sobe = []

    def dodaj_sobu(self, broj_sobe, tip_sobe):
        nova_soba = Room(broj_sobe, tip_sobe)
        self.sobe.append(nova_soba)
        print(f"Dodana soba {broj_sobe} u hotel.")

    def rezervisi_sobu(self):
        print("Dostupne sobe:")
        for soba in self.sobe:
            print(f"Soba {soba.broj_sobe} - Status: {soba.status}")

        broj_sobe = input("Unesite broj sobe koju zelite rezervisati: ")
        for soba in self.sobe:
            if soba.broj_sobe == broj_sobe and soba.status == "slobodna":
                gost = input("Unesite ime gosta: ")
                soba.rezervisi(gost)
                return
        print("Soba nije pronadjena ili je vec zauzeta.")

    def odjavi_sobu(self):
        print("Zauzete sobe:")
        for soba in self.sobe:
            if soba.status == "zauzeta":
                print(f"Soba {soba.broj_sobe} - Gost: {soba.gost}")

        broj_sobe = input("Unesite broj sobe koju zelite osloboditi: ")
        for soba in self.sobe:
            if soba.broj_sobe == broj_sobe and soba.status == "zauzeta":
                soba.oslobodi()
                return
        print("Soba nije pronadjena ili vec slobodna.")


hotel = Hotel()


while True:
    broj_sobe = input("Unesite broj sobe (ili 'kraj' za zavrsetak unosa): ")
    if broj_sobe.lower() == 'kraj':
        break
    tip_sobe = input("Unesite tip sobe: ")
    hotel.dodaj_sobu(broj_sobe, tip_sobe)


while True:
    odgovor = input("Zelite li rezervisati sobu? (da/ne): ")
    if odgovor.lower() != 'da':
        break
    hotel.rezervisi_sobu()


while True:
    odgovor = input("Zelite li osloboditi sobu? (da/ne): ")
    if odgovor.lower() != 'da':
        break
    hotel.odjavi_sobu()
