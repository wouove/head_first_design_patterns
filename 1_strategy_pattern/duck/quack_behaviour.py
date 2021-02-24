class QuackBehaviour:
    def quack(self):
        raise NotImplementedError("quack() not implemented by subclass")


class Quack(QuackBehaviour):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehaviour):
    def quack(self):
        print("<<Silence>>")


class Squeak(QuackBehaviour):
    def quack(self):
        print("Squeak")