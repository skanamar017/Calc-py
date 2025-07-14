import unittest
from calculator import Calculator


class TestStringMethods(unittest.TestCase):

    def test(self):
        c = Calculator() #
        self.assertEqual(c.add(3), 3)  
        self.assertEqual(c.add(-10), -7)
        self.assertEqual(c.add(8), 1)
        self.assertEqual(c.sub(3), -2)
        self.assertEqual(c.multiply(3), -6)
        self.assertEqual(c.divide(-6), 1)





if __name__ == '__main__':
    unittest.main()
