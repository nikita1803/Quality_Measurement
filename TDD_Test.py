'''
@Author: Nikita Rai
@Date: 2021-02-16 3:00:30
@Last Modified by: Nikita Rai
@Last Modified time: 2021-02-16 9:00:30
@Title : Quality Measurement unit test
'''
from logging import NullHandler
import unittest
import TDD_main

object = TDD_main.feet_Analyser
class TestFeet(unittest.TestCase):

    def test_Feet_Happy(self):
        inch = TDD_main.feet_Analyser.calculate_inch(1)
        self.assertEqual(inch,12)

    def test_Feet_Sad(self):
        inch = TDD_main.feet_Analyser.calculate_inch(2)
        with self.assertRaises(Exception):
            self.assertEqual(inch, 'False')

    def test_feet_null_Happy(self):
        inch = object.equal(0)
        self.assertEqual(inch,False)

    def test_feet_null_sad(self):
        inch = object.equal(3)
        with self.assertRaises(Exception):
            self.assertEqual(inch , 'True')

if __name__ == '__main__':
    unittest.main()