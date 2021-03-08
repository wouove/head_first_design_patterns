from abc import ABC, abstractmethod
from pizza import CheesePizza, ClamPizza
from pizza_ingredients import NYPizzaIngredientFactory


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
        ingredients_factory = NYPizzaIngredientFactory()
        if pizza_type == 'cheese':
            pizza = CheesePizza(ingredients_factory)
            pizza.name = "New York Style Cheese Pizza"
        # if pizza_type == 'pepperoni':
        #     pizza = NYStylePepperoniPizza()
        if pizza_type == 'clam':
            pizza = ClamPizza(ClamPizza)
            pizza.name = "New York Style Clam Pizza"
        # elif pizza_type == 'veggie':
        #     pizza = NYStyleVeggiePizza()
        return pizza


# class ChicagoStylePizzaStore(PizzaStore):
#     def create_pizza(self, pizza_type):
#         pizza = None
#         if pizza_type == 'cheese':
#             pizza = ChicagoStyleCheesePizza()
#         # if pizza_type == 'pepperoni':
#         #     pizza = ChicagoStylePepperoniPizza()
#         # if pizza_type == 'clam':
#         #     pizza = ChicagoStyleClamPizza()
#         # elif pizza_type == 'veggie':
#         #     pizza = ChicagoStyleVeggiePizza()
#         return pizza
