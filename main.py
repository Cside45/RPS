""""
Simplistic rock paper scissors game!
Cside45 - 7/20/2020
"""
import random


def chooser():
    rpc = ['Rock', 'Paper', 'Scissors']
    print('Adversary -', random.choice(rpc))


def player():
    print('1 = Rock, 2 = Paper 3 = Scissors')
    hand = int(input('Choose your selection:'))

    if hand == 1:
        print('Player - Rock')
    if hand == 2:
        print('Player - Paper')
    if hand == 3:
        print('Player - Scissors')
    if hand > 3:
        print("Please make an appropriate selection")
        player()
    if hand < 1:
        print('Please make an appropriate selection')
        player()


player()

chooser()





