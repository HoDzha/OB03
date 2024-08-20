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


    def __str__(self):
        return self.name