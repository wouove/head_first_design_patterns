from beverage import Beverage


class CondimentDecorator(Beverage):
    def get_description(self):
        pass

    def cost(self):
        pass


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return f'{self.beverage.get_description()}, Mocha'

    def cost(self):
        return 0.2 + self.beverage.cost()


class SteamedMilk(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return f'{self.beverage.get_description()}, Steamed Milk'

    def cost(self):
        return 0.1 + self.beverage.cost()


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return f'{self.beverage.get_description()}, Soy'

    def cost(self):
        return 0.15 + self.beverage.cost()


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return f'{self.beverage.get_description()}, Whip'

    def cost(self):
        return 0.1 + self.beverage.cost()
