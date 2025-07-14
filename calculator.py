import math
import conversions

## Class
class Calculator:   

## Constructor
    def __init__(self): 
        self.display_val = 0

        self.mode="Decimal" # default mode
        self.units="Radians" #defualt units
        self.memory=0
    

    def memory_add(self): #Add the currently displayed value to the value in memory (store in memory and update display) 
        self.memory+=self.display_val
        self.display_val=self.memory
    
    def memory_clear(self): #Reset memory *
        self.memory=0
    
    def memory_recall(self): #Recall the current value from memory to the display *
        self.display_val=self.memory
        return self.display_val




    def switchDisplayMode(self):
        if self.mode=="Decimal":
            self.mode="Hexadecimal"
        elif self.mode=="Hexadecimal":
            self.mode=="Binary"
        elif self.mode=="Binary":
            self.mode=="Octal"
        elif self.mode=="Octal":
            self.mode=="Decimal"
        return self.mode

    def switchDisplayMode(self, setting):
        if setting in ["Binary", "Octal", "Decimal", "Hexadecimal"]:
            self.mode=setting
            return self.mode
        print("Not a valid mode")
        return

    def switchUnitsMode(self):
        if self.units=="Degrees":
            self.units="Radians"
        elif self.units=="Radians":
            self.units="Degrees"
        return self.units

    def switchUnitsMode(setting):
        if setting in ["Degrees", "Radiens"]:
            units=setting
            return units
        print("Not a valid mode")
        return

    ## Start of Core Methods (functions)
    def add(self, x): 
        #convert display_val to bin, oct, or hex
        #x will be in bin, oct, or hex
        if self.mode=="Binary":
            bin_val=conversions.bin_float_to_dec(self.display_val)
            bin_x=conversions.bin_float_to_dec(x)
            result = bin_val + bin_x
            self.display_val = result
            return result
        elif self.mode=="Octal":
            oct_val=conversions.oct_float_to_dec(self.display_val)
            oct_x=conversions.oct_float_to_dec(x)
            result = oct_val + oct_x
            self.display_val = result
            return result
        elif self.mode=="Decimal":
            result = self.display_val + x
            self.display_val = result
            return result
        elif self.mode=="Hexadecimal":
            hex_val=conversions.hex_float_to_dec(self.display_val)
            hex_x=conversions.hex_float_to_dec(x)
            result = hex_val + hex_x
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
    
    # Variable Exponentiation 
    def varExp(self, y):
        result = self.display_val ** y
        self.display_val = result
        return result
    
    def inverse(self):
        if self.display_val == 0:
            self.display_val = 'err'
            return

        result = 1 / self.display_val
        self.display_val = result
        return result
    
    def invert(self):
        result = self.display_val * -1
        return result
    
    def percentage(self, percent):
        result = self.display_val * percent / 100
        return result
    
    def nth_root(self, n):
        result = self.display_val ** (1/n)
        return result
    
    def sine(self):
        if self.units=="Radians":
            result = math.sin(self.display_val)
        elif self.units=="Degrees":
            result = math.sin(math.radians(self.display_val))
        return result

    def cosine(self):
        if self.units=="Radians":
            result = math.cos(self.display_val)
        elif self.units=="Degrees":
            result = math.cos(math.radians(self.display_val))
        return result

    def tangent(self):
        if self.units=="Radians":
            result = math.tan(self.display_val)
        elif self.units=="Degrees":
            result = math.tan(math.radians(self.display_val))
        return result
    
    def inverse_sine(self):
        if self.units=="Radians":
            result = math.asinsin(self.display_val)
        elif self.units=="Degrees":
            result = math.degrees(math.asin(self.display_val))
        return result

    def inverse_cosine(self):
        if self.units=="Radians":
            result = math.acoscos(self.display_val)
        elif self.units=="Degrees":
            result = math.degrees(math.acos(self.display_val))
        return result

    def inverse_tangent(self):
        if self.units=="Radians":
            result = math.acostan(self.display_val)
        elif self.units=="Degrees":
            result = math.degrees(math.atan(self.display_val))
        return result



        
    def clear(self):
        self.display_val = 0

    

    

    

# add lots more methods to this calculator class.
# for a commit