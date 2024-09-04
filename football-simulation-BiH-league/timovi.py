class Tim:
    def __init__(self, ime, igraci):
        self.ime = ime
        self.igraci = igraci
        self.bodovi = 0
        self.gol_razlika = 0
        self.golovi = {}

    def __str__(self):
        return f"{self.ime} - Bodovi: {self.bodovi}, Gol razlika: {self.gol_razlika}"

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