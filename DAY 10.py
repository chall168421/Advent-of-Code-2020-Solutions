from itertools import permutations, product

import re

def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString


def prod(seq):

    tot = 1
    for i in seq:
        
        tot *= i
    
    return tot

    
TAB = '\t'
NL = '\n'

example_input = '''0
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
52'''

with open("day10.txt") as f:
    puzzle_input = f.read()

    

example_input = example_input.split(NL)
puzzle_input = ("0\n" + puzzle_input).split(NL)

TARGET = 19208

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

    data = sorted(list(map(int, data)))


    one = 1
    three = 1

    i = 0

    chain(data)
    
    while i < count:

        jolt = data[i]
        #print(jolt)


        if jolt+1 in data:
            i = data.index(jolt+1)
            one += 1
            
        if jolt+3 in data:
            i = data.index(jolt+3)
            three += 1

        else:
            break

            


    
    return (one, three), data
         
    

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper


count = 0
def chain(data, i =0):
    global count

    count += 1
    log("\nBranch!")

    for x, d in enumerate(data):
        log("{}{}".format(" " if x != i else "!", d), end="")

    
    while i < len(data):
        jolt = data[i]
        possible = 0
        for j in range(1, 4):
            
            if jolt+j in data:
                possible += 1    
                i = data.index(jolt+j)
                if possible > 1:
                    chain(data, i)
             

        if possible == 0:
            break
            
                
                
    return count, data


def check_jolts(data):
    jolt_map = {}
    for i, d in enumerate(data):
        jolt_map[d] = set()
        for j in range(1, 4):
            if d + j in data:
                jolt_map[d].add(data[j])

    return jolt_map


        

def sum_jolts(jolt_map):
    end_point = GOAL
    total = 0
    while end_point > 0:
        possibilities = traverse(end_point, 0, jolt_map)
        

        

        
        

def solve2(data):
    
    data = sorted(list(map(int, data)))


    one = 1
    three = 1

    chain(data)

    

    result = count

    return result, data
    


    



LOG = False



print("Solving example")
result, data = solve2(example_input)
print("Result is", result)



if results[0] == TARGET:
    print("Success, solving puzzle input")

    results = solve2(puzzle_input)
    print("Result is", results[0])
    

    







