class FlyBehaviour:
    def fly(self):
        raise NotImplementedError("Did not implement fly() in subclass")


class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("I am flying!!")


class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("I can't fly")