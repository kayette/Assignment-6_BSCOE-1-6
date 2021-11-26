import operator, time, sys, random

typing_speed = 50

def pause(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*4.0/typing_speed)

def pauseNext(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*14.0/typing_speed)

def askCalc():
    global ansKey
    get_intA = random.randint(0,100)
    get_intB = random.randint(0,100)
    operator = "+"
    question = str(get_intA) + " " + str(operator) + " " + str(get_intB)
    ansKey = eval(question)
    print(question)
    return ansKey

def askQuestion():
    rightAns = askCalc()
    userAns = int(input("= "))
    return rightAns == userAns

def quizProper():
    pause("\nPlease enter your name to proceed.\n")
    getName = input()
    time.sleep(1)
    pause(f"\nWelcome to your first math quiz, {getName}!\nThere are 10 random addition questions for you to answer. Your score will be revealed at the end of the quiz.\nBest of luck, iskolar ng bayan!\n \n")
    time.sleep(1)
    userScore = 0
    for q in range(1,11):
        sys.stdout.write(f"{q}.) ")
        sys.stdout.flush()
        correct = askQuestion()
        if correct:
            userScore += 1
            print(f"\nCorrect!\n")
        else:
            print(f"\nIncorrect. The answer is {ansKey}.\n")
    time.sleep(1)
    pauseNext("Calculating results...\n")
    if userScore >= 8: 
        pauseNext(f"\nYour final score is... {userScore}/10\n")
        print(f"Are you a math whiz? Sana all! Keep it up for our second math quiz!")
    elif userScore >= 5:
        pauseNext(f"\nYour final score is... {userScore}/10.\n")
        print(f"Amazing! Iskolar ng bayan yarn? Let's do even better in our second math quiz!")
    elif userScore >= 0:
        pauseNext(f"\nYour final score is... {userScore}/10.\n")
        print(f"That's a good try! Bawi na lang next life. Don't worry, there's still plenty of time to review.")
    pauseNext("\nEnd of first quiz...\n")
    
quizProper()





