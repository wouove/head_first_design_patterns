class Subject:
    def register_observer(self, observer):
        raise NotImplementedError("register_oberserver not implemented")

    def remove_observer(self, observer):
        raise NotImplementedError("remove_oberserver not implemented")

    def notify_observers(self):
        raise NotImplementedError("notify_oberservers not implemented")


class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure



