from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getNumber():
    a = float(input("number? "))
    return a

def displayResult(x: float):
    print(x, "\n")


def performCalcLoop(calc):
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'add':
            a = getNumber()
            displayResult(calc.add(a))
        elif choice == 'subract':
            a = getNumber()
            displayResult(calc.sub(a))
        elif choice == 'multiply':
            a = getNumber()
            displayResult(calc.mult(a))
        elif choice == 'divide':
            a = getNumber()
            displayResult(calc.div(a))
        elif choice == 'square':
            displayResult(calc.square())
        elif choice == 'square root':
            displayResult(calc.square_root())
        elif choice == 'exponent':
            a = getNumber()
            displayResult(calc.exponent(a))
        elif choice == 'inverse':
            displayResult(calc.inverse())
        elif choice == 'invert sign':
            displayResult(calc.invert_sign())
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
        
        else:
            print("That is not a valid input.")
        


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
