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
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))
        elif choice == 'subract':
            a, b = getTwoNumbers()
            displayResult(calc.sub(a, b))
        elif choice == 'multiply':
            a, b = getTwoNumbers()
            displayResult(calc.mult(a, b))
        elif choice == 'divide':
            a, b = getTwoNumbers()
            displayResult(calc.div(a, b))
        elif choice == 'square':
            a = getNumber()
            displayResult(calc.square(a))
        elif choice == 'square root':
            a = getNumber()
            displayResult(calc.square_root(a))
        elif choice == 'exponent':
            a, b = getTwoNumbers()
            displayResult(calc.exponent(a, b))
        elif choice == 'inverse':
            a = getNumber()
            displayResult(calc.inverse(a))
        elif choice == 'invert sign':
            a = getNumber()
            displayResult(calc.invert_sign(a))
        elif choice == 'sine':
            a = getNumber()
            displayResult(calc.sine(a))
        elif choice == 'cosine':
            a = getNumber()
            displayResult(calc.cosine(a))
        elif choice == 'tangent':
            a = getNumber()
            displayResult(calc.tangent(a))
        elif choice == 'inverse sine':
            a = getNumber()
            displayResult(calc.inverse_sine(a))
        elif choice == 'inverse consine':
            a = getNumber()
            displayResult(calc.inverse_cosine(a))
        elif choice == 'inverse tangent':
            a = getNumber()
            displayResult(calc.inverse_tangent(a))
        
        else:
            print("That is not a valid input.")
        


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
