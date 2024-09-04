from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Krug(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Pravougaonik(Shape):
    def __init__(self, sirina, visina):
        self.sirina = sirina
        self.visina = visina

    def area(self):
        return self.sirina * self.visina

    def perimeter(self):
        return 2 * (self.sirina + self.visina)

class Kocka(Shape):
    def __init__(self, stranica):
        self.stranica = stranica

    def area(self):
        return self.stranica ** 2

    def perimeter(self):
        return 4 * self.stranica


krug = Krug(5)
pravougaonik = Pravougaonik(4, 6)
kvadrat = Kocka(3)

print("Povrsina kruga:", krug.area())
print("Obim kruga:", krug.perimeter())

print("Povrsina pravougaonika:", pravougaonik.area())
print("Obim pravougaonika:", pravougaonik.perimeter())

print("Povrsina kvadrata:", kvadrat.area())
print("Obim kvadrata:", kvadrat.perimeter())