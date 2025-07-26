def calculateSquare(inputNumber):
    squaredResult = inputNumber ** 2
    return squaredResult


def findLargestNumber(firstNumber, secondNumber):
    if firstNumber > secondNumber:
        largestNumber = firstNumber
    elif secondNumber > firstNumber:
        largestNumber = secondNumber
    else:
        largestNumber = firstNumber  
    
    return largestNumber


def demonstrateSquareFunction():
    print("Task 1: Square Number Function")
    print("=" * 50)
    
    try:
        userNumber = float(input("Enter a number to square: "))
        squareResult = calculateSquare(userNumber)
        print(f"The square of {userNumber} is: {squareResult}")
        
        print("\nTesting with sample numbers:")
        testNumbers = [2, 5, 7, 10, -3]
        
        for currentTestNumber in testNumbers:
            testResult = calculateSquare(currentTestNumber)
            print(f"Square of {currentTestNumber} = {testResult}")
            
    except ValueError:
        print("Error Please enter a valid number")

    print("\n")


def demonstrateLargestNumberFunction():
    print("Task 2: Find Largest of Two Numbers Function")
    print("=" * 50)
    
    try:
        firstUserNumber = float(input("Enter the first number: "))
        secondUserNumber = float(input("Enter the second number: "))
        
        largestResult = findLargestNumber(firstUserNumber, secondUserNumber)
        
        if firstUserNumber == secondUserNumber:
            print(f"Both numbers are equal: {largestResult}")
        else:
            print(f"The largest number between {firstUserNumber} and {secondUserNumber} is: {largestResult}")
        
        print("\nTesting function with sample number pairs:")
        testPairs = [(10, 5), (3, 8), (15, 15), (-2, 7), (-10, -5)]
        
        for firstTestNumber, secondTestNumber in testPairs:
            testLargest = findLargestNumber(firstTestNumber, secondTestNumber)
            if firstTestNumber == secondTestNumber:
                print(f"Largest of {firstTestNumber} and {secondTestNumber} = {testLargest} (equal)")
            else:
                print(f"Largest of {firstTestNumber} and {secondTestNumber} = {testLargest}")
                
    except ValueError:
        print("Error Please enter valid numbers")



if __name__ == "__main__":
    demonstrateSquareFunction()
    demonstrateLargestNumberFunction()
    print("=" * 50)