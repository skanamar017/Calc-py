import math

## Class
class Calculator:   

## Constructor
    def __init__(self): 
        self.display_val = 0

## Start of Core Methods (functions)
    def add(self, x): 
        result = self.display_val + x
        self.display_val = result
        return result

    def sub(self, x):
        result = self.display_val - x
        self.display_val = result
        return result

    def multiply(self, x):
        result = self.display_val * x
        self.display_val = result
        return result
    
    def divide(self, x):
        result = self.display_val / x
        self.display_val = result
        return result
    
    def square_rt(self,):
        # Is the current display in an error state already?
        if self.display_val < 0:

        # If yes → do nothing (or signal that the error must be cleared).
            self.display_val = 'err'
            return
                
        result = math.sqrt(self.display_val)
        self.display_val = result                
        return result
    
    def square(self):
        result = self.display_val ** 2
        self.display_val = result
        return result
    


    
    def clear(self):
        self.display_val = 0

    

    

    

# add lots more methods to this calculator class.

