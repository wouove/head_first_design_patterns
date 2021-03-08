from abc import ABC, abstractmethod

class Pizza(ABC):
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")


class CheesePizza(Pizza):
    def __init__(self, ingredients_factory):
        self.ingredients_factory = ingredients_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredients_factory.create_dough()
        self.sauce = self.ingredients_factory.create_sauce()
        self.cheese = self.ingredients_factory.create_cheese()


class ClamPizza(Pizza):
    def __init__(self, ingredients_factory):
        self.ingredients_factory = ingredients_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredients_factory.create_dough()
        self.sauce = self.ingredients_factory.create_sauce()
        self.cheese = self.ingredients_factory.create_cheese()
        self.clam = self.ingredients_factory.create_clam()