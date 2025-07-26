def sortDictionaryByValue():
    print("Task 1: Sort Dictionary by Value")
    print("=" * 50)
    
    try:
        sampleDictionary = {'apple': 45, 'banana': 30, 'cherry': 60, 'date': 25, 'elderberry': 35}
        
        print(f"Original Dictionary: {sampleDictionary}")
        
        ascendingSortedDict = dict(sorted(sampleDictionary.items(), key=lambda dictItem: dictItem[1]))
        print(f"Ascending Order (by value): {ascendingSortedDict}")
        
        descendingSortedDict = dict(sorted(sampleDictionary.items(), key=lambda dictItem: dictItem[1], reverse=True))
        print(f"Descending Order (by value): {descendingSortedDict}")
        
    except ValueError:
        print("Error Please enter valid numbers")
    
    print("\n")


def checkKeyExistsInDictionary():
    print("Task 2: Check if Key Exists in Dictionary")
    print("=" * 50)
    
    try:
        studentGrades = {'Tarek': 85, 'Omar': 92, 'Osama': 78, 'Ahmad': 96, 'Ali': 88}
        
        print(f"Sample Dictionary: {studentGrades}")
        
        searchKey = input("Enter a key to search for: ")
        
        if searchKey in studentGrades:
            print(f"Key '{searchKey}' exists in the dictionary")
            print(f"Value: {studentGrades[searchKey]}")
        else:
            print(f"Key '{searchKey}' does not exist in the dictionary")
        
        print(f"Available keys: {list(studentGrades.keys())}")
        
    except Exception:
        print("Error Please enter a valid key")
    
    print("\n")


def iterateOverDictionary():
    print("Task 3: Iterate Over Dictionary")
    print("=" * 50)
    
    try:
        countryCapitals = {
            'Egypt': 'Cairo',
            'France': 'Paris',
            'Germany': 'Berlin',
            'Japan': 'Tokyo',
            'Brazil': 'Brasilia'
        }
        
        print(f"Dictionary: {countryCapitals}")
        
        print("\nIteration Method 1 - Keys only:")
        for countryName in countryCapitals:
            print(f"Country: {countryName}")
        
        print("\nIteration Method 2 - Values only:")
        for capitalName in countryCapitals.values():
            print(f"Capital: {capitalName}")
        
        print("\nIteration Method 3 - Keys and Values:")
        for countryName, capitalName in countryCapitals.items():
            print(f"{countryName} -> {capitalName}")
        
        print("\nIteration Method 4 - Using enumerate:")
        for indexNumber, (countryName, capitalName) in enumerate(countryCapitals.items(), 1):
            print(f"{indexNumber}. {countryName}: {capitalName}")
            
    except Exception:
        print("Error occurred during iteration")
    
    print("\n")


def generateNumbersAndSquaresDictionary():
    print("Task 4: Generate Dictionary of Numbers and Squares")
    print("=" * 50)
    
    try:
        upperLimit = int(input("Enter the upper limit for numbers: "))
        
        if upperLimit <= 0:
            print("Error Please enter a positive number")
        else:
            squaresDictionary = {}
            
            for currentNumber in range(1, upperLimit + 1):
                numberSquare = currentNumber ** 2
                squaresDictionary[currentNumber] = numberSquare
            
            print(f"Dictionary of numbers and their squares (1 to {upperLimit}):")
            print(squaresDictionary)
            
            print("\nDetailed view:")
            for numberKey, squareValue in squaresDictionary.items():
                print(f"{numberKey}² = {squareValue}")
                
    except ValueError:
        print("Error Please enter a valid number")
    
    print("\n")


def manageEmployeeData():
    print("Task 5: Employee Data Management")
    print("=" * 50)
    
    try:
        employeeDatabase = {}
        
        numberOfEmployees = int(input("How many employees do you want to add? "))
        
        for employeeIndex in range(numberOfEmployees):
            print(f"\nEntering data for Employee {employeeIndex + 1}:")
            
            employeeNumber = input("Enter employee number: ")
            employeeName = input("Enter employee name: ")
            employeeDepartment = input("Enter department: ")
            employeeSalary = float(input("Enter salary: "))
            employeePosition = input("Enter position: ")
            
            employeeData = {
                'name': employeeName,
                'department': employeeDepartment,
                'salary': employeeSalary,
                'position': employeePosition
            }
            
            employeeDatabase[employeeNumber] = employeeData
        
        print("\n" + "=" * 60)
        print("EMPLOYEE DATABASE")
        print("=" * 60)
        
        for empNumber, empData in employeeDatabase.items():
            print(f"Employee Number: {empNumber}")
            print(f"  Name: {empData['name']}")
            print(f"  Department: {empData['department']}")
            print(f"  Position: {empData['position']}")
            print(f"  Salary: ${empData['salary']:.2f}")
            print("-" * 40)
            
    except ValueError:
        print("Error Please enter valid numbers for salary")



if __name__ == "__main__":
    sortDictionaryByValue()
    checkKeyExistsInDictionary()
    iterateOverDictionary()
    generateNumbersAndSquaresDictionary()
    manageEmployeeData()
    print("=" * 50)