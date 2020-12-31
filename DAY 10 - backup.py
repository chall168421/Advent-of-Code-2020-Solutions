from itertools import combinations

from collections import Counter

from functools import lru_cache

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

puzzle_input = list(map(int, puzzle_input))

puzzle_input = puzzle_input + [max(puzzle_input) + 3]

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
         




def chain(data, i =0, count=0):

    count += 1    

    while i < len(data):
        jolt = data[i]
        possibilities = 0
        for j in range(1, 4):
            if jolt+j in data:
                pos = data.index(jolt+j)
                possibilities += 1
                if possibilities > 1:
                    count = chain(data, pos, count)
                else:
                    i = pos

        if possibilities == 0:
            #print("No poss")
            return count
    return count


@lru_cache(maxsize=2048, typed=False)
def traverse(node=0, count=1):
    
    counter.update([node])
    for i, link in enumerate(nodes[node].paths):

        if i > 0:
            count += 1

        
        count = traverse(link, count=count)
    
    return count
        


def solve3(data, i =0, count=0):

    data = sorted(list(map(int, data)))


    class Node:
        def __init__(self, v):
            self.value = v
            self.paths = set()

        def __repr__(self):
            return str(self.value)

        def get_paths(self):
            return "I link to {}".format([str(i) for i in self.paths])

    for num in data:
        try:
            this_node = nodes[num]
        except Exception:
            nodes[num] = Node(num)
            this_node = nodes[num]

        for i in range(1, 4):
            if num+i in data:
                try:
                    link_node = nodes[num+i]
                except Exception:
                    nodes[num+i] = Node(num+i)
                    link_node = nodes[num+i]

                log("Just linked {} to {}".format(this_node, link_node))
                this_node.paths.add(num+i)


    


    for n in nodes.values():
        log(n)
        log(n.get_paths())

    

    result = traverse(0)
        
                

    
    return result, nodes  

    
    

def solve4(data):
    data = sorted(list(map(int, data)))
    for i, d in enumerate(data[:-1]):
        this = d
        next_ = data[i+1]

        print(next_ - this, end=", ")

    return 0, data
           
def solve2(data):
    
    data = sorted(list(map(int, data)))


    one = 1
    three = 1

    

    result = new_chain(data, 0, 0)

    

    return result, data


            
            
    
counter = Counter()


LOG = False

nodes = {}

print("Solving example")
result, data = solve4(example_input)
print("Result is", result)

results = [TARGET, None]

input()
if results[0] == TARGET:
    nodes = {}
    traverse.cache_clear()
    print("Success, solving puzzle input")
    results = solve4(puzzle_input)
    print("Result is", results[0])
    

    







