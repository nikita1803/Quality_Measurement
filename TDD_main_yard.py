'''
@Author: Nikita Rai
@Date: 2021-02-17 8:00:30
@Last Modified by: Nikita Rai
@Last Modified time: 2021-02-17 8:00:30
@Title : Quality Measurement unit test for yaard
'''
class yaard_analyser:
    '''
    Description:
        this class is created for yaard analyser. 
    Methods: 
        three feet equal to one yaard
    '''
    def three_feet_equal_to_one_yard(feet,yard):
        '''
        Description:
            this function is use to check three feet equal to one yaard or not
        Parameter:
            inch and feet is passes as an argument
        Return:
            boolean value
        '''
        try:
            if(yard!=3*feet):
                raise Exception
            else:
                print("Correct input")
                return True
        except Exception:
            print("wrong input")
            return False

    def one_feet_not_equal_to_one_yard(feet,yard):
        '''
        Description:
            this function is use to check one feet not equal to one yaard or not
        Parameter:
            yard and feet is passes as an argument
        Return:
            boolean value
        '''
        try:
            if(feet==yard):
                raise Exception
            else:
                print("feet is not equal to yard")
                return True
                
        except Exception:
            print("feet can't be equal yard ")
            return False


    def one_inch_not_equal_to_one_yard(inch,yard):
        '''
        Description:
            this function is use to check one inch not equal to one yaard 
        Parameter:
            yard and inch is passes as an argument
        Return:
            boolean value
        '''
        try:
            if(inch == yard):
                raise Exception
            else:
                print("inch is not equal to yard")
                return True
                
        except Exception:
            print("inch can't be equal yard ")
            return False

    def one_yard_equal_to_thirtysix_inch(inch,yard):
        '''
        Description:
            this function is use to check one yard equal to 36 inch
        Parameter:
            yard and feet is passes as an argument
        Return:
            boolean value
        '''
        try:
            if(yard!=36*inch):
                raise Exception
            else:
                print("Correct input")
                return True
        except Exception:
            print("wrong input")
            return False

    def thirtysix_inch_equal_to_one_yard(inch,yard):
        '''
        Description:
            this function is use to check 36 inch equal to one yaard
        Parameter:
            yard and inch is passes as an argument
        Return:
            boolean value
        '''
        try:
            if(inch!=(yard/36)):
                raise Exception
            else:
                print("Correct input")
                return True
        except Exception:
            print("wrong input")
            return False

    def one_yard_equal_to_three_feet(feet,yard):
        '''
        Description:
            this function is use to check one yard equal to three feet
        Parameter:
            yard and feet is passes as an argument
        Return:
            boolean value
        '''
        try:
            if(feet!=(yard/3)):
                raise Exception
            else:
                print("Correct input")
                return True
        except Exception:
            print("wrong input")
            return False
  
if __name__ == "__main__":
    object=yaard_analyser()
    yard = int(input("enter yard value"))
    feet = int(input("enter feet value"))
    inch = int(input("enter inch value"))
    yaard_analyser.three_feet_equal_to_one_yard(feet,yard)
    yaard_analyser.one_feet_not_equal_to_one_yard(feet,yard)
    yaard_analyser.one_inch_not_equal_to_one_yard(inch,yard)
    yaard_analyser.one_yard_equal_to_thirtysix_inch(inch,yard)
    yaard_analyser.thirtysix_inch_equal_to_one_yard(inch,yard)
    yaard_analyser.one_yard_equal_to_three_feet(feet,yard)