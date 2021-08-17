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

if __name__ == "__main__":
    object=yaard_analyser()
    yard = int(input("enter yard value"))
    feet = int(input("enter feet value"))
    yaard_analyser.three_feet_equal_to_one_yard(feet,yard)