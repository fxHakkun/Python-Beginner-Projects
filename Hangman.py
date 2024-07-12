import random
import string
from Words import word

def valid_words(word):
    words = random.choice(word)
    while ' ' or '-' in words:
        words = random.choice(word)
    return words

def play_hangman():
    guess = valid_words(word)
    alphabet = string.ascii_uppercase
    word_letters = set(guess)
    used_letters = set()

    #getting user input
    while len(word_letters) > 0:
        #letters used
        print("You have used these letters: "," ".join(used_letters))
        #What current word is(ie W-RD)
        word_list = [letter if letter in used_letters else '-' for letter in guess]
        print("Current word:"," ".join(word_list))
        user_letter = input("Guess the letter : ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You already guessed that. Try again.")
        else:
            print("Invalid. Try again.")

    #gets here when len(word_letters) == 0
print(valid_words(word))
print('1')
print('2')
print('babi')
play_hangman()


