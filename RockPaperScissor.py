import random

#rockpaperscissor
Choice = ['r', 'p', 's']
# r > s , p > r , s > p
of3 = 3

def play():
    computer = random.choice(Choice)
    user = input("Your choice of [R]rock, [P]paper, [S]scissor? :").lower()
    print(f"You use {user} and Computer using {computer}")
    if user == computer:
        return 'Draw'
    if is_lost(user,computer):
        return 'You lost'
    return 'You win'

def is_lost(player,opponent):
    if (opponent == 'r' and player == 's') or (opponent == 'p' and player == 'r') or (opponent == 's' and player == 'p'):
        return True

while of3 > 0:  #3 times play      
    print(play())
    of3 = of3 - 1