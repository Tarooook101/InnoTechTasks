def getDistinctElementsFromList():
    print("Task 1: Get Distinct Elements from List")
    print("=" * 50)
    
    try:
        print("Enter your list (comma-separated numbers):")
        userInput = input("Enter numbers: ")
        userList = [int(number.strip()) for number in userInput.split(",")]
        userDistinctList = []
        
        for currentElement in userList:
            if currentElement not in userDistinctList:
                userDistinctList.append(currentElement)
        
        print(f"Original List: {userList}")
        print(f"Unique List: {userDistinctList}")
        
    except ValueError:
        print("Error: Please enter valid numbers separated by commas")
    
    print("\n")


def printEvenNumbersFromList():
    print("Task 2: Print Even Numbers from List")
    print("=" * 50)
    
    try:
        print("Enter your list (comma-separated numbers):")
        userInput = input("Enter numbers: ")
        userList = [int(number.strip()) for number in userInput.split(",")]
        userEvenNumbers = []
        
        for currentNumber in userList:
            if currentNumber % 2 == 0:
                userEvenNumbers.append(currentNumber)
        
        print(f"Original List: {userList}")
        print(f"Even Numbers: {userEvenNumbers}")
        
    except ValueError:
        print("Error Please enter valid numbers separated by commas")
    
    print("\n")


def findKthLargestElement():
    print("Task 3: Find Kth Largest Element")
    print("=" * 50)
    
    try:
        print("Enter your list (comma-separated numbers):")
        userInput = input("Enter numbers: ")
        numbersList = [int(number.strip()) for number in userInput.split(",")]
        
        kthPosition = int(input("Enter k (position of largest element to find): "))
        
        if kthPosition <= 0 or kthPosition > len(numbersList):
            print(f"Error: k should be between 1 and {len(numbersList)}")
        else:
            sortedList = sorted(numbersList, reverse=True)
            kthLargestElement = sortedList[kthPosition - 1]
            
            print(f"Original List: {numbersList}")
            print(f"Sorted List (descending): {sortedList}")
            print(f"The {kthPosition}th largest element is: {kthLargestElement}")
            
    except ValueError:
        print("Error Please enter valid numbers and k value")
    
    print("\n")


def checkListPalindrome():
    print("Task 4: Check if List is Palindrome")
    print("=" * 50)
    
    try:
        print("Enter your list (comma-separated values):")
        userInput = input("Enter values: ")
        inputList = [item.strip() for item in userInput.split(",")]
        
        reversedList = inputList[::-1]
        
        if inputList == reversedList:
            isPalindrome = True
            print(f"List: {inputList}")
            print(f"Reversed: {reversedList}")
            print("Result: True - The list is a palindrome")
        else:
            isPalindrome = False
            print(f"List: {inputList}")
            print(f"Reversed: {reversedList}")
            print("Result: False - The list is not a palindrome")
            
    except Exception:
        print("Error Please enter a valid input")
    
    print("\n")


def createShoppingList():
    shoppingList = []
    print("Enter 10 shopping items:")
    for i in range(1, 11):
        item = input(f"Enter item {i}: ")
        shoppingList.append(item)
    return shoppingList


def insertItemIntoList(inputList, item, position):
    if position < 1 or position > len(inputList) + 1:
        return False
    inputList.insert(position - 1, item)
    return True


def runAllListTasks():
    getDistinctElementsFromList()
    printEvenNumbersFromList()
    findKthLargestElement()
    checkListPalindrome()
    
    shoppingList = createShoppingList()
    if shoppingList:
        insertItemIntoShoppingList(shoppingList)
    
    print("=" * 50)


if __name__ == "__main__":
    runAllListTasks()