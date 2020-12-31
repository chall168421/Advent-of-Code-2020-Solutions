from math import ceil
from itertools import combinations, permutations
import heapq
from copy import deepcopy
import numpy as np

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

example_input = '''.#.
..#
###'''



puzzle_input = """"""

target = 112



with open("day17.txt") as f:
    puzzle_input = f.read()


examples = [example_input]




def log(*s, end=NL):
    if LOG:
        for i in s:
            print(i, end=" ")
        print(end, end="")

def log_grid(data):
    for i, row in enumerate(data):
        for j, cell in enumerate(row):

            p = ' '
            if i == y and j == x:
                p = '!'
            ##log("{1}{0}{1}".format(i, p))
        #log()


        

def get_neighbours(tesseract, w, z, y, x, debug=False):
    if debug:
        pass
        #log("This cube is at {} {} {}".format(w, z, y, x))

    for cu in [-1, 0, 1]:
        for f in [-1, 0, 1]:
            for r in [-1, 0, 1]:
                for c in [-1, 0, 1]:
                    if f == r == c == cu == 0:
                        continue

                    
                        
                    new_w = w + cu
                    new_z = z + f
                    new_y = y + r
                    new_x = x + c

                    if debug:
                        pass
                        #log("Checking neighbour at {} {} {} {}".format(new_w, new_z, new_y, new_x))

                    
                    try:
                        n = tesseract[new_w][new_z][new_y][new_x]
                        if debug:
                            pass
                            #log("result:", n)
                        yield n
                    except:
                        yield 0         


def print_cube(tesseract, cube_nums=None):
    for j, cube in enumerate(tesseract):
        if cube_nums is None:
            print("cube", j)
        else:
            print("cube", cube_nums[j])
        for i, face in enumerate(cube):
            view_port_found = False

            print("face", i)
            
            for y, row in enumerate(face):
                if 1 in row:
                    view_port_found = True
                else:
                    view_port_found = False
                for x, cell in enumerate(row):
                    
                

                    if view_port_found:
                        print(cell, end="")

                if view_port_found: 
                    print()
                    
                    


def solve(data, cap):
    answer = None
    start_state = data
    data = data.replace(".", "0").replace("#", "1")
    data = data.split(NL)

    first_line = data[0]

    dimension = 0

    dimension = len(first_line) * (2 * 5)

    

    start_state = np.full((dimension, dimension), 0, dtype=int, order='C')
    
        
    write_line = (dimension // 2) - len(first_line)//2
    
    for line in data:   
        
        line_buffer = (dimension - len(line) // 2) * [0]
        final_line = line_buffer + list(map(int, line)) + line_buffer
        final_line = (final_line*2)[:dimension]
        start_state[write_line] = deepcopy(final_line)
        write_line += 1


    
    # leading empty faces

    # trailing empty faces

    tesseract = np.full((dimension, dimension, dimension, dimension), 0, dtype=int, order='C')

    m = dimension//2

    tesseract[m][m] = start_state
    

    


    try:

        input("tesseract complete")

        state = deepcopy(tesseract)

        

        next_state = deepcopy(state)

        dims_in_use = [m-1, m, m+1]
        

        for cycle_no in range(6):


            
            print("Starting cycle", cycle_no)
            active_count = 0
            for w, cube in enumerate(state):
                print("cube", w)
                if w not in dims_in_use:
                    print("skipping")
                    continue

                
                for z, face in enumerate(cube):
                    if z not in dims_in_use:
                        continue

                    if any([1 in row for row in face]):
                        #log("active face", z, face)
                        active_face = True
                    else:
                        active_face = False
                
                    for y, row in enumerate(face):
                        
                        
                        for x, cell in enumerate(row):
                            track = False
                            hypercube = state[w][z][y][x]
                            n = list(get_neighbours(state, w, z, y, x))

                                
                        
                            if hypercube == 0 and n.count(1) == 3:
                                
                                next_state[w][z][y][x] = 1
                                
                                if track:
                                    print("I am {} at coords {} {} {} {}. Neigbours {}".format(cube, w, z, y, x, n))
                                    print("switch active")
                                    input()
      
                                active_count += 1

                                
                            elif hypercube == 1 and n.count(1) not in [2, 3]:
                                
                                next_state[w][z][y][x] = 0
                                if track:
                                    print("switch inactive")
                            elif cube == 1:
                                
                                if track:
                                    print("remain active")
          

                                active_count += 1


            

            print(active_count, "active")
            
            print("Finished cycle", cycle_no)

            state = deepcopy(next_state)

            active_count = sum([sum([sum([np.count_nonzero(row == 1) for row in face]) for face in cube]) for cube in state])

            print("Active:", active_count)
            dims_in_use = [dims_in_use[0]-1] + dims_in_use + [dims_in_use[-1]+1]

    

    except KeyboardInterrupt:
        return 0, tesseract
                
    return active_count, state


LOG = False




print("Success, solving puzzle input")

results = solve(puzzle_input, cap=30000000)
print("Result is", results[0])










