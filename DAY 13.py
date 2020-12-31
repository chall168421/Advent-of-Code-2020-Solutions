from itertools import combinations

from functools import reduce

    

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

example_input = '''939
7,13,x,x,59,x,31,19'''


##
##with open("day13.txt") as f:
##    puzzle_input = f.read()


puzzle_input = '''1003681
23,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,431,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,x,x,409,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'''

example_input = example_input.split(NL)
puzzle_input = puzzle_input.split(NL)

TARGET = 1068781


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


    ts = int(data[0])

    in_service = [[int(d), 0] for d in data[1].split(",") if d != "x"]

    

    
    for bus in in_service:

        t = 0
        while t < ts:
            t += bus[0]

        bus[1] = t

        
         

    shortest = min(in_service, key=lambda x:x[1])

    wait_time =  abs(ts - shortest[1])
    
    return shortest[0] * wait_time, data
    


def solve2(data, param):

    data = data.split(",")

    comp_buses = [[int(d), i] for i, d in enumerate(data) if d != "x"]
            
    bus = comp_buses[0][0]
    log("Checking bus", bus)
    ts = 0

    print(comp_buses)
    
    
    comp_buses = comp_buses[1:]

    n = [n[0] for n in comp_buses]
    a = [n[1]+bus for n in comp_buses]

    x = chinese_remainder(n, a)
        
        

    while True:

        ts += bus  
        
        if all([(ts + i) % c == 0 for c, i in comp_buses]):
        
            return ts, data

        
                
def solve3(data, param):

    data = data.split(",")

    from chinese_remainder import find_chinese_remainder

    comp_buses = [[int(d), i] for i, d in enumerate(data) if d != "x"]

    first_bus = comp_buses[0]


    all_mods = []
    all_targets = []

    for other_bus in comp_buses[1:]:
        all_mods.append([first_bus[0], other_bus[0]])
        all_targets.append([other_bus[1], 0])
        
    
    res = find_chinese_remainder(all_mods, all_targets)


    lowest = 999
    

    for (ts, mod) in res:

        delay = [b[1] for b in comp_buses if b[0] == mod][0]

        if delay < lowest:
            first_bus_ts = ts - delay
        print("bus {} will arrive at {}. This needed to be {} mins after first bus {}".format(mod, ts, delay, first_bus))

   
        
    return first_bus_ts, data


examples = '''The earliest timestamp that matches the list 17,x,13,19 is 3417.
67,7,59,61 first occurs at timestamp 754018.
67,x,7,59,61 first occurs at timestamp 779210.
67,7,x,59,61 first occurs at timestamp 1261476.
1789,37,47,1889 first occurs at timestamp 1202161486.
7,13,x,x,59,x,31,19 first occurs at timestamp 1068781'''.split("\n")


for line in examples:
    try:
        data, target = line.split(" first occurs at timestamp ")
    except:
        data, target = line.split(" is ")
        data = data.split(" ")[-1]

    
    


    LOG = True

    print("Solving example")
    results = solve3(data, param=5)
    print("Result is", results[0])
    print("Target was", target)
    input()

print("Success, solving puzzle input")
results = solve3(puzzle_input[1], param=25)
print("Result is", results[0])
    

    






 
