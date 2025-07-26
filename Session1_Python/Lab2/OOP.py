import math
from datetime import datetime

print("Task 1: Circle Class")
print("=" * 50)

class Circle:
    def __init__(self, circleRadius):
        self.circleRadius = circleRadius
    
    def calculateArea(self):
        circleArea = math.pi * (self.circleRadius ** 2)
        return circleArea
    
    def calculatePerimeter(self):
        circlePerimeter = 2 * math.pi * self.circleRadius
        return circlePerimeter

try:
    userRadius = float(input("Enter the radius of the circle: "))
    if userRadius < 0:
        print("Error Radius cannot be negative")
    else:
        userCircle = Circle(userRadius)
        circleAreaResult = userCircle.calculateArea()
        circlePerimeterResult = userCircle.calculatePerimeter()
        
        print(f"Circle with radius {userRadius}:")
        print(f"Area: {circleAreaResult:.2f}")
        print(f"Perimeter: {circlePerimeterResult:.2f}")
        
except ValueError:
    print("Error Please enter a valid number")
except Exception:
    print("Error Please enter valid input")

print("\n")


print("Task 2: Person Class")
print("=" * 50)

class Person:
    def __init__(self, personName, personCountry, birthDate):
        self.personName = personName
        self.personCountry = personCountry
        self.birthDate = birthDate
    
    def calculateAge(self):
        currentDate = datetime.now()
        personAge = currentDate.year - self.birthDate.year
        
        if currentDate.month < self.birthDate.month or (currentDate.month == self.birthDate.month and currentDate.day < self.birthDate.day):
            personAge -= 1
        
        return personAge
    
    def displayPersonInfo(self):
        calculatedAge = self.calculateAge()
        print(f"Name: {self.personName}")
        print(f"Country: {self.personCountry}")
        print(f"Birth Date: {self.birthDate.strftime('%Y-%m-%d')}")
        print(f"Age: {calculatedAge} years")

try:
    userName = input("Enter person's name: ")
    userCountry = input("Enter person's country: ")
    
    print("Enter birth date:")
    birthYear = int(input("Enter birth year (YYYY): "))
    birthMonth = int(input("Enter birth month (1-12): "))
    birthDay = int(input("Enter birth day (1-31): "))
    
    userBirthDate = datetime(birthYear, birthMonth, birthDay)
    userPerson = Person(userName, userCountry, userBirthDate)
    
    print("\nPerson Information:")
    userPerson.displayPersonInfo()
    
except ValueError:
    print("Error Please enter valid date values")


print("\n")


print("Task 3: Calculator Class")
print("=" * 50)

class Calculator:
    def __init__(self):
        pass
    
    def addNumbers(self, firstNumber, secondNumber):
        additionResult = firstNumber + secondNumber
        return additionResult
    
    def subtractNumbers(self, firstNumber, secondNumber):
        subtractionResult = firstNumber - secondNumber
        return subtractionResult
    
    def multiplyNumbers(self, firstNumber, secondNumber):
        multiplicationResult = firstNumber * secondNumber
        return multiplicationResult
    
    def divideNumbers(self, firstNumber, secondNumber):
        if secondNumber == 0:
            return "Error Cannot divide by zero"
        divisionResult = firstNumber / secondNumber
        return divisionResult

try:
    userCalculator = Calculator()
    
    firstOperand = float(input("Enter first number: "))
    secondOperand = float(input("Enter second number: "))
    
    print(f"\nCalculator Results for {firstOperand} and {secondOperand}:")
    print(f"Addition: {firstOperand} + {secondOperand} = {userCalculator.addNumbers(firstOperand, secondOperand)}")
    print(f"Subtraction: {firstOperand} - {secondOperand} = {userCalculator.subtractNumbers(firstOperand, secondOperand)}")
    print(f"Multiplication: {firstOperand} × {secondOperand} = {userCalculator.multiplyNumbers(firstOperand, secondOperand)}")
    print(f"Division: {firstOperand} ÷ {secondOperand} = {userCalculator.divideNumbers(firstOperand, secondOperand)}")
    
except ValueError:
    print("Error Please enter valid numbers")

print("\n")


print("Task 4: Shape Classes with Inheritance")
print("=" * 50)

class Shape:
    def __init__(self, shapeName):
        self.shapeName = shapeName
    
    def calculateArea(self):
        pass
    
    def calculatePerimeter(self):
        pass

class ShapeCircle(Shape):
    def __init__(self, circleRadius):
        super().__init__("Circle")
        self.circleRadius = circleRadius
    
    def calculateArea(self):
        return math.pi * (self.circleRadius ** 2)
    
    def calculatePerimeter(self):
        return 2 * math.pi * self.circleRadius

class ShapeTriangle(Shape):
    def __init__(self, triangleBase, triangleHeight, sideA, sideB, sideC):
        super().__init__("Triangle")
        self.triangleBase = triangleBase
        self.triangleHeight = triangleHeight
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC
    
    def calculateArea(self):
        return 0.5 * self.triangleBase * self.triangleHeight
    
    def calculatePerimeter(self):
        return self.sideA + self.sideB + self.sideC

class ShapeSquare(Shape):
    def __init__(self, squareSide):
        super().__init__("Square")
        self.squareSide = squareSide
    
    def calculateArea(self):
        return self.squareSide ** 2
    
    def calculatePerimeter(self):
        return 4 * self.squareSide

try:
    # Test Circle
    print("Testing Circle:")
    testCircleRadius = float(input("Enter circle radius: "))
    testCircle = ShapeCircle(testCircleRadius)
    print(f"Circle - Area: {testCircle.calculateArea():.2f}, Perimeter: {testCircle.calculatePerimeter():.2f}")
    
    # Test Square
    print("\nTesting Square:")
    testSquareSide = float(input("Enter square side length: "))
    testSquare = ShapeSquare(testSquareSide)
    print(f"Square - Area: {testSquare.calculateArea():.2f}, Perimeter: {testSquare.calculatePerimeter():.2f}")
    
    # Test Triangle
    print("\nTesting Triangle:")
    testTriangleBase = float(input("Enter triangle base: "))
    testTriangleHeight = float(input("Enter triangle height: "))
    testSideA = float(input("Enter side A length: "))
    testSideB = float(input("Enter side B length: "))
    testSideC = float(input("Enter side C length: "))
    
    testTriangle = ShapeTriangle(testTriangleBase, testTriangleHeight, testSideA, testSideB, testSideC)
    print(f"Triangle - Area: {testTriangle.calculateArea():.2f}, Perimeter: {testTriangle.calculatePerimeter():.2f}")
    
    # Display all shapes
    allShapes = [testCircle, testSquare, testTriangle]
    print(f"\nSummary of all shapes:")
    for currentShape in allShapes:
        print(f"{currentShape.shapeName} - Area: {currentShape.calculateArea():.2f}, Perimeter: {currentShape.calculatePerimeter():.2f}")
        
except ValueError:
    print("Error Please enter valid numbers")


print("=" * 50)