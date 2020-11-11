import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Bevvy", 5)
    
    #test a drink object to check it has a name by referring to the price attribute of the drink object
    
    def test_has_drink(self):
        self.assertEqual(self.drink.price, 5) 
    