import random
import string
from Words import word
from HangmanVisual import lives_visual_dict

def valid_words(word):
    words = random.choice(word)
    while ' ' in words or '-' in words:
        words = random.choice(word)
    return words.upper()

def play_hangman():
    lives = 7
    x = 0
    words = valid_words(word)
    alphabet = set(string.ascii_uppercase)
    word_letters = set(words)
    used_letters = set()

    #getting user input
    while len(word_letters) > 0 and lives > 0:

        #letters used
        print("You have used these letters: "," ".join(used_letters))

        #What current word is(ie W-RD)
        word_list = [letter if letter in used_letters else '-' for letter in words]
        print("Current word: "," ".join(word_list))

        user_letter = input("Guess a letter : ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            #Condition to minus lives
            else:
                lives = lives - 1
                x = x + 1
                print(f"Try again. The letter {user_letter} is not in the word.\nRemaining lives : {lives}")
                if x < 7:
                    print(lives_visual_dict[x])

        elif user_letter in used_letters:
            print("You already used that. Try again.")
        else:
            print("Invalid input. Try again.")

    #gets here when len(word_letters) == 0

    if lives == 0:
        print(f"The man is hanged, you fail to save him. The word is {words}")
        print(lives_visual_dict[x])

    else:
        word_list = [letter if letter in used_letters else '-' for letter in words]
        used_letters.add(user_letter)
        print(" ".join(word_list))
        print(f"You won ! {words} is the word !")
        print(lives_visual_dict[8])

#Execute the code
play_hangman()


