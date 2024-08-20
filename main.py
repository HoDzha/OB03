
import pickle


# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        return f"{self.name} is eating."


# Подкласс Bird
class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def make_sound(self):
        return f"{self.name} sings."


# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return f"{self.name} roars."


# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        return f"{self.name} hisses."


# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


# Класс Zoo, использующий композицию
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, person):
        self.staff.append(person)

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)


# Класс сотрудника ZooKeeper
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        return f"{self.name} feeds {animal.name}."


# Класс сотрудника Veterinarian
class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        return f"{self.name} heals {animal.name}."


# Пример использования
if __name__ == "__main__":
    # Создание животных
    parrot = Bird("Polly", 3, "Parrot")
    lion = Mammal("Simba", 5, "Golden")
    snake = Reptile("Kaa", 2, "Smooth")

    # Создание сотрудников
    keeper = ZooKeeper("John")
    vet = Veterinarian("Dr. Smith")

    # Создание зоопарка
    zoo = Zoo()
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)
zoo.add_staff(keeper)
zoo.add_staff(vet)

# Демонстрация полиморфизма
animal_sound(zoo.animals)

# Сохранение и загрузка состояния зоопарка
zoo.save_to_file("zoo_data.pkl")
loaded_zoo = Zoo.load_from_file("zoo_data.pkl")

# Проверка загруженных данных
for animal in loaded_zoo.animals:
    print(animal.make_sound())
for staff in loaded_zoo.staff:
    if isinstance(staff, ZooKeeper):
        print(staff.feed_animal(parrot))
    elif isinstance(staff, Veterinarian):
        print(staff.heal_animal(lion))
