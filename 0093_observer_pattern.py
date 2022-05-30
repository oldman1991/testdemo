# coding: utf-8
""" 
@author: lipeng
@file: 0093_observer_pattern.py 
@time: 2019/12/23
"""
from abc import ABCMeta, abstractmethod
import unittest

"""
观察者模式
观察者模式定义了对象之间的一对多依赖，这样一来，当一个对象改变状态时，
它的所有依赖着都会收到通知并自动更新
"""


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, temp, humidity, pressure):
        pass


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def register_observer(self, o: Observer):
        pass

    @abstractmethod
    def remove_observer(self, o: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class DisplayElement(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        self.observers: set[Observer] = set()
        self.temp = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, o: Observer):
        self.observers.add(o)

    def remove_observer(self, o: Observer):
        if o in self.observers:
            self.observers.remove(o)

    def notify_observers(self):
        for observe in self.observers:
            observe.update(self.temp, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_weather_data(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


class CurrentConditionsDisplay(Observer, DisplayElement):
    pressure: object
    humidity: object
    temp: object

    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print(f"Current conditions:{self.temp}, degrees and {self.humidity},")


class TestWeatherStation(unittest.TestCase):
    def test_weather_station(self):
        weather_data = WeatherData()
        CurrentConditionsDisplay(weather_data)
        weather_data.set_weather_data(2, 3, 5)
