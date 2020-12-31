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

example_input = '''S1
E1
W1
N1
R90
F1
R180
F1
R270
F1
L90
F1
L180
F1
L270
F1
N1
F1
E1
F1'''


example_input = '''R90
R90
R90
R180
L90
L90
L180
R270
R90
L270
L180'''

example_input = '''F10
N3
F7
R90
F11'''

with open("day12.txt") as f:
    puzzle_input = f.read()

example_input = example_input.split(NL)
puzzle_input = puzzle_input.split(NL)

TARGET = 286


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
    


    vectors = """1,0
1,1
0,1
-1,1
-1,0
-1,-1
0,-1
1,-1""".split("\n")

    vectors = [list(map(int, v.split(","))) for v in vectors]

    directions = """east
south east
south
south west
west
north west
north
north east""".split("\n")
    
    d = 0

    east, north = 0, 0


    x_vel = 1
    y_vel = 0

    wp_north = -1
    wp_east = 10

    debug = False
    
    for line in data:
        log(line)

        amt = int("".join([i for i in line if i.isdigit()]))

        
        rotate = 0
                    
        if "S" in line:
            wp_north += 1 * amt
            log("going south")
        if "N" in line:
            wp_north += -1 * amt
            log("going north")
        if "E" in line:
            wp_east += 1 * amt
            log("going east")
        if "W" in line:
            wp_east += -1 * amt
            log("going west")
                        
        if "R" in line:
            rotate = 1
        elif "L" in line:
            rotate = -1
            

        if wp_north == 0 or wp_east == 0:
            debug = True

        if rotate:            
            turns = amt // 90

            if rotate == -1:
                if turns == 1:
                    turns = 3
                elif turns == 3:
                    turns = 1
                
                

            for i in range(turns):
                t = wp_east
                if wp_east >= 0 and wp_north <= 0:                
                    wp_east = abs(wp_north)                
                elif wp_east >= 0 and wp_north >= 0:                
                    wp_east = 0 - wp_north          
                elif wp_east <= 0 and wp_north >= 0:
                    wp_east = 0 - wp_north
                    
                else:
                    wp_east = abs(wp_north)
                wp_north = t

            
            

        if "F" in line:
            
            
            log("going", d)


            
            east += wp_east * amt
            north += wp_north * amt

   
        log("wp is", wp_east, wp_north)
        log("new pos", east, north)

    
    result = sum([abs(east), abs(north)])
    
    return result, data
         
    
    
    
def solve2(data, target=10884537):    
    return result, data
    


    



LOG = False

puzzle_input.remove("")
print("Solving example")
results = solve(example_input, param=5)
print("Result is", results[0])
if results[0] == TARGET:
    print("Success, solving puzzle input")
    input()
    results = solve(puzzle_input, param=25)
    print("Result is", results[0])
    

    







