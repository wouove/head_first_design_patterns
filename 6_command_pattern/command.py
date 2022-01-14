from abc import abstractmethod


class Command:
    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()
