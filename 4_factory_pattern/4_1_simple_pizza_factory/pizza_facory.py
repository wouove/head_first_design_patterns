from pizza import CheesePizza, PepperoniPizza, ClamPizza, VeggiePizza

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        pizza = None
        if pizza_type == 'cheese':
            pizza = CheesePizza()
        if pizza_type == 'pepperoni':
            pizza = PepperoniPizza()
        if pizza_type == 'clam':
            pizza = ClamPizza()
        elif pizza_type == 'veggie':
            pizza = VeggiePizza()
        return pizza
