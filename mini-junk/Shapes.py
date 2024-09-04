class Shape:
    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.name = name

class Circle(Shape):
    pi = 3.14159

    def __init__(self, x, y, color, name, radius):
        super().__init__(x, y, color, name)
        self.radius = radius

    def calculate_area(self):
        return self.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, x, y, color, name, side_length):
        super().__init__(x, y, color, name)
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

class Rectangle(Shape):
    def __init__(self, x, y, color, name, width, height):
        super().__init__(x, y, color, name)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

circle = Circle(0, 0, "red", "Circle", 5)
square = Square(0, 0, "blue", "Square", 4)
rectangle = Rectangle(0, 0, "green", "Rectangle", 3, 6)

print(f"Povrsina kruga: {circle.calculate_area()}")
print(f"Povrsina kvadrata: {square.calculate_area()}")
print(f"Povrsina pravougaonika: {rectangle.calculate_area()}")




