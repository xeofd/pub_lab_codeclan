import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
#from src.food import Food

# new class
class TestPub(unittest.TestCase):
    
    def setUp(self):
        # set up customers
        self.customer_1 = Customer('Jarrod', 50.00)
        self.customer_2 = Customer('Ally', 45)

        # set up drinks list
        self.drink_1 = Drink('Redbull Vodka', 5.00)
        self.drink_2 = Drink('Mojito', 3.50)
        self.drinks = []
        self.drinks.append(self.drink_1)
        self.drinks.append(self.drink_2)

        # set up pub
        self.pub = Pub("Prancing Pony", 100.00, self.drinks)

    # test functions
    def test_pub_has_name(self):
        name = self.pub.name
        self.assertEqual('Prancing Pony', name)

    def test_customer_has_name(self):
        name = self.customer_1.name 
        self.assertEqual("Jarrod", name)  

    def test_drink_has_price(self):
        price = self.drink_1.price
        self.assertEqual(5.00, price)

    def test_customer_buys_drink(self):
        self.customer_1.buy_drink(self.pub,'Mojito')
        self.assertEqual(46.50, self.customer_1.wallet)
        self.assertEqual(103.50, self.pub.till)