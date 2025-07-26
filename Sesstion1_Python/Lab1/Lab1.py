import math


def calculateCircleArea():
    """Task 1: Calculate the area of a circle from user input"""
    print("Task 1: Circle Area")
    print("=" * 50)

    try:
        circleRadius = float(input("Enter the radius of the circle: "))
        if circleRadius < 0:
            print("Error Radius cannot be negative")
        else:
            circleArea = math.pi * circleRadius ** 2
            print(f"The area of the circle with radius {circleRadius} is: {circleArea:.2f}")
    except ValueError:
        print("Error Please enter a valid number")

    print("\n")


def checkOddOrEven():
    """Task 2: Check if a number is odd or even"""
    print("Task 2: Odd or Even Checker")
    print("=" * 50)

    try:
        inputNumber = int(input("Enter a number: "))
        
        if inputNumber % 2 == 0:
            print(f"{inputNumber} is an Even number")
        else:
            print(f"{inputNumber} is an Odd number")
    except ValueError:
        print("Error Please enter a valid integer")

    print("\n")


def calculateConditionalSum():
    """Task 3: Sum of three integers with special condition"""
    print("Task 3: Conditional Sum Calculator")
    print("=" * 50)

    try:
        firstInteger = int(input("Enter first integer: "))
        secondInteger = int(input("Enter second integer: "))
        thirdInteger = int(input("Enter third integer: "))
        
        if firstInteger == secondInteger or secondInteger == thirdInteger or firstInteger == thirdInteger:
            sumResult = 0
            print(f"Two or more values are equal, so the sum is: {sumResult}")
        else:
            sumResult = firstInteger + secondInteger + thirdInteger
            print(f"Sum of {firstInteger}, {secondInteger}, and {thirdInteger} is: {sumResult}")
    except ValueError:
        print("Error Please enter valid integers")

    print("\n")


def printSummationPattern():
    """Task 4: Print Natural Numbers Summation Pattern"""
    print("Task 4: Natural Numbers Summation Pattern")
    print("=" * 50)

    try:
        numberOfTerms = int(input("Enter the number of terms: "))
        if numberOfTerms <= 0:
            print("Error Please enter a positive number")
        else:
            print("Pattern:")
            for currentTerm in range(1, numberOfTerms + 1):
                currentSum = sum(range(1, currentTerm + 1))
                
                termsList = " + ".join(str(termValue) for termValue in range(1, currentTerm + 1))
                print(f"{termsList} = {currentSum}")
    except ValueError:
        print("Error Please enter a valid integer")

    print("\n")


def checkPrimeNumber():
    """Task 5: Check if a number is prime"""
    print("Task 5: Prime Number Checker")
    print("=" * 50)

    try:
        inputNumber = int(input("Enter a number to check if it's prime: "))
        
        if inputNumber < 2:
            print(f"{inputNumber} is not a prime number")
        elif inputNumber == 2:
            print(f"{inputNumber} is a prime number")
        else:
            isPrime = True
            for divisor in range(2, int(math.sqrt(inputNumber)) + 1):
                if inputNumber % divisor == 0:
                    isPrime = False
                    break
            
            if isPrime:
                print(f"{inputNumber} is a prime number")
            else:
                print(f"{inputNumber} is not a prime number")
    except ValueError:
        print("Error Please enter a valid integer")

    print("\n")


def displayPowersOfTwo():
    """Task 6: Display first 16 powers of 2"""
    print("Task 6: First 16 Powers of 2")
    print("=" * 50)

    print("Powers of 2 starting with 1:")
    for exponent in range(16):
        powerResult = 2 ** exponent
        print(f"2^{exponent} = {powerResult}")

    print("\n")


def printEvenNumbers():
    """Task 7: Print even numbers in range"""
    print("Task 7: Even Numbers in Range")
    print("=" * 50)

    try:
        upperLimit = int(input("Enter the upper limit (n): "))
        if upperLimit < 1:
            print("Error: Please enter a positive number!")
        else:
            print(f"Even numbers from 1 to {upperLimit}:")
            evenNumbersList = []
            for currentNumber in range(1, upperLimit + 1):
                if currentNumber % 2 == 0:
                    evenNumbersList.append(currentNumber)
            
            if evenNumbersList:
                print(", ".join(map(str, evenNumbersList)))
            else:
                print("No even numbers in the given range")

    except ValueError:
        print("Error Please enter valid integers")

    print("=" * 50)


if __name__ == "__main__":
    calculateCircleArea()
    checkOddOrEven()
    calculateConditionalSum()
    printSummationPattern()
    checkPrimeNumber()
    displayPowersOfTwo()
    printEvenNumbers()