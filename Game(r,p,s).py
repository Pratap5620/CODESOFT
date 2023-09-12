# -*- coding: utf-8 -*-
"""
Created on Mon Sep  11 13:32:30 2023

@author: om123
"""

from numpy import random
import sys

''' Creating Rock Paper and Scissor game'''

wins = 0
losses = 0
tie = 0
    
while True:
    print("Enter Player's Move: (r)ock (p)aper and (s)cissor or (q)uit")
    
    player_move = input("Enter Player's Move: ")
    
    if player_move == 'q':
        sys.exit()#Quit the Game
    if player_move == 'r' or player_move == 'p' or player_move == 's':
        break
    print("type one of r, p or s")
    
"""Creating players move"""

if player_move =='r':
    print("Rock versus....")
elif player_move=='p':
    print("Paper versus....")
elif player_move=='s':
    print("scissor versus....")

"""Creating computers move"""

random_number = random.randint(1,3)
if random_number==1:
   computer_move = 'r'
   print("Rock")
elif random_number==2:
    computer_move='p'
    print("Paper")
elif random_number==3:
    computer_move='s'
    print("Scissor")

"""Creating gaming condition"""


if player_move==computer_move:
    print("It's a tie.")
    tie =tie+1
elif player_move=='r' and computer_move =='s':
    print("You win")
    wins=wins+1
elif player_move=='p' and computer_move =='r':
    print("You win")
    wins=wins+1
elif player_move=='s' and computer_move =='p':
    print("You win")
    wins=wins+1
elif player_move=='r' and computer_move =='p':
    print("You lose!")
    losses =losses+1
elif player_move=='s' and computer_move =='r':
    print("You lose!")
    losses =losses+1
elif player_move=='p' and computer_move =='s':
    print("You lose!")
    losses =losses+1
