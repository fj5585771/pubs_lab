import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Wee Dram", 1000)

    def test_pub_has_name(self):
        self.assertEqual(self.pub.name, "The Wee Dram") 

    def test_pub_has_till_amount(self):
        self.assertEqual(self.pub.till, 1000) 





    


    # def test_till_has_updated(self):
    # self.pub.update_till(self.pub.till)
    # self.assertEqual(45, self.customer.wallet)