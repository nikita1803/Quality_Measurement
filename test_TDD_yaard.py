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

if __name__ == '__main__':
    unittest.main()
