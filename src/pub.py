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

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        return False

    def can_sell(self, customer): 
        if (self.check_age(customer)):
            return True
        return False
    
    def get_out(self):
        string = "You are not old enough to drink! Get out of here punk!"
        return string