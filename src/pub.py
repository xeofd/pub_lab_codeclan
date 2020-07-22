# new class
class Pub:
    # initialize the class
    def __init__(self, name, till, drinks, food_list):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.food_list = food_list
        self._max_drunkenness = 12
        self.stock = {
            "drinks": [self.drinks], 
            "food": [self.food_list]
        }

    def find_drink(self, drink_name):
        for drink in self.drinks:
            if (drink_name == drink.name):
                return drink
    
    def find_food(self, food_name):
        for food in self.food_list:
            if food_name == food.name:
                return food

    def increase_or_decrease_cash(self, value):
        self.till += value

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        return False

    def can_sell(self, customer): 
        if (self.check_age(customer) and customer.drunkenness <= self._max_drunkenness):
            return True
        return False

    def stock_value(self):
        total = 0
        for drink in self.stock['drinks']:
            total += drink.price
    
    def add_drink(self, item):
        self.drinks.append(item)

    def add_food(self, item):
        self.food_list.append(item)
    
    # def get_out(self):
    #     string = "You are not old enough to drink! Get out of here punk!"
    #     return string