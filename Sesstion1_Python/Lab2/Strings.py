def reverseString():
    print("Task 1: String Reverser")
    print("=" * 50)
    
    try:
        inputString = input("Enter a string to reverse: ")
        reversedString = inputString[::-1]
        print(f"Original String: \"{inputString}\"")
        print(f"Reversed String: \"{reversedString}\"")
    except Exception:
        print("Error Please enter a valid string")
    
    print("\n")


def countUpperAndLowerCaseLetters():
    print("Task 2: Upper and Lower Case Counter")
    print("=" * 50)
    
    try:
        inputString = input("Enter a string to analyze: ")
        upperCaseCount = 0
        lowerCaseCount = 0
        
        for currentCharacter in inputString:
            if currentCharacter.isupper():
                upperCaseCount += 1
            elif currentCharacter.islower():
                lowerCaseCount += 1
        
        print(f"Sample String: '{inputString}'")
        print(f"No. of Upper case characters: {upperCaseCount}")
        print(f"No. of Lower case characters: {lowerCaseCount}")
    except Exception:
        print("Error Please enter a valid string")
    
    print("\n")


def checkPalindrome():
    print("Task 3: Palindrome Checker")
    print("=" * 50)
    
    try:
        inputString = input("Enter a string to check if it's a palindrome: ")
        
        cleanedString = inputString.replace(" ", "").lower()
        reversedCleanedString = cleanedString[::-1]
        
        if cleanedString == reversedCleanedString:
            print(f"'{inputString}' is a palindrome")
        else:
            print(f"'{inputString}' is not a palindrome")
            
    except Exception:
        print("Error Please enter a valid string")


    


if __name__ == "__main__":
    reverseString()
    countUpperAndLowerCaseLetters()
    checkPalindrome()
    print("=" * 50)