import random
import time
from likovi import Pauk, Carobnjak, Ratnik
from logika import log
from oruzje import Oruzje


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


def generiraj_duel(heroji):
    carolija = Oruzje("Carolija", "carolija")
    for heroj in heroji:
        if isinstance(heroj, Carobnjak):
            heroj.uzmi_oruzje(carolija)
        elif isinstance(heroj, Ratnik):
            oruzje = Oruzje("Koplje" if random.random() < 0.5 else "Mac", "koplje" if random.random() < 0.5 else "mac")
            heroj.uzmi_oruzje(oruzje)
    return random.sample(heroji, 2)