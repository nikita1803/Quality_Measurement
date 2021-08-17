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
object1 = TDD_main.inch_Analyser
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

    def test_feet_type_Happy(self):
        '''
        Description:
            this function is use to check the type of the data 
        Parameter:
            self parameter
        Return:
            none
        '''
        feet=1
        type= object.Type(feet)
        self.assertEqual(type,True)
    
    def test_feet_type_Sad(self):
        '''
        Description:
            this function is use to check the type if not match then raise the exception
        Parameter:
            self parameter
        Return:
            none
        '''
        feet=1.1
        type= object.Type(feet)
        with self.assertRaises(Exception):
            self.assertEqual(type,True)

    def test_zero_feet_Sad(self):
        '''
        Description:
            this function is use to check if user input is zero then raise the error
        Parameter:
            self parameter
        Return:
            none
        '''
        feet = TDD_main.feet_Analyser.zerofeet(0)
        with self.assertRaises(Exception):
            self.assertEqual(feet, 'False')

    def test_zero_feet_Happy(self):
        '''
        Description:
            this function is use to check if user input non zero then  pass the case
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = object.zerofeet(3)
        self.assertEqual(inch , True)

class TestInch(unittest.TestCase):

    def test_inch_null_Sad(self):
        '''
        Description:
            this function is use to check null value , if null value is there then it raises the exception 
        Parameter:
            self parameter
        Return:
            none
        '''
        inch =TDD_main.inch_Analyser.equal(0)
        with self.assertRaises(Exception):
            self.assertEqual(inch,'False')

    def test_inch_null_Happy(self):
        '''
        Description:
            this function is use to check null value , if not then it passes the case 
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = TDD_main.inch_Analyser.equal(3)
        self.assertEqual(inch , True)

    def test_inch_reference_Happy(self):
        '''
        Description:
            this function is use to check refrence of the object , if match then pass the case
        Parameter:
            self parameter
        Return:
            none
        '''
        obj = TDD_main.inch_Analyser()
        reference = object1.reference(obj)
        self.assertEqual(reference, True)

    def test_inch_reference_Sad(self):
        '''
        Description:
            this function is use to check refrence of the object if not match then raise the error 
        Parameter:
            self parameter
        Return:
            none
        '''
        obj = TDD_main.inch_Analyser()
        reference = object1.reference('object')
        with self.assertRaises(Exception):
            self.assertEqual(reference, 'False')

    def test_inch_type_Happy(self):
        '''
        Description:
            this function is use to check type of the data if not match then pass the case
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = 1
        type= object.Type(inch)
        self.assertEqual(type,True)
    
    def test_inch_type_Sad(self):
        '''
        Description:
            this function is use to check type of the data if not match then raise the error 
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = 1.1
        type= object.Type(inch)
        with self.assertRaises(Exception):
            self.assertEqual(type,True)

    def test_zero_inch_Sad(self):
        '''
        Description:
            this function is use to check zero inch is equal to zero then raise the exception
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = TDD_main.inch_Analyser.zeroinch(0)
        with self.assertRaises(Exception):
            self.assertEqual(inch, 'False')

    def test_zero_inch_Happy(self):
        '''
        Description:
            this function is use to check non zero value then pass the test case
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = object1.zeroinch(3)
        self.assertEqual(inch , True)
    
    def test_feet_not_equal_inch_Sad(self):
        '''
        Description:
            this function is use to check one feet not equal to one inch , if equal then raise the exception
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = TDD_main.comparing_length.one_feet_not_equal_to_one_inch(1,1)
        with self.assertRaises(Exception):
            self.assertEqual(inch, 'False')

    def test_feet_not_equal_inch_Happy(self):
        '''
        Description:
            this function is use to check if one feet is not equal to one inch then pass the case
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = TDD_main.comparing_length.one_feet_not_equal_to_one_inch(1,12)
        self.assertEqual(inch , True)

    def test_feet_not_equal_inch_Sad(self):
        '''
        Description:
            this function is use to check one feet not equal to one inch , if equal then raise the exception
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = TDD_main.comparing_length.one_feet_not_equal_to_one_inch(1,1)
        with self.assertRaises(Exception):
            self.assertEqual(inch, 'False')

    def test_feet_not_equal_inch_Happy(self):
        '''
        Description:
            this function is use to check if one feet is not equal to one inch then pass the case
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = TDD_main.comparing_length.one_feet_not_equal_to_one_inch(1,12)
        self.assertEqual(inch , True)

    def test_inch_not_equal_feet_Sad(self):
        '''
        Description:
            this function is use to check if inch is equal to feet then raise the exception
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = TDD_main.comparing_length.one_inch_is_not_equal_to_feet(1,1)
        with self.assertRaises(Exception):
            self.assertEqual(inch, 'False')

    def test_inch_not_equal_feet_Happy(self):
        '''
        Description:
            this function is use to check if inch not equal to feet then pass the test case 
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = TDD_main.comparing_length.one_inch_is_not_equal_to_feet(1,12)
        self.assertEqual(inch , True)

    def test_twelve_inch_equal_one_feet_Sad(self):
        '''
        Description:
            this function is use to check 12 inch is not equal to one feet then it raise the exception
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = TDD_main.comparing_length.one_feet_equal_to_twelve_inch(1,1)
        with self.assertRaises(Exception):
            self.assertEqual(inch, 'False')

    def test_twelve_inch_equal_one_feet_Happy(self):
        '''
        Description:
            this function is use to check if 12 inch equal to 1 feet then it passes the caseS 
        Parameter:
            self parameter
        Return:
            none
        '''
        inch = TDD_main.comparing_length.one_feet_equal_to_twelve_inch(12,1)
        self.assertEqual(inch , True)

if __name__ == '__main__':
    unittest.main()