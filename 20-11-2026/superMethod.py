# super() method


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {(3.14 * self.radius * self.radius):.2f}cm^2")
        super().describe() # Adds the superclass method as well

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {(self.width * self.width):.2f}cm^2")
        super().describe() # Adds the superclass method as well

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {(self.width * self.height / 2):.2f}cm^2")
        super().describe() # Adds the superclass method as well

circle = Circle(color="Red", is_filled=True, radius=6)
circle.describe()

square = Square(color="Blue", is_filled=False, width=5.5)
square.describe()

triangle = Triangle(color="Yellow", is_filled=True, width=3.3, height=5.5)
triangle.describe()
