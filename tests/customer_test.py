import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Fraser", 50)
    
    def test_customer_has_name(self):
        self.assertEqual(self.customer.name, "Fraser")

    def test_customer_has_wallet_value(self):
        pass
