import sys, time, random

typing_speed = 50

def numberSort():
    firstNum = int(input("\nEnter your first number: "))
    secondNum = int(input("Enter your second number: "))
    thirdNum = int(input("Enter your third number: "))
    fourthNum = int(input("Enter your fourth number: "))
    if firstNum <= secondNum and secondNum <= thirdNum and thirdNum <= fourthNum:
        print(f"\nThe numbers aranged in descending order are [{fourthNum}, {thirdNum}, {secondNum}, {firstNum}].\n")
    elif firstNum <= secondNum and secondNum <= fourthNum and fourthNum <= thirdNum:
        print(f"\nThe numbers arranged in descending order are [{thirdNum}, {fourthNum}, {secondNum}, {firstNum}].\n")
    elif firstNum <= thirdNum and thirdNum <= secondNum and secondNum <= fourthNum:
        print(f"\nThe numbers arranged in descending order are [{fourthNum}, {secondNum}, {thirdNum}, {firstNum}].\n")
    elif firstNum <= fourthNum and fourthNum <= secondNum and secondNum <= thirdNum:
        print(f"\nThe numbers arranged in descending order are [{thirdNum}, {secondNum}, {fourthNum}, {firstNum}].\n")
    elif firstNum <= fourthNum and fourthNum <= thirdNum and thirdNum <= secondNum:
        print(f"\nThe numbers arranged in descending order are [{secondNum}, {thirdNum}, {fourthNum}, {firstNum}].\n")
    elif firstNum <= thirdNum and thirdNum <= fourthNum and fourthNum <= secondNum:
        print(f"\nThe numbers arranged in descending order are [{secondNum}, {fourthNum}, {thirdNum}, {firstNum}].\n")
    elif secondNum <= firstNum and firstNum <= thirdNum and thirdNum <= fourthNum:
        print(f"\nThe numbers arranged in descending order are [{fourthNum}, {thirdNum}, {firstNum}, {secondNum}].\n")
    elif secondNum <= firstNum and firstNum <= fourthNum and fourthNum <= thirdNum:
        print(f"\nThe numbers arranged in descending order are [{thirdNum}, {fourthNum}, {firstNum}, {secondNum}].\n")
    elif secondNum <= fourthNum and fourthNum <= thirdNum and thirdNum <= firstNum:
        print(f"The numbers arranged in descending order are [{firstNum}, {thirdNum}, {fourthNum}, {secondNum}].\n")
    elif secondNum <= thirdNum and thirdNum <= firstNum and firstNum <= fourthNum:
        print(f"\nThe numbers arranged in descending order are [{fourthNum}, {firstNum}, {thirdNum}, {secondNum}].\n")
    elif secondNum <= fourthNum and fourthNum <= firstNum and firstNum <= thirdNum:
        print(f"\nThe numbers arranged in descending order are [{thirdNum}, {firstNum}, {fourthNum}, {secondNum}].\n")
    elif secondNum <= thirdNum and thirdNum <= fourthNum and fourthNum <= secondNum:
        print(f"\nThe numbers arranged in descending order are [{firstNum}, {fourthNum}, {thirdNum}, {secondNum}].\n")
    elif thirdNum <= fourthNum and fourthNum <= secondNum and secondNum <= firstNum:
        print(f"\nThe numbers arranged in descending order are [{firstNum}, {secondNum}, {fourthNum}, {thirdNum}].\n")
    elif thirdNum <= secondNum and secondNum <= fourthNum and fourthNum <= firstNum:
        print(f"\nThe numbers arranged in descending order are [{firstNum}, {fourthNum}, {secondNum}, {thirdNum}].\n")
    elif thirdNum <= firstNum and firstNum <= secondNum and secondNum <= fourthNum:
        print(f"\nThe numbers arranged in descending order are [{fourthNum}, {secondNum}, {firstNum}, {thirdNum}].\n")
    elif thirdNum <= secondNum and secondNum <= firstNum and firstNum <= fourthNum:
        print(f"\nThe numbers arranged in descending order are [{fourthNum}, {firstNum}, {secondNum}, {thirdNum}].\n")
    elif thirdNum <= firstNum and firstNum <= fourthNum and fourthNum <= secondNum:
        print(f"\nThe numbers arranged in descending order are [{secondNum}, {fourthNum}, {firstNum}, {thirdNum}].\n")
    elif thirdNum <= fourthNum and fourthNum <= firstNum and firstNum <= secondNum:
        print(f"\nThe numbers arranged in descending order are [{secondNum}, {firstNum}, {fourthNum}, {thirdNum}].\n")
    elif fourthNum <= thirdNum and thirdNum <= secondNum and secondNum <= firstNum:
        print(f"\nThe numbers arranged in descending order are [{firstNum}, {secondNum}, {thirdNum}, {fourthNum}].\n")
    elif fourthNum <= secondNum and secondNum <= thirdNum and thirdNum <= firstNum:
        print(f"\nThe numbers arranged in descending order are [{firstNum}, {thirdNum}, {secondNum}, {fourthNum}].\n")
    elif fourthNum <= firstNum and firstNum <= thirdNum and thirdNum <= secondNum:
        print(f"\nThe numbers arranged in descending order are [{secondNum}, {thirdNum}, {firstNum}, {fourthNum}]\n.")
    elif fourthNum <= firstNum and firstNum <= secondNum and secondNum <= thirdNum:
        print(f"\nThe numbers arranged in descending order are [{thirdNum}, {secondNum}, {firstNum}, {fourthNum}].\n")
    elif fourthNum <= thirdNum and thirdNum <= firstNum and firstNum <= secondNum:
        print(f"\nThe numbers arranged in descending order are [{secondNum}, {firstNum}, {thirdNum}, {fourthNum}].\n")
    else:
        print(f"\nThe numbers arranged in descending order are [{thirdNum}, {firstNum}, {secondNum}, {fourthNum}].\n")

def pause(loading):
    for letter in loading:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*4.0/typing_speed)

def pauseNext(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*14.0/typing_speed)

getName = input("\nPlease enter your name: ")

pauseNext("\nLoading...\n")
time.sleep(1)
pause(f"\nHi there, {getName}! Welcome to Number Sorter 3.0! To proceed, please input 4 numbers.\n")
time.sleep(.5)
kazuha = numberSort()
time.sleep(1)
print("Thank you for using Number Sorter 3.0! Feel free to try again with different values, or come back next time.")
pauseNext(f"See you, {getName}!\n")