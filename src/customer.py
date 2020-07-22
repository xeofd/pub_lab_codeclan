from src.pub import Pub

# new class
class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    
    def buy_drink(self, pub, drink_name):
        drink = pub.find_drink(drink_name)
        self.wallet -= drink.price
        pub.increase_or_decrease_cash(drink.price)
