class ChocolateBoiler:
    __instance__ = None

    def __init__(self):
        if ChocolateBoiler.__instance__ is None:
            ChocolateBoiler.__instance__ = self
            self.empty = True
            self.boiled = False
        else:
            raise Exception('Instance already created')

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
        """
        if not ChocolateBoiler.__instance__:
            ChocolateBoiler()
        return ChocolateBoiler.__instance__

    def fill(self):
        if self.empty:
            print("Filling the boiler")
            self.empty = False
            self.boiled = False

    def drain(self):
        if not self.empty:
            print("Draining the boiler")
            self.empty = True

    def boil(self):
        if not self.empty and not self.boiled:
            print("Bringing the contents to a boil")
            self.boiled = True
