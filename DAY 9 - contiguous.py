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

example_input = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''

with open("day6.txt") as f:
    puzzle_input = f.read()

example_input = example_input.split(NL)
puzzle_input = puzzle_input.split(NL)

TARGET = 62


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


def solve(data, preamble=5):
    
   
    data = list(map(int, data))

    prev = list(data[0:preamble])

    for num in data[preamble:]:
        #print(num)
     
        valid = False
        for n in prev[-preamble:]:
            
            for n2 in prev[-preamble:]:
                if n == n2 or n == num:
                    continue
                if n + n2 == num:
                  
                    valid = True
                    break
            if valid:
                break
            
        if not valid:
            return solve2(data, num)
            
            

        prev.append(num)



         
    
    
    
def solve2(data, target=10884537):
    tot = 0

    highest = list(map(int, data)).index(target)

    data = tuple(map(int, data))
    tried = set()
    print(data)
    lowest = 0
    comb_tot = 0
    print("Finding contiguous set that adds up to {} in above ^".format(target))


    top = 0
       
    for index, number in enumerate(data):

        if comb_tot > target:
            lowest += 1
            
        min_needed = 2

        for comb_start in range(lowest, highest):
            
            comb_tot = 0
            
            comb_length = 1
            while comb_tot < target:
                comb_length += 1

                
                #print("Max comb_length is", comb_length) 
            
                comb = set(data[comb_start:comb_start+comb_length])
                hash_comb = hash("".join(str(i) for i in comb))
                if hash_comb in tried:
                    continue
                else:
                    tried.add(hash_comb)

                #print("Does {} add up to {}?".format(comb, target))               
               
                comb_tot = sum(comb)
                if comb_tot == target:
                    print("Success")
                    print(comb)
                    print("biggest + smallest is")
                    print( min(comb) + max(comb))
                    return min(comb) + max(comb),data
                
                if comb_tot > target:
                    break
        


    



LOG = True


puzzle_input.remove("")
print("Solving example")
results = solve(example_input, preamble=5)
print("Result is", results[0])
if results[0] == TARGET:
    print("Success, solving puzzle input")
    input()
    results = solve(puzzle_input, preamble=25)
    print("Result is", results[0])
    

    







