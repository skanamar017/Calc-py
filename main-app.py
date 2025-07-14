from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getNumber():
    a = float(input("number? "))
    return a

def getMode():
    a = str(input("mode? "))
    return a

def displayResult(x: float):
    print(x, "\n")


def performCalcLoop(calc):
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice=="Switch Mode":
            displayResult(calc.switchDisplayMode())
        elif choice=="Choose Mode":
            a=getMode()
            displayResult(calc.chooseDisplayMode(a))
        elif choice=="Switch Units":
            displayResult(calc.switchUnitsMode())
        elif choice=="Choose Units":
            a=getMode()
            displayResult(calc.chooseUnitsMode(a))
        elif choice=="M+":
            displayResult(calc.memory_add())
        elif choice=="MC":
            displayResult(calc.memory_clear())
        elif choice=="MRC":
            displayResult(calc.memory_recall())
        elif choice == 'add':
            a = getNumber()
            displayResult(calc.add(a))
        elif choice == 'subtract':
            a = getNumber()
            displayResult(calc.sub(a))
        elif choice == 'multiply':
            a = getNumber()
            displayResult(calc.multiply(a))
        elif choice == 'divide':
            a = getNumber()
            displayResult(calc.divide(a))
        elif choice == 'square':
            displayResult(calc.square())
        elif choice == 'square root':
            displayResult(calc.square_rt())
        elif choice == 'exponent':
            a = getNumber()
            displayResult(calc.varExp(a))
        elif choice == 'inverse':
            displayResult(calc.inverse())
        elif choice == 'invert':
            displayResult(calc.invert())
        elif choice=="percent":
            a = getNumber()
            displayResult(calc.percentage(a))
        elif choice=="nth root":
            a = getNumber()
            displayResult(calc.nth_root(a))
        elif choice == 'sine':
            displayResult(calc.sine())
        elif choice == 'cosine':
            displayResult(calc.cosine())
        elif choice == 'tangent':
            displayResult(calc.tangent())
        elif choice == 'inverse sine':
            displayResult(calc.inverse_sine())
        elif choice == 'inverse consine':
            displayResult(calc.inverse_cosine())
        elif choice == 'inverse tangent':
            displayResult(calc.inverse_tangent())
        elif choice=="clear":
            displayResult(calc.clear())
        
        else:
            print("That is not a valid input.")
        


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
