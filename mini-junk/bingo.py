import random

class BingoIgra:
    def igraj(self):
        igraci = {}  
        broj_igraca = int(input("Unesite broj igraca: "))

        for i in range(broj_igraca):
            ime_igraca = input(f"Unesite ime {i + 1}. igraca: ")
            brojevi = set()
            for j in range(5):
                while True:
                    broj = int(input(f"{ime_igraca}, unesite jedinstveni broj (1-48) za {j+1}. broj: "))
                    if broj < 1 or broj > 48:
                        print("Broj van opsega. Unesite broj između 1 i 48.")
                        continue
                    if broj in brojevi:
                        print("Vec ste uneli taj broj. Unesite jedinstveni broj.")
                        continue
                    brojevi.add(broj)
                    break

            igraci[ime_igraca] = brojevi

        izvuceni_brojevi = set()
        while len(izvuceni_brojevi) < 5:
            broj = random.randint(1, 48)
            if broj not in izvuceni_brojevi:
                izvuceni_brojevi.add(broj)

        print("\nIzvuceni brojevi su:", list(izvuceni_brojevi))

        pobjednici = []
        for igrac in igraci:
            pogoci = igraci[igrac].intersection(set(izvuceni_brojevi))
            if len(pogoci) == 5:
                print(f"BINGO! {igrac} je pogodio sve brojeve!")
                pobjednici.append(igrac)
            else:
                print(f"{igrac} je pogodio brojeve: {pogoci}")

        if pobjednici:
            print("Pobjednici su:", pobjednici)
        else:
            print("Nema pobjednika.")

igra = BingoIgra()
igra.igraj()
