import random

#rockpaperscissor
Choice = ['r', 'p', 's']
# r > s , p > r , s > p
of3 = 3

def play():
    computer = random.choice(Choice)
    user = input("Your choice of [R]rock, [P]paper, [S]scissor? :").lower()
    if user == computer:
        standardized(user,computer)
        return 'Draw'   
    if is_lost(user,computer):
        standardized(user,computer)
        return 'You lost'
    standardized(user,computer)
    return 'You win'

def standardized(user,computer): # Just to beautify the representation, but is there any other shorter way? too many if lol
    if user == 'r':
        user = 'Rock'
    if user == 'p':
        user = 'Paper'
    if user == 's':
        user = 'Scissor'
    if computer == 'r':
        computer = 'Rock'
    if computer == 'p':
        computer = 'Paper'
    if computer == 's':
        computer = 'Scissor'
    print(f"You use {user} and Computer using {computer}")  

def is_lost(player,opponent):
    if (opponent == 'r' and player == 's') or (opponent == 'p' and player == 'r') or (opponent == 's' and player == 'p'):
        return True

while of3 > 0:  #3 times play      
    print(play())
    of3 = of3 - 1
