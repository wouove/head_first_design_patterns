from abc import ABC, abstractmethod
from ingredient import ThinCrustDough, MarinaraSauce, ReggianoCheese, Garlic, Onion, Mushroom, RedPepper, \
    SlicedPepperoni, FreshClams


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_veggies(self):
        pass

    @abstractmethod
    def create_pepperoni(self):
        pass

    @abstractmethod
    def create_clam(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClams()