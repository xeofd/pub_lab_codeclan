# new class
class Pub:
    # initialize the class
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def find_drink(self, drink_name):
        for drink in self.drinks:
            if (drink_name == drink.name):
                return drink
    
    def increase_or_decrease_cash(self, value):
        self.till += value