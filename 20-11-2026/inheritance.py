# Inheritance

class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):

    def can_bark(self):
        print(f"Yes, {self.name} is a dog, Hence he can bark!")

class Cat(Animal):

    def can_meow(self):
        print(f"Yes, {self.name} is a cat, Hence she can meow!")

class Mouse(Animal):

    def can_speak(self):
        print(f"I don't know, {self.name} is a mouse, Never seen them speak!")

dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")

dog.eat()
dog.sleep()
dog.can_bark()

cat.eat()
cat.sleep()
cat.can_meow()

mouse.eat()
mouse.sleep()
mouse.can_speak()
