import random

def Igraj():
    
    lista_kutija = [10, 20, 50, 100, 150, 200, 250, 1000, "novi zivot", "prazna", "prazna", "prazna"]
    random.shuffle(lista_kutija)
    print(lista_kutija)
    zauzete_kutije = []
    banka = 0
    novi_zivot = 0
    broj_kutija = 12
    broj_pogodjenih_kutija_sa_novcem = 0

    is_game_on = True

    while is_game_on:
        odabir = input(f"Odaberite slobodnu kutiju: (1-{broj_kutija}) ili napisite exit za izlaz iz igrice. Zauzete kutije su: {zauzete_kutije} ")
        if odabir == "exit":
                    banka += 50
                    print(f"Zaustavili ste igru i osvojili dodatni bonus od 50 KM. Ukupno ste osvojili {banka} KM, čestitamo! ")
                    is_game_on = False
        else:
             while int(odabir) not in zauzete_kutije and broj_pogodjenih_kutija_sa_novcem < 8: 
                odabir = int(odabir)
                zauzete_kutije.append(odabir)
                if type(lista_kutija[odabir - 1]) == int:
                        banka += int(lista_kutija[odabir - 1])
                        print(f"Čestitamo, osvojili ste {lista_kutija[odabir - 1]} KM. \nVasa trenutna banka iznosi: {banka} KM")
                        if broj_pogodjenih_kutija_sa_novcem == 7:
                            print(f"Igra je zavrsena, osvojio si {banka} KM! Čestitamo.")
                            is_game_on = False
                            break
                        broj_pogodjenih_kutija_sa_novcem += 1
                elif lista_kutija[odabir - 1] == "prazna":
                    if novi_zivot == 0:
                        print("Nazalost izgubili ste sve, vise srece drugi put!")
                        is_game_on = False
                    else:
                        banka //= 2
                        print(f"Iskoristili ste novi zivot. Vasa banka se umanjila za polovinu i trenutno iznosi: {banka} KM!")
                        novi_zivot -= 1
                        lista_kutija.remove("novi zivot")
                        broj_kutija -= 1
                        zauzete_kutije.clear()
                        random.shuffle(lista_kutija)
                        break
                else:
                    print("Osvojio si novi zivot")
                    novi_zivot += 1
                    break
while True:
    Igraj()
    nova_igra = int(input("Ako zelite da zapocnete novu igru pritisnite 1: "))
    if nova_igra == 1:
        continue
    else:
        break