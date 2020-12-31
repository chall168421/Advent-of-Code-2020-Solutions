from itertools import combinations
import heapq

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

example_input = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''



puzzle_input = "16,11,15,0,1,7"
##
##with open("day14.txt") as f:
##    puzzle_input = f.read()

##example_input = example_input.split(",")
##puzzle_input = puzzle_input.split(",")

TARGET = 208


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

    data = list(map(int, data.split(",")))

    print(data)

    last = None
    spoken = list()
    turn = 1
    while turn != 2020 + 1:
        if len(spoken) == 0:
            for n in data:
                log("turn", turn)
                spoken.append(n)
                log(spoken)
                turn += 1
        log("turn", turn)
        num = data[(turn-1) % len(data)]
        

        if spoken.count(last) <= 1:
            spoken.append(0)
        else:
            log("check last", last)
            last_spoken = len(spoken) - list(reversed(spoken)).index(last)
            log("last spoken", last_spoken)
            cut_list = list(spoken[:last_spoken-1])
            try:
                second_last_spoken =    len(cut_list) - list(reversed(cut_list)).index(last)
                log("last time spoken", second_last_spoken)
                spoken.append( last_spoken  - second_last_spoken)
            except:
                spoken.append(1)
            

        last = spoken[-1]
        turn += 1
        log(spoken)
        if LOG:
            input()


    return spoken[-1], data
        
        


    

    
def speak_num(discard, spoken, n, turn):

    if n in spoken:        
        spoken[n].append(turn)
        if len(spoken[n]) > 2:
            discard.add(spoken[n].pop(0))
    else:
        spoken[n] = [turn]

        
    
def solve2(data, cap=2020):    
   

    data = list(map(int, data.split(",")))

    print(data)

    last = None
    spoken = {}
    turn = 1
    discard = set()
    
    while turn != cap + 1:
        if len(spoken.values()) == 0:
            for n in data:
                #log("turn", turn)
                speak_num(discard, spoken, n, turn)
                log(spoken)
                turn += 1

##        log(turn)

##        log("last is", last)
        
        if  last is None or len(spoken[last]) <= 1 and last not in discard:            
            speak_num(discard, spoken, 0, turn)
           
            last = 0
        else:

            

            try:
                last_spoken = spoken[last][1]
                second_last_spoken = spoken[last][0]
                diff = last_spoken - second_last_spoken
##                log("diff is", diff)
                speak_num(discard, spoken, diff, turn)
                last = diff
            except:
                speak_num(discard, spoken, 0, turn)
                last = 0

##        log(spoken)
##        if LOG:
##            input()
        
        turn += 1
        if turn % 300000 == 0:
            print(turn, "turn")


    return last, spoken


example_set_1 = """Given 0,3,6, the 2020th number spoken is 436.
Given 1,3,2, the 2020th number spoken is 1.
Given 2,1,3, the 2020th number spoken is 10.
Given 1,2,3, the 2020th number spoken is 27.
Given 2,3,1, the 2020th number spoken is 78.
Given 3,2,1, the 2020th number spoken is 438.
Given 3,1,2, the 2020th number spoken is 1836."""
    
example_set_2 = """Given 0,3,6, the 30000000th number spoken is 175594.
Given 1,3,2, the 30000000th number spoken is 2578.
Given 2,1,3, the 30000000th number spoken is 3544142.
Given 1,2,3, the 30000000th number spoken is 261214.
Given 2,3,1, the 30000000th number spoken is 6895259.
Given 3,2,1, the 30000000th number spoken is 18.
Given 3,1,2, the 30000000th number spoken is 362."""
LOG = False
##
for line in example_set_1.split("\n"):

    target = line.split(" ")[-1][:-1]
    data = line.split(" ")[1][:-1]


    


    print("Solving example")
    results = solve2(data, cap=2020)
    print("results")
    print(results[0])
    print("Target")
    print(target)
    input()
    

    

print("Success, solving puzzle input")

results = solve2(puzzle_input, cap=30000000)
print("Result is", results[0])










