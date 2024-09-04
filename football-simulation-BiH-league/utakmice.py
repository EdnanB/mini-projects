from datetime import datetime, timedelta
import random
from timovi import generiraj_timove

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
        print("\nNema zabiljezenih golova.")
    
    print("\nPobjednik sezone:", pobednik.ime)

    print("\nOdigrane utakmice i rezultati:")
    for utakmica in utakmice:
        rezultat = f"{utakmica.domaci.ime} {utakmica.rezultat.domaci} - {utakmica.rezultat.gosti} {utakmica.gosti.ime}"
        print(f"{utakmica.datum}: {rezultat}")

timovi = generiraj_timove()
utakmice = generiraj_raspored_utakmica(timovi)