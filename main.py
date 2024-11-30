from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_coffe= MoneyMachine()
coffer_maker= CoffeeMaker()

menu= Menu()

is_on=True
while is_on :
    items=menu.get_items()
    choice=input((f"what do you want {items}"))
    if choice== "off":
        is_on=False
    elif choice == "report":
        coffer_maker.report()
        money_coffe.report()
    else:
        drink=menu.find_drink(choice)
        if coffer_maker.is_resource_sufficient(drink):
            if money_coffe.make_payment(drink.cost):
               coffer_maker.make_coffee(drink)