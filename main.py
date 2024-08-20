class Animal():
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def make_sound(self):
        print("The animal sounds")
    def eat(self):
        print("The animal eats")
    def sleep(self):
        print("The animal sleeps")
    def move(self):
        print("The animal moves")
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_color(self):
        return self.color
    def __str__(self):
        return self.name

class Bird(Animal):
    def __init__(self, name, age, color, wingspan):
        super().__init__(name, age, color)
        self.wingspan = wingspan
    def make_sound(self):
        print("The bird chirps")
    def move(self):
        print("The bird flies")
    def get_wingspan(self):
        return self.wingspan
    def __str__(self):
        return super().__str__() + " " + str(self.wingspan