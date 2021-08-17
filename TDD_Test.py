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
        '''
        Description:
            this function use to check the feet value is equal to 12
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = TDD_main.feet_Analyser.calculate_inch(1)
        self.assertEqual(inch,12)

    def test_Feet_Sad(self):
        '''
        Description:
            the function is use to check the feet is not equal to 12 then raise the exception
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = TDD_main.feet_Analyser.calculate_inch(2)
        with self.assertRaises(Exception):
            self.assertEqual(inch, 'False')

    def test_feet_null_Happy(self):
        '''
        Description:
            the function is use to check the null value if not zero then pass
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = object.equal(0)
        self.assertEqual(inch,False)

    def test_feet_null_sad(self):
        '''
        Description:
            this function is use to check the null value if equal to zero then raise the error
        Parameter:
            self as a parameter
        Return:
            none
        '''
        inch = object.equal(3)
        with self.assertRaises(Exception):
            self.assertEqual(inch , 'True')

    def test_feet_reference_Happy(self):
        '''
        Description:
            this function is use to check the refrence of the object
        Parameter:
            self parameter
        Return:
            none
        '''
        obj = TDD_main.feet_Analyser()
        reference = object.reference(obj)
        self.assertEqual(reference, True)

    def test_feet_reference_Sad(self):
        '''
        Description:
            this function is use to check the refrence of object if not matched then raise the error
        Parameter:
            self parameter
        Return:
            none
        '''
        obj = TDD_main.feet_Analyser()
        reference = object.reference('object')
        with self.assertRaises(Exception):
            self.assertEqual(reference, 'False')

if __name__ == '__main__':
    unittest.main()