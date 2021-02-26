from observer import Observer


class DisplayElement:
    def display(self):
        raise NotImplementedError("display() not implemented")


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self):
        self.temperature = None
        self.humidity = None

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature} C degrees and {self.humidity} humidity")

