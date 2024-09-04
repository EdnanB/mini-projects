import random

kutije = [10, 20, 50, 100, 150, 200, 250, 1000, "Novi Zivot", "Prazno", "Prazno", "Prazno"]
random.shuffle(kutije)
print("Dobrodošli u igru otvaranja kutija!")

zauzete_kutije = []
totalni_dobitak = 0
novi_zivot = 0
pogodjene_kutije = 0
broj_kutija = 12

while True:
    print("\nPočetni raspored kutija:")
    for i in range(len(kutije)):
        if i + 1 in zauzete_kutije:
            if type(kutije[i]) == int or type(kutije[i]) == float:
                print(f"Kutija {i + 1}: {kutije[i]} KM")
            else:
                print(f"Kutija {i + 1}: {kutije[i]}")
        else:
            print(f"Kutija {i + 1}")

    odabir = input(f"Odaberite kutiju: (1-{broj_kutija}) ili unesite 'exit' za završetak igre. Zauzete kutije su: {zauzete_kutije} ")

    if odabir == "exit":
        if novi_zivot > 0:
            totalni_dobitak += 50
            print(f"Zaustavili ste igru i osvojili dodatni bonus od 50 KM radi dodatnog života. Ukupno ste osvojili {totalni_dobitak} KM, cestitamo! ")
        else:
            print(f"Ukupno ste osvojili {totalni_dobitak} KM. ")
        break
    else:
        odabir = int(odabir)
        if 1 <= odabir <= broj_kutija and odabir not in zauzete_kutije and pogodjene_kutije < 8:
            zauzete_kutije.append(odabir)
            if type(kutije[odabir - 1]) == int or type(kutije[odabir - 1]) == float:
                dobitak = kutije[odabir - 1]
                totalni_dobitak += dobitak
                print(f"Čestitamo, otvorili ste kutiju {odabir} i pronašli {dobitak} KM. \nVasa trenutna banka iznosi: {totalni_dobitak} KM")

                pogodjene_kutije += 1
                if pogodjene_kutije == 8:
                    print(f"Igra je završena, osvojili ste {totalni_dobitak} KM! Čestitamo.")
                    break
            elif kutije[odabir - 1] == "Prazno":
                if novi_zivot == 0:
                    print("Vi ste izgubili! I nazalost svi vasi dobitci su takodjer izgubljeni!")
                    break
                else:
                    totalni_dobitak //= 2
                    print(f"Iskoristili ste vas dodatni život. Vasa banka se umanjila za pola i iznosi: {totalni_dobitak} KM!")
                    novi_zivot -= 1
                    kutije.remove("Novi Zivot")
                    broj_kutija -= 1
                    zauzete_kutije.clear()
                    random.shuffle(kutije)
            else:
                print("Čestitamo, otvorili ste kutiju i pronašli dodatni život!")
                novi_zivot += 1
        else:
            if pogodjene_kutije >= 8:
                print(f"Igra je završena, osvojili ste {totalni_dobitak} KM! Čestitamo.")
            elif odabir in zauzete_kutije:
                print("Žao nam je, ovu kutiju ste već otvorili. Molimo vas odaberite drugu kutiju.")
            else:
                print("Nevažeći broj kutije. Molimo odaberite broj unutar raspoloživih kutija.")