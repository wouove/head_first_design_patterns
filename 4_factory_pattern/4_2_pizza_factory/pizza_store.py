from abc import ABC, abstractmethod
from pizza import NYStyleCheesePizza, ChicagoStyleCheesePizza


class PizzaStore(ABC):

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type):
        pass


class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizza = None
        if pizza_type == 'cheese':
            pizza = NYStyleCheesePizza()
        # if pizza_type == 'pepperoni':
        #     pizza = NYStylePepperoniPizza()
        # if pizza_type == 'clam':
        #     pizza = NYStyleClamPizza()
        # elif pizza_type == 'veggie':
        #     pizza = NYStyleVeggiePizza()
        return pizza


class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizza = None
        if pizza_type == 'cheese':
            pizza = ChicagoStyleCheesePizza()
        # if pizza_type == 'pepperoni':
        #     pizza = ChicagoStylePepperoniPizza()
        # if pizza_type == 'clam':
        #     pizza = ChicagoStyleClamPizza()
        # elif pizza_type == 'veggie':
        #     pizza = ChicagoStyleVeggiePizza()
        return pizza
