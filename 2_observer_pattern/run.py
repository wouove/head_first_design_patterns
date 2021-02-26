from subject import WeatherData
from display_element import CurrentConditionsDisplay

if __name__ == '__main__':
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay()
    weather_data.register_observer(current_display)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(52, 44, 20.4)
    weather_data.set_measurements(73, 55, 10.4)