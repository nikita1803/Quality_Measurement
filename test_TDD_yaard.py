'''
@Author: Nikita Rai
@Date: 2021-02-16 3:00:30
@Last Modified by: Nikita Rai
@Last Modified time: 2021-02-16 9:00:30
@Title : Quality Measurement unit test
'''
import unittest
import TDD_main_yard

object = TDD_main_yard.yaard_analyser
class TestFeet(unittest.TestCase):

    def test_one_yaard_equal_three_feet_Happy(self):
        '''
        Description:
            this function use to check the one yaard equal to three feet then it pass the case
        Parameter:
            self parameter
        Return:
            none
        '''
        data = TDD_main_yard.yaard_analyser.three_feet_equal_to_one_yard(3,9)
        self.assertEqual(data,True)

    def test_one_yaard_equal_three_feet_Sad(self):
        '''
        Description:
            this function use to check the one yaard equal to three feet then it raises the exception
        Parameter:
            self parameter
        Return:
            none
        '''
        data = TDD_main_yard.yaard_analyser.three_feet_equal_to_one_yard(8,4)
        with self.assertRaises(Exception):
            self.assertEqual(data,'False')
    
    def test_one_feet_not_equal_to_one_yard_Happy(self):
        '''
        Description:
            this function use to check the one feet not equal to one yaard then it pass the error
        Parameter:
            self parameter
        Return:
            none
        '''
        data = TDD_main_yard.yaard_analyser.one_feet_not_equal_to_one_yard(3,9)
        self.assertEqual(data,True)

    def test_one_feet_not_equal_to_one_yard_Sad(self):
        '''
        Description:
            this function use to check the one feet equal to one yaard the it raise the exception
        Parameter:
            self parameter
        Return:
            none
        '''
        data = TDD_main_yard.yaard_analyser.three_feet_equal_to_one_yard(2,2)
        with self.assertRaises(Exception):
            self.assertEqual(data,'False')

    def test_one_inch_not_equal_to_one_yard_Happy(self):
        '''
        Description:
            this function use to check the one inch is not equal to one yaard then it passes the case
        Parameter:
            self parameter
        Return:
            none
        '''
        data = TDD_main_yard.yaard_analyser.one_feet_not_equal_to_one_yard(3,6)
        self.assertEqual(data,True)

    def test_one_inch_not_equal_to_one_yard_Sad(self):
        '''
        Description:
            this function use to check the one one inch is equal to one yaard then it raises the error
        Parameter:
            self parameter
        Return:
            none
        '''
        data = TDD_main_yard.yaard_analyser.three_feet_equal_to_one_yard(3,3)
        with self.assertRaises(Exception):
            self.assertEqual(data,'False')

    def test_one_yard_equal_to_thirtysix_inch_Happy(self):
        '''
        Description:
            this function use to check the one yaard is equal to 36 inch then it passes the case
        Parameter:
            self parameter
        Return:
            none
        '''
        data = TDD_main_yard.yaard_analyser.one_yard_equal_to_thirtysix_inch(1,36)
        self.assertEqual(data,True)

    def test_one_yard_equal_to_thirtysix_inch_Sad(self):
        '''
        Description:
            this function use to check the one yaard is not equal to 36 then it raises the exception
        Parameter:
            self parameter
        Return:
            none
        '''
        data = TDD_main_yard.yaard_analyser.one_yard_equal_to_thirtysix_inch(1,22)
        with self.assertRaises(Exception):
            self.assertEqual(data,'False')

if __name__ == '__main__':
    unittest.main()
