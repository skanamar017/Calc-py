## Class
class Calculator:   

## Constructor
    def __init__(self): 
        self.display_val = 0

## Start of Core Methods (functions)
    def add(self, x): 
        sum = self.display_val + x 
        self.display_val = sum
        return sum

    def sub(self, x):
        difference = self.display_val - x
        self.display_val = difference
        return difference


    def multiply(self, x):
        product = self.display_val * x
        self.display_val = product
        return product
    

# add lots more methods to this calculator class.

