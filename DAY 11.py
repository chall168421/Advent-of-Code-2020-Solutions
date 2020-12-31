from itertools import combinations

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

example_input = ''''''

with open("day6.txt") as f:
    puzzle_input = f.read()

example_input = example_input.split(NL)
puzzle_input = puzzle_input.split(NL)

TARGET = None


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
    return result, data
         
    
    
    
def solve2(data, target=10884537):    
    return result, data
    


    



LOG = True


puzzle_input.remove("")
print("Solving example")
results = solve(example_input, param=5)
print("Result is", results[0])
if results[0] == TARGET:
    print("Success, solving puzzle input")
    input()
    results = solve(puzzle_input, param=25)
    print("Result is", results[0])
    

    







