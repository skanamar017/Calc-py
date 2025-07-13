from calculator import Calculator


mode="Decimal" # default mode
units="Degrees"

def switchDisplayMode():
    if mode=="Decimal":
        mode="Hexadecimal"
    elif mode=="Hexadecimal":
        mode=="Binary"
    elif mode=="Binary":
        mode=="Octal"
    elif mode=="Octal":
        mode=="Decimal"
    return mode


def switchDisplayMode(setting):
    if setting in ["Binary", "Octal", "Decimal", "Hexadecimal"]:
        mode=setting
        return mode
    print("Not a valid mode")
    return

def getTwoNumbers():
    a = str(input("first number? "))
    b = str(input("second number? "))
    return a, b


def displayResult(x):
    print(x, "\n")



#add set mode operation to calc loop

#need to add degrees to radians and memory


def switchUnitsMode():
    if units=="Degrees":
        units="Radians"
    elif units=="Radians":
        units="Degrees"
    return units


def switchUnitsMode(setting):
    if setting in ["Degrees", "Radiens"]:
        units=setting
        return units
    print("Not a valid mode")
    return


memory=[]




def performCalcLoop(calc):
    choice = input("Operation? ")
    if choice == 'add':
        a, b = getTwoNumbers()
        if mode=="Binary":
            a = int(a, 2)
            b = int(b, 2)
            result=calc.add(a, b)
            displayResult(bin(result)[2:])
        elif mode=="Octal":
            a = int(a, 8)
            b = int(b, 8)
            result=calc.add(a, b)
            displayResult(oct(result)[2:])
        elif mode=="Decimal":
            displayResult(calc.add(float(a), float(b)))
        elif mode=="Hexadecimal":
            a = int(a, 16)
            b = int(b, 16)
            result=calc.add(a, b)
            displayResult(hex(result)[2:])




def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
