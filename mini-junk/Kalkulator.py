class Kalkulator:
    def __init__(self , a , b):
        self.a = a
        self.b = b

    def saberi(self):
        return (self.a + self.b)
    def oduzmi(self):
        return (self.a - self.b)
    def pomnozi(self):
        return (self.a * self.b)
    def podijeli(self):
        return (self.a / self.b)

a = int(input("Unesite broj: "))
b = int(input("Unesite 2 broj: "))

calculator = Kalkulator(a , b)
print(calculator.saberi())
print(calculator.oduzmi())
print(calculator.pomnozi())
print(calculator.podijeli())