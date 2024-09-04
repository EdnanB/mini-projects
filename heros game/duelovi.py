import time
import random
from likovi import Zmaj, Pauk, Carobnjak, Ratnik
from logika import log, prikazi_log
from akcije import borba, generiraj_duel
from oruzje import Oruzje

def duel():
    heroji = [Carobnjak(150), Ratnik(120), Zmaj(100), Pauk(80)]

    print("Prvi mec:")
    time.sleep(2)
    heroji_za_prvi_duel = generiraj_duel(heroji)

    for heroj in heroji:
        oruzje = Oruzje("Koplje" if random.random() < 0.5 else "Mac", "koplje" if random.random() < 0.5 else "mac")
        heroj.uzmi_oruzje(oruzje)
        heroj.promeni_oruzje()

    pobijednik_prvog_duela = borba(heroji_za_prvi_duel[0], heroji_za_prvi_duel[1])
    gubitnik_prvog_duela = heroji_za_prvi_duel[1] if pobijednik_prvog_duela == heroji_za_prvi_duel[0] else heroji_za_prvi_duel[0]
    log(pobijednik_prvog_duela, gubitnik_prvog_duela, "pobjednik")
    prikazi_log()
    print()

    print("Drugi mec:")
    time.sleep(2)
    heroji_za_drugi_duel = generiraj_duel([heroj for heroj in heroji if heroj not in heroji_za_prvi_duel])

    for heroj in heroji:
        oruzje = Oruzje("Koplje" if random.random() < 0.5 else "Mac", "koplje" if random.random() < 0.5 else "mac")
        heroj.uzmi_oruzje(oruzje)
        heroj.promeni_oruzje()

    pobijednik_drugog_duela = borba(heroji_za_drugi_duel[0], heroji_za_drugi_duel[1])
    gubitnik_drugog_duela = heroji_za_drugi_duel[1] if pobijednik_drugog_duela == heroji_za_drugi_duel[0] else heroji_za_drugi_duel[0]
    log(pobijednik_drugog_duela, gubitnik_drugog_duela, "pobjednik")
    prikazi_log()
    print()
