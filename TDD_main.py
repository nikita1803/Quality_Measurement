
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

    def zerofeet(value):
        '''
        Description:
            zerofeet is a function which is use to check 0 feet equal to 0 feet
        Parameter:
            value is a parameter
        Return:
            boolean value
        '''
        try:
            if(value==0):
                raise Exception
            else:
                inch = 12* value
                print(inch)
                return True
        except Exception:
            print("please enter a non zero value")
            return False

    
    def equal(value):
        '''
        Description:
            equal function is use to check the value is equal or non equal to zero
        Parameter:
            calue as a parameter
        Return:
            boolean value
        '''
        try:
            if(value!=0):
                return True
            elif (value==0):
                raise Exception
        except Exception:
            print("Value is none")
            return False

    def reference(obj1):
        '''
        Description:
            refrence is a parameter which is use to check the refrence of the object
        Parameter:
            object is passes as an argument to which we have to check the refrence
        Return:
            boolean value
        '''
        try:
            if(isinstance(obj1,feet_Analyser)):
                return True
            else:
                raise Exception
        except Exception:
            print("refrence is not matched")
            return False

    def Type(value):
        '''
        Description:
            type is a function which is use to check the value type 
        Parameter:
            value as an argument
        Return:
            boolean value
        '''
        try:
            if (type(value) == int):
                print("Is a number")
                return True
            else:
                raise Exception
        except Exception:
            print("another type of data")
            return False

class inch_Analyser(feet_Analyser):
    '''
    Description:
        test inch is class which is use to check all the inch related logic(null, refrence, type , equals)
    Methods: 
        zerofeet
        refrence  
    '''
    def zeroinch(value):
        '''
        Description:
            zero inch is a function which is use check the value is zeo or non zero
        Parameter:
            value as an argument
        Return:
            boolean value
        '''
        try:
            if(value==0):
                raise Exception
            else:
                feet = value / 12
                print(feet)
                return True
        except Exception:
            print("please enter a non zero value")
            return False

    def reference(obj2):
        '''
        Description:
            refrence function is use to check the refrence of the object  
        Parameter:
            object is passes as an argument
        Return:
            boolean value
        '''
        try:
            if(isinstance(obj2,inch_Analyser)):
                return True
            else:
                raise Exception
        except Exception:
            print("refrence is not matched")
            return False
            
    def zero_feet_equal_to_zero_inch(inch,feet):
        '''
        Description:
            this function is use to check the zero feet equals to zero inch
        Parameter:
            inch and feet is passes as an argument
        Return:
            boolean value
        '''
        try:
            if(feet==inch==0):
                raise Exception
            else:
                return True
        except Exception:
            print("please enter a nonzero value")
            return False

class comparing_length:
    '''
    Description:
        comparing length is class which is use to check 4 feet and inch type tests 
    Methods: 
        one feet not equal to one inch 
    '''
    def one_feet_not_equal_to_one_inch(feet,inch):
        '''
        Description:
            this function is use to check one feet is not equal to one inch
        Parameter:
            inch and feet is passes as an argument
        Return:
            boolean value
        '''
        try:
            if(feet==inch):
                raise Exception
            else:
                print("feet is not equal to inch")
                return True
                
        except Exception:
            print("feet can not be equal to inch ")
            return False

    def one_inch_is_not_equal_to_feet(inch,feet):
        '''
        Description:
            this function is use to check inch is equal to one feet then raise the exception if not then pass
        Parameter:
            inch and feet is passes as an argument
        Return:
            boolean value
        '''
        try:
            if(inch==feet):
                raise Exception
            else:
                print("inch is not equal to feet")
                return True
                
        except Exception:
            print("inch can't be equal feet ")
            return False

    def one_feet_equal_to_twelve_inch(feet,inch):
        '''
        Description:
            this function is use to check one feet is equal to 12 inch or not
        Parameter:
            inch and feet is passes as an argument
        Return:
            boolean value
        '''
        try:
            if(feet==12*inch):
                print("right")
                return True      
            else:
                raise Exception       
        except Exception:
            print("1 feet is equal to 12 inch  ")
            return False

    def twelve_inch_equal_to_one_feet(feet,inch):
        '''
        Description:
            this function is use to check 12 inch is equal to one feet or not
        Parameter:
            inch and feet is passes as an argument
        Return:
            boolean value
        '''
        try:
            if(12*inch==feet):
                print("right")
                return True   
            else:
                raise Exception
        except Exception:
            print("12 inches is equal to 1 feet ")
            return False       
                      
if __name__ == '__main__':
    feet = int(input("enter the feet value"))
    object1 = feet_Analyser()
    feet_Analyser.calculate_inch(feet)
    feet_Analyser.equal(feet)
    feet_Analyser.reference(object1)
    feet_Analyser.Type(feet)
    inch = int(input("Enter the inch value"))
    object2 = inch_Analyser()
    inch_Analyser.zeroinch(inch)
    inch_Analyser.equal(inch)
    inch_Analyser.reference(object2)
    inch_Analyser.Type(inch)
    inch_Analyser.zero_feet_equal_to_zero_inch(feet,inch)
    comparing_length.one_feet_not_equal_to_one_inch(feet,inch)
    comparing_length.one_inch_is_not_equal_to_feet(inch,feet)
    comparing_length.one_feet_equal_to_twelve_inch(feet,inch)
    comparing_length.twelve_inch_equal_to_one_feet(feet,inch)