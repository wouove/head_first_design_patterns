from abc import ABC

class Pizza(ABC):
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Tossing dough")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self.toppings:
            print(topping)

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

# NY pizzas
class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauze"
        self.toppings = []
        self.toppings.append("Grated Reggiano Cheese")

# class NYStylePepperoniPizza(Pizza):
#
#
# class NYStyleClamPizza(Pizza):
#
#
# class NYStyleVeggiePizza(Pizza):

# Chicago pizzas
class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings = []
        self.toppings.append("Shredded Mozzerella Cheese")

    def cut(self):
        print("Cutting pizza into square slices")

# class ChicagoStylePepperoniPizza(Pizza):
#
# class ChicagoStyleClamPizza(Pizza):
#
# class ChicagoStyleVeggiePizza(Pizza):