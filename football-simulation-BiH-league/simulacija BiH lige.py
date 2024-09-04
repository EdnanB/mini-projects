import random
from datetime import datetime, timedelta

class Tim:
    def __init__(self, ime, igraci):
        self.ime = ime
        self.igraci = igraci
        self.bodovi = 0
        self.gol_razlika = 0
        self.golovi = {}

    def __str__(self):
        return f"{self.ime} - Bodovi: {self.bodovi}, Gol razlika: {self.gol_razlika}"

class Rezultat:
    def __init__(self, domaci=0, gosti=0):
        self.domaci = domaci
        self.gosti = gosti

class Utakmica:
    def __init__(self, domaci_tim, gostujuci_tim, datum):
        self.domaci = domaci_tim
        self.gosti = gostujuci_tim
        self.rezultat = None
        self.datum = datum

    def simuliraj_rezultat(self):
        
        sansa_gol_domaci = 3
        sansa_gol_gosti = 1

        max_golova_u_utakmici = 6  

        golovi_domaci = 0
        golovi_gosti = 0

        for _ in range(90):
            
            if golovi_domaci + golovi_gosti >= max_golova_u_utakmici:
                break

            
            if golovi_domaci >= max_golova_u_utakmici / 2:
                break

            if random.randint(1, 100) <= sansa_gol_domaci:
                golovi_domaci += 1

            if random.randint(1, 100) <= sansa_gol_gosti:
                golovi_gosti += 1

        self.rezultat = Rezultat(golovi_domaci, golovi_gosti)
        self.domaci.gol_razlika += golovi_domaci - golovi_gosti
        self.gosti.gol_razlika += golovi_gosti - golovi_domaci

        if golovi_domaci > golovi_gosti:
            self.domaci.bodovi += 3
        elif golovi_domaci < golovi_gosti:
            self.gosti.bodovi += 3
        else:
            self.domaci.bodovi += 1
            self.gosti.bodovi += 1

def generiraj_timove():
    timovi = [
        Tim("FK Sarajevo", ["Rogic L." , "Andjusic N." , "Anicic M." , "Beganovic A." , "Buljubasic M." , "Djurickov M." , "Durakovic E." , "Hasic A." , "Julardzija E." , "Mustafic M." , "Renan Oliveira"]),
        Tim("HSK Zrinjski", ["Marić M." , "Bilbija N." , "Corluka J." , "Ivancic A." , "Kis T." , "Malekinusic M." , "Memija K." , "Radic S." , "Sabljic F." , "Senic M." , "Zlomislic D."]),
        Tim("FK Borac", ["David Stjepanovic" , "Jakov Blagaic" , "David Cavic" , "Maks Juraj Celic" , "Stefan Ficovic" , "Srdjan Grahovac" , "Sebastian Herrera" , "Ranko Jokic" , "Alen Jurilj" , "Zoran Kvržić" , "Jovo Lukic"]),
        Tim("FK Velez", ["Hadzikic O." , "Bruno Oliveira" , "Giorgi Guliashvili" , "Halilovic D." , "Haskic N." , "Hrkac A." , "Orec A." , "Sikalo T." , "Sturm K." , "Suljic A." , "Vehabovic E."]),
        Tim("FK Sloga Doboj", ["Scekic Nemanja" , "Pavel Baranov" , "Nikola Dujakovic" , "Srdjan Grabez" , "Toni Jovic" , "Josip Kvesić" , "Milan Milanovic" , "Milos Nikolic" , "Dejan Popara" , "Ajdin Redzic" , "Dejan Vidic"]),
        Tim("NK Siroki Brijeg", ["Bender J." , "Chinedu S." , "Dadic T." , "Kpan C." , "Lukic D." , "Mamic L." , "Matic M." , "Musa B." , "Pranjic I." , "Saravanja I." , "Tomic T."]),
        Tim("HSK Posusje", ["Marko Galic" , "Andro Babić" , "Dominik Begić" , "Gabrijel Boban" , "Joao Erick" , "Karlo Kamenar" , "Luka Lucic" , "Frane Maglica" , "Nikola Mandic" , "Ivan Marić" , "Branko Vrgoc"]),
        Tim("NK GOSK", ["Adnan Bobic" , "Tino Bradara" , "Aldin Cajic" , "Gabrijel Coko" , "Faruk Gogic" , "Filip Mihaljevic" , "Jure Obsivac" , "Vasilije Radenovic" , "Nihad Sero" , "Dino Skorup" , "Riad Suta"]),
        Tim("FK Tuzla City", ["Eldin Lolic" , "Faruk Bihorac" , "Dino Coric" , "Mirza Delimedjac" , "Huso Karjasevic" , "Rijad Kobiljar" , "Mirzad Mehanovic" , "Nenad Nikic" , "Ajdin Nukic" , "Amer Ordagic" , "Djordje Pantelic"]),
        Tim("FK Zeljeznicar", ["Vedad Muftic" , "Abdulmalik Al Jaber" , "Joseph Amoah" , "Andrija Drljo" , "Drazen Dubackic" , "Marin Galic" , "Aleksandar Kosoric" , "Sulejman Krpic" , "Nedim Mekic" , "Benjamin Sehic" , "Vahid Selimovic"]),
        Tim("FK Igman", ["Ceman A." , "Ahmetovic M." , "Denkovic S." , "Djoric I." , "Dupovac A." , "Hebibovic A." , "Hebibovic K." , "Janketic V." , "Oremus M." , "Piric A." , "Sipovic E."]),
        Tim("FK Zvijezda - 09", ["Damjanovic L." , "Karaklajic P." , "Maksimovic N." , "Ponjevic D." , "Ristanovic P." , "Saliman K." , "Sapic S." , "Tomanovic S." , "Vadze G." , "Velickovic S." , "Vukoja B."]),
        ]
    
    return timovi
    
def generiraj_raspored_utakmica(timovi):
    raspored = []
    broj_timova = len(timovi)
    
    parovi_timova = [(timovi[i], timovi[j]) for i in range(broj_timova) for j in range(i + 1, broj_timova)]
    random.shuffle(parovi_timova)
    
    
    start_datuma = datetime.strptime('2024-01-01', '%Y-%m-%d')
    for k in range(2):
        for par in parovi_timova:
            
            datum_utakmice = start_datuma + timedelta(days=random.randint(1, 30))
            nova_utakmica = Utakmica(par[0], par[1], datum_utakmice.strftime('%Y-%m-%d'))
            raspored.append(nova_utakmica)
    
    return raspored

def azuriraj_tabelu(utakmice):
    for utakmica in utakmice:
        utakmica.simuliraj_rezultat()
        for igrac in utakmica.domaci.igraci:
            utakmica.domaci.golovi[igrac] = utakmica.domaci.golovi.get(igrac, 0) + utakmica.rezultat.domaci
        for igrac in utakmica.gosti.igraci:
            utakmica.gosti.golovi[igrac] = utakmica.gosti.golovi.get(igrac, 0) + utakmica.rezultat.gosti

def sortiraj_po_bodovima_i_razlici(tim):
    return (-tim.bodovi, -tim.gol_razlika)

def ispisi_tabelu_na_kraju_sezone(timovi):
    sortirani_timovi = sorted(timovi, key=sortiraj_po_bodovima_i_razlici)
    print("Tabela lige na kraju sezone:")
    print("{:<5} {:<20} {:<10} {:<10}".format("Poz.", "Tim", "Bodovi", "Gol razlika"))
    i = 1
    for tim in sortirani_timovi:
        print("{:<5} {:<20} {:<10} {:<10}".format(i, tim.ime, tim.bodovi, tim.gol_razlika))
        i += 1
    
    pobednik = sortirani_timovi[0]

    
    svi_golovi = {igrac: broj_golova for tim in timovi for igrac, broj_golova in tim.golovi.items()}
    if svi_golovi:  
        najbolji_strijelac = max(svi_golovi, key=svi_golovi.get)
        tim_najboljeg_strijelca = [tim for tim in timovi if najbolji_strijelac in tim.igraci][0]
        print("\nNajbolji strijelac sezone:", najbolji_strijelac, f"(Tim: {tim_najboljeg_strijelca.ime})")
    else:
        print("\nNema zabilježenih golova.")
    
    print("\nPobednik sezone:", pobednik.ime)

    print("\nOdigrane utakmice i rezultati:")
    for utakmica in utakmice:
        rezultat = f"{utakmica.domaci.ime} {utakmica.rezultat.domaci} - {utakmica.rezultat.gosti} {utakmica.gosti.ime}"
        print(f"{utakmica.datum}: {rezultat}")

timovi = generiraj_timove()
utakmice = generiraj_raspored_utakmica(timovi)

azuriraj_tabelu(utakmice)
ispisi_tabelu_na_kraju_sezone(timovi)
