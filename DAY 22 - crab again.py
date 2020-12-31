from itertools import combinations

import numpy as np

# preallocate empty array and assign slice by chrisaycock
def shift(arr, num, fill_value=np.nan):
    result = np.empty_like(arr)
    if num > 0:
        result[:num] = fill_value
        result[num:] = arr[:-num]
    elif num < 0:
        result[num:] = fill_value
        result[:num] = arr[-num:]
    else:
        result[:] = arr
    return result

import re

def replacenth(string, sub, wanted, n):
    np.where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:np.where]
    after = string[np.where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString

    
TAB = '\t'
NL = '\n'

example_input = list('''389125467''')



puzzle_input = list('789465123')

##example_input = example_input.split(NL)
##puzzle_input = puzzle_input.split(NL)

TARGET = 149245887792


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


class Cups(list):

    def __init__(self, items):

        self.cups = list(map(int, items))

        if PARTB:
            self.cups += list(range(max(self.cups) + 1, 1000001))

        self.cups = np.array(self.cups)
        self.hi = max(self.cups)
        self.lo = min(self.cups)
        self.reposition = []
        self.current = self.cups[0]
        self.record = []
        self.size = len(self.cups)


    def append(self, new):
        self.cups.append(new)


    def do_move(self, move):

        

        last_cup_string = None


        log("-- move {} --".format(move+1))

        self.reposition = []

        i = np.where(self.cups, self.current)
        

        log("current is", self.current)

##        log("cups: ", end="")
##        for j, cup in enumerate(self.cups[:20]):
##            log(" {} ".format(cup) if j != i else "({})".format(cup), end="")
##
##        log()

        if move == FINAL:

            if PARTB:

                cup1 = np.where(self.cups, 1)
                tot = []
                for i in range(2):
                    cup1 += 1
                    if cup1 == self.size:
                        cup1 = 0

                    tot.append(self.cups[cup1])

                return tot[0] * tot[1]
            else:
                return self.cups
                    
            
    
        to_remove = []
        i += 1
        
        for x in range(3):
            if i == len(self.cups):
                i = 0


            self.reposition.append(i)
            


        log("pick up: {}".format(", ".join([self.cups[i] for i in self.reposition])))

        destination = self.current-1
        if destination < self.lo:
                destination = self.hi

        while destination in self.reposition:
            destination -= 1
  
            if destination < self.lo:
                destination = self.hi
                
        
        log("destination:", destination)


        destination_index = np.where(self.cups, destination) + 1

        for y in range(3):
            return_cup = self.reposition.pop(-1)

            
        
   
        
        next_cup = np.where(self.cups, self.current) + 1

        if next_cup == self.size:
            next_cup = 0
        
        self.current = self.cups[next_cup]


        if not PARTB:
            log(self.cups)
        
            
        
LOG = True

def solve(data, param):



    current = 0

    cups = Cups(data)

    for move in range(FINAL):

        if move % 10000 == 0:
            print(move)

        result = cups.do_move(move)

    print(result)




        

        
    

        


    return result, data
         
    
    
    
def solve2(data, target=10884537):    
    return result, data
    


FINAL = 10000000

PARTB = True



LOG = False



results = solve(example_input, param=25)
print("Example test results", results)


print("Success, solving puzzle input")
#input()
results = solve(puzzle_input, param=25)
print("Result is", results)










