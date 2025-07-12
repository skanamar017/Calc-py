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
    
    def clear(self):
        self.display_val = 0
    

# add lots more methods to this calculator class.

