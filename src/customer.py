from src.pub import Pub

# new class
class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0
    
    def buy_drink(self, pub, drink_name):
        if (pub.can_sell(self)):
            drink = pub.find_drink(drink_name)
            self.wallet -= drink.price
            pub.increase_or_decrease_cash(drink.price)
            self.drunkenness += drink.alcohol_level

    def buy_food(self,pub, food_name):
        food = pub.find_food(food_name)
        self.wallet -= food.price
        pub.increase_or_decrease_cash(food.price)
        self.drunkenness -= food.rejuvenation_level
