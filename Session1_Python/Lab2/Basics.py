import math

def convertInchesToCentimeters():
    print("Task 1: Inches to Centimeters Converter")
    print("=" * 50)
    
    try:
        lengthInInches = float(input("Enter length in inches: "))
        lengthInCentimeters = lengthInInches * 2.54
        print(f"Length in centimeters: {lengthInCentimeters:.2f} cm")
    except ValueError:
        print("Error Please enter a valid number")
    
    print("\n")


def convertCelsiusToFahrenheit():
    print("Task 2: Celsius to Fahrenheit Converter")
    print("=" * 50)
    
    try:
        temperatureInCelsius = float(input("Enter temperature in Celsius: "))
        temperatureInFahrenheit = (temperatureInCelsius * 9/5) + 32
        print(f"Temperature in Fahrenheit: {temperatureInFahrenheit:.2f}°F")
    except ValueError:
        print("Error Please enter a valid number")
    
    print("\n")


def calculateSphereVolume():
    print("Task 3: Sphere Volume Calculator")
    print("=" * 50)
    
    try:
        sphereRadius = float(input("Enter the radius of the sphere: "))
        if sphereRadius < 0:
            print("Error Radius cannot be negative")
        else:
            sphereVolume = (4/3) * math.pi * (sphereRadius ** 3)
            print(f"Volume of the sphere: {sphereVolume:.2f}")
    except ValueError:
        print("Error Please enter a valid number")
    
    print("\n")


def calculateEmployeePay():
    print("Task 4: Employee Pay Calculator")
    print("=" * 50)
    
    try:
        grossPay = float(input("Enter employee's gross pay: "))
        if grossPay < 0:
            print("Error Gross pay cannot be negative")
        else:
            taxRate = 0.20  
            taxAmount = grossPay * taxRate
            netPay = grossPay - taxAmount
            
            print(f"Gross Pay: ${grossPay:.2f}")
            print(f"Tax Amount (20%): ${taxAmount:.2f}")
            print(f"Net Pay: ${netPay:.2f}")
    except ValueError:
        print("Error Please enter a valid number")
    
    print("\n")


def printNumbersOneToTen():
    print("Task 5: Print Numbers 1 to 10")
    print("=" * 50)
    
    print("Numbers from 1 to 10:")
    for currentNumber in range(1, 11):
        print(currentNumber, end=" ")
    
    print("\n\n")


def acceptNumbersUntilNegative():
    print("Task 6: Accept Numbers Until Negative")
    print("=" * 50)
    
    print("Enter numbers (negative number to stop):")
    enteredNumbers = []
    
    while True:
        try:
            userInput = float(input("Enter a number: "))
            if userInput < 0:
                print("Negative number entered. Stopping...")
                break
            else:
                enteredNumbers.append(userInput)
                print(f"You entered: {userInput:.2f}")
        except ValueError:
            print("Error Please enter a valid number")
    
    if enteredNumbers:
        print(f"Numbers you entered: {[f'{num:.2f}' for num in enteredNumbers]}")
    else:
        print("No valid numbers were entered")
    
    print("\n")


def identifyNumberRange():
    print("Task 7: Number Range Identifier")
    print("=" * 50)
    
    try:
        inputInteger = int(input("Enter an integer: "))
        
        if 0 <= inputInteger <= 10:
            print(f"{inputInteger} belongs to Range 1: 0 to 10")
        elif 11 <= inputInteger <= 20:
            print(f"{inputInteger} belongs to Range 2: 11 to 20")
        elif 21 <= inputInteger <= 30:
            print(f"{inputInteger} belongs to Range 3: 21 to 30")
        elif 31 <= inputInteger <= 40:
            print(f"{inputInteger} belongs to Range 4: 31 to 40")
        else:
            print(f"{inputInteger} does not belong to any specified range (0-40)")
            
    except ValueError:
        print("Error Please enter a valid integer")


    


if __name__ == "__main__":
    convertInchesToCentimeters()
    convertCelsiusToFahrenheit()
    calculateSphereVolume()
    calculateEmployeePay()
    printNumbersOneToTen()
    acceptNumbersUntilNegative()
    identifyNumberRange()
    print("=" * 50)