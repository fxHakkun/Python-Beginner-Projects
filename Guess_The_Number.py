#Guess the number

import random

def guess(x):
    randomnumber = random.randint(1,x)
    guessnumber = 0
    while randomnumber != guessnumber:
        guessnumber = int(input(f"guess the number between 1 and {x} : "))
        if randomnumber > guessnumber:
            print("sorry too low, guess again")
        if randomnumber < guessnumber:
            print("sorry too high, guess again")
    print(f"You are correct ! {guessnumber} is the correct answer.")

guess(100)