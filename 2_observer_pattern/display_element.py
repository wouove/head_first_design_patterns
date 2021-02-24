from oberver import Observer
from subject import WeatherData


class DisplayElement:
    def display(self):
        raise NotImplementedError("display() not implemented")


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.temperature = None
        self.humidity = None
        self.weather_data = weather_data

    