class PizzaStore:
    def __init__(self, factory):
        self.factory = factory

    def order_pizza(self, pizza_type):
        pizza = self.factory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
