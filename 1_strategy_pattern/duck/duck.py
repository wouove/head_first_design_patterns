from fly_behaviour import FlyWithWings
from quack_behaviour import Quack


class Duck:
    def __init__(self, fly_behaviour, quack_behaviour):
        self.fly_behaviour = fly_behaviour
        self.quack_behaviour = quack_behaviour

    def display(self):
        raise NotImplementedError("display() not implemented")

    def perform_fly(self):
        self.fly_behaviour.fly(self)

    def perform_quack(self):
        self.quack_behaviour.quack(self)


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings, Quack)

    def display(self):
        print("I am a real Mallard duck")