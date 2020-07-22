import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
#from src.food import Food

# new class
class TestPub(unittest.TestCase):
    
    def setUp(self):
        # set up customers
        self.customer_1 = Customer('Jarrod', 50.00, 17)
        self.customer_2 = Customer('Ally', 45, 40)

        # set up drinks list
        self.drink_1 = Drink('Redbull Vodka', 5.00, 3)
        self.drink_2 = Drink('Mojito', 3.50, 2)
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

    def test_customer_buys_drink_pass(self):
        self.customer_2.buy_drink(self.pub, 'Mojito')
        self.assertEqual(41.5, self.customer_2.wallet)
        self.assertEqual(103.50, self.pub.till)

    def test_customer_buys_drink_fail(self):
        fail_message = "You are not old enough to drink! Get out of here punk!"
        self.assertEqual(None, self.customer_1.buy_drink(self.pub,'Mojito'))
        # We wanted a message printed in method get_out but could not get it to work.

    def test_check_age_pass(self):
        customer = self.customer_2
        self.assertEqual(True, self.pub.check_age(customer))

    def test_check_age_fail(self):
        customer = self.customer_1
        self.assertEqual(False, self.pub.check_age(customer))

    #def test
    

    
