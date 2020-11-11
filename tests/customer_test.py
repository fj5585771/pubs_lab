import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Fraser", 50, 18)
        self.drink = Drink("Bevvy", 5)
    
    def test_customer_has_name(self):
        self.assertEqual(self.customer.name, "Fraser")

    def test_customer_has_wallet_value(self):
        self.assertEqual(self.customer.wallet, 50)

    def test_customer_pays_for_drink(self):
        self.customer.pay_for_drink(self.drink.price)
        self.assertEqual(45, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(self.customer.age, 18)