from calculator import Calculator


mode="Decimal" # default mode

def switchDisplayMode():
    if mode=="Decimal":
        mode="Hexadecimal"
        return mode
    elif mode=="Hexadecimal":
        mode=="Binary"
        return mode
    elif mode=="Binary":
        mode=="Octal"
        return mode
    elif mode=="Octal":
        mode=="Decimal"
        return mode


def switchDisplayMode(setting):
    mode=setting
    return mode

def getTwoNumbers():
    a = str(input("first number? "))
    b = str(input("second number? "))
    return a, b


def displayResult(x):
    print(x, "\n")



#add set mode operation to calc loop

#need to add degrees to radians and memory
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
