from coffee_maker import CoffeeMaker
from menu import MenuItem, Menu
from money_machine import MoneyMachine

menu = Menu()
coffeMaker = CoffeeMaker()
profit = MoneyMachine()
while True:
    choice = input(f"What would you like? {menu.get_items()} ").lower()
    if choice =="report":
        coffeMaker.report()
    elif choice == "off":
        break
    else:
        is_resource_sufficient = coffeMaker.is_resource_sufficient(choice)
        if is_resource_sufficient:
            coffeMaker.make_coffee(choice)
        elif not is_resource_sufficient:
            print(is_resource_sufficient)
        else:
            pass