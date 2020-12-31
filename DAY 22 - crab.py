from itertools import combinations
from copy import deepcopy

import re

def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString

    
TAB = '\t'
NL = '\n'

example_input = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''

##example_input = '''Player 1:
##43
##19
##
##Player 2:
##2
##29
##14'''
##


with open("day22.txt") as f:
    puzzle_input = f.read()

example_input = example_input.split(NL)
puzzle_input = puzzle_input.split(NL)

TARGET = 291


def log(*s, end=NL):
    if LOG:
        for i in s:
            print(i, end=" ")
        print(end, end="")

def print_grid(data):
    for i, row in enumerate(data):
        for j, cell in enumerate(row):

            p = ' '
            if i == y and j == x:
                p = '!'
            log("{1}{0}{1}".format(i, p))
        log()


def solve(data, param):
    player1 = []
    player2 = []
    deck = player1
    for line in data[1:]:
        if "Player" in line:
            deck = player2
            continue
        if line.strip() == "":
            continue
        deck.append(int(line))



    return combat(player1, player2)


global game_no
game_no = 0

def subgame(player1, player2):
    global game_no

    game_no += 1

    round = 1

    state = []

    win = 0

    while len(player1) and len(player2):

        log("-- Round {} (Game {}) --".format(round, game_no))
      


        

        log("Player 1's deck", player1)
        log("Player 2's deck", player2)

        
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        log("Player 1 drew", card1)
        log("Player 2 drew", card2)

        if len(player1) >= card1 and len(player2) >= card2:
            
            win, winner = subgame(deepcopy(player1[:card1]), deepcopy(player2[:card2]))
            

        elif card1 > card2:
            win = 1
            winner = player1
        else:
            win = 2
            winner = player2

        if win == 1:
            log("Player 1 wins round {} of game {}".format(round, game_no))
            player1.append(card1)
            player1.append(card2)
        else:
           
            player2.append(card2)
            player2.append(card1)
            log("Player 2 wins round {} of game {}".format(round, game_no))
##        winner.append(max([card1, card2]))
##        winner.append(min([card1, card2]))
        

        round += 1

        round_hash = "".join([str(i) for i in player1 + ["|"]    + player2])

        if round_hash in state:
            win = 999
            break

        else:
            state.append(round_hash)



        

    if len(player1) or win == 999:
        log("The winner of game {} is player 1!".format(game_no))
        game_no -= 1
        return 1, player1
    else:
        log("The winner of game {} is player 2!".format(game_no))
        game_no -= 1
        return 2, player2


    

def combat(player1, player2):
    global depth
    depth = 1

    
    tot = 0


    win, player = subgame(player1, player2)

   


    for i, v in enumerate(reversed(player)):
        tot += (i+1) * v

    return tot

        
    

    
    
def solve2(data, target=10884537):    
    return result, data
    


    



LOG = False

puzzle_input.remove("")
print("Solving example")
results = solve(example_input, param=5)
print("Result is", results)

print("Success, solving puzzle input")
input()
results = solve(puzzle_input, param=25)
print("Result is", results)










