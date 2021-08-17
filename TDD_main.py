
'''
@Author: Nikita Rai
@Date: 2021-02-16 3:00:30
@Last Modified by: Nikita Rai
@Last Modified time: 2021-02-16 9:00:30
@Title : Quality Measurement
'''
from logging import exception
from unittest.case import expectedFailure

class feet_Analyser:
    '''
    Description:
        test feet is class which is use to check all the feet related logic(null, refrence, type , equals)
    Methods: 
        calculate_inch
        zerofeet
        equal
        refrence
        type  
    '''
    def calculate_inch(feet):
        '''
        Description:
            Calculate inch is a function which is use to calculate the inch 
        Parameter:
            feet passes as a parameter
        Return:
            none
        '''
        inch = 12*feet
        print("length in inches",round(inch,2))
        try:
            if(inch==12):
                print("Data match")
                return inch
            else:
                raise Exception
        except Exception:
            print("Data not matched")
                  
if __name__ == '__main__':
    feet = int(input("enter the feet value"))
    object1 = feet_Analyser()
    feet_Analyser.calculate_inch(feet)