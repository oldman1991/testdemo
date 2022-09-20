# coding: utf-8
""" 
@author: lipeng
@file: 0095_command_pattern.py 
@time: 2019/12/28
"""
from abc import ABCMeta, abstractmethod
import unittest

"""

"""


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")


class LightOnCommand(Command):
    def __init__(self, light):
        self.light: Light = light

    def execute(self):
        self.light.on()


class GarageDoor():
    def open(self):
        print("Door is Open")

    def close(self):
        print("Door is Close")


class GarageDoorOnCommand(Command):

    def __init__(self, garage_door):
        self.garage_door: GarageDoor = garage_door

    def execute(self):
        self.garage_door.open()


class SimpleRemoteControl:
    command: Command

    def set_command(self, command: Command):
        self.command = command

    def button_was_pressed(self):
        self.command.execute()


class TestRemoteControl(unittest.TestCase):
    def test_light(self):
        simple_remote_control: SimpleRemoteControl = SimpleRemoteControl()
        light = Light()
        light_on = LightOnCommand(light)
        simple_remote_control.set_command(light_on)
        simple_remote_control.button_was_pressed()

    def test_garage_door(self):
        simple_remote_control: SimpleRemoteControl = SimpleRemoteControl()
        garage_door = GarageDoor()
        garage_door_on_command = GarageDoorOnCommand(garage_door)
        simple_remote_control.set_command(garage_door_on_command)
        simple_remote_control.button_was_pressed()