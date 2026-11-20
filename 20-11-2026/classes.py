# Python Object Oriented Programming

class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def show_model(self):
        print(self.model)

    def show_year(self):
        print(self.year)

    def show_color(self):
        print(self.color)

tata = Car(model="Punch", year=2026, color="Black")

tata.show_color()