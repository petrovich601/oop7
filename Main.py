# Реализация проекта "Вендинговый автомат"

from Hot_Drink import *
from Vending_machine import *

drink1 = Hot_Drink('cappuccino', 67, 200)
drink2 = Hot_Drink('espresso', 42, 150)
drink3 = Hot_Drink('latte', 70, 200)

list_drink = Vending_machine()
list_drink.add_drink(drink1)
list_drink.add_drink(drink2)
list_drink.add_drink(drink3)
# list_drink.print()
# list_drink.del_drink(drink1)
# list_drink.print()
list_drink.find_drink('cappuccino')

