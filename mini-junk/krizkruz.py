def prikazi_tablu(tabla):
    for red in tabla:
        print(" | ".join(red))
        print("-" * 9)

def provjeri_pobjednika(tabla, igrac):
    for i in range(3):
        if tabla[i][0] == tabla[i][1] == tabla[i][2] == igrac or tabla[0][i] == tabla[1][i] == tabla[2][i] == igrac:
            return True
    if tabla[0][0] == tabla[1][1] == tabla[2][2] == igrac or tabla[0][2] == tabla[1][1] == tabla[2][0] == igrac:
        return True
    return False

def igraj_iks_oks():
    tabla = [[" " for _ in range(3)] for _ in range(3)]
    igraci = ["X", "O"]
    indeks_igraca = 0
    kraj_igre = False
    preostali_potezi = 9

    print("Dobrodošli u igru Iks Oks!")
    prikazi_tablu(tabla)

    while not kraj_igre:
        trenutni_igrac = igraci[indeks_igraca % 2]

        validan_unos = False
        while not validan_unos:
            red = input(f"Igraču {trenutni_igrac}, unesite red (0-2): ")
            kolona = input(f"Igraču {trenutni_igrac}, unesite kolonu (0-2): ")

            if red.isdigit() and kolona.isdigit():
                red = int(red)
                kolona = int(kolona)

                if 0 <= red <= 2 and 0 <= kolona <= 2 and tabla[red][kolona] == " ":
                    tabla[red][kolona] = trenutni_igrac
                    preostali_potezi -= 1
                    validan_unos = True
                else:
                    print("Pogrešan unos. Molimo unesite ispravnu poziciju.")
            else:
                print("Unesite cijeli broj između 0 i 2.")

        prikazi_tablu(tabla)

        if provjeri_pobjednika(tabla, trenutni_igrac):
            print(f"Igrač {trenutni_igrac} je pobijedio!")
            kraj_igre = True
        elif preostali_potezi == 0:
            print("Neriješeno!")
            kraj_igre = True

        indeks_igraca += 1

igraj_iks_oks()



