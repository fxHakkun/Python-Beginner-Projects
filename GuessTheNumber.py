#Guess the number

import random

def guess(x):
    randomnumber = random.randint(1,x)
    lives = random.randint(5,10)
    guessnumber = 0
    print("You guess me first")
    while randomnumber != guessnumber and lives != 0:
        guessnumber = int(input(f"Lives begin with {lives}. guess the number between 1 and {x} : "))
        if randomnumber > guessnumber:
            print("sorry too low, guess again")
            lives = lives - 1
            print(f" Lives = {lives}")
        elif randomnumber < guessnumber:
            print("sorry too high, guess again")
            lives = lives - 1
            print(f"Lives = {lives}")
    if lives == 0:
        print(f"Lives has turned {lives} . Sorry you lost, The correct number is {randomnumber} ")
    if randomnumber == guessnumber:
        print(f"You are correct ! {guessnumber} is the correct answer.")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    lives = random.randint(5,10)
    print("Let me guess you next.")
    while feedback != 'y' and low != high and lives != 0 :
        guess = random.randint(low,high)
        feedback = input(f"Lives begin with {lives} does {guess} is correct? (Y) is too high? (H) or too low? (L)").lower()
        if feedback == 'h':
            high = guess - 1
            lives = lives -1
            print(f"Lives = {lives}")
        elif feedback == 'l':
            low = guess + 1
            lives = lives -1
            print(f"Lives = {lives}")
    if low == high: #adding if on while cause I determined the computer guess wrong but deemed correct when high and low is the same thus it skip the process
        guess = low
        feedback = input(f"{guess} is correct? (Y)").lower()
    if lives == 0:
        print(f"Lives has turned {lives}")
        guess = int(input("What is the correct number? "))
        print(f"You win ! , the computer lose. Computer can't guess {guess} as the correct number")
    if feedback == 'y':
        print(f"Correct! Computer guess the number {guess} correctly.")
    
x = int(input("Set the high?" )) #just to vary the fun

guess(x)
computer_guess(x)