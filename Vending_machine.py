from Hot_Drink import *
from Vending_machine import *


class Vending_machine:
    def __init__(self):
        list = []
        self._list = list

    def add_drink(self, drink):
        self._list.append(drink)

    def del_drink(self, drink):
        self._list.remove(drink)

    def print(self):
        for el in self._list:
            print(str(el))

    def find_drink(self, name):
        for el in self._list:
            f = str(el).find(name)
            if f == 10:
                print(str(el))
