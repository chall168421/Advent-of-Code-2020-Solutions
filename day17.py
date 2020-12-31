from math import ceil
from itertools import combinations, permutations
import heapq
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
            log("{1}{0}{1}".format(i, p))
        log()


        

def get_neighbours(cube, z, y, x, debug=False):
    if debug:
        log("This cube is at {} {} {}".format(z, y, x))

    for f in [-1, 0, 1]:
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                if f == r == c == 0:
                    continue

                
                    

                new_z = z + f
                new_y = y + r
                new_x = x + c

                if debug:
                    log("Checking neighbour at {} {} {}".format(new_z, new_y, new_x))

                
                try:
                    n = cube[new_z][new_y][new_x]
                    if debug:
                        log("result:", n)
                    yield n
                except:
                    yield "."         


def print_cube(cube, faces=None):
    for i, face in enumerate(cube):
        view_port_found = False
        if faces is None:
            print("face", i)
        else:
            print("faces", faces[i])
        for y, row in enumerate(face):
            if "#" in row:
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

    start_state = []

    max_buffer = 0

    for line in data.split(NL):      

        if not max_buffer:            
            max_buffer = len(line) * (2 * 5)
            for i in range((max_buffer//2)-1):                        
                start_state.append(list("." * max_buffer))
        
        line_buffer = ceil((max_buffer - len(line)) // 2) * "."
        final_line = list(line_buffer + line + line_buffer)

        final_line = (final_line*2)[:max_buffer]
        start_state.append(list(final_line))

    for i in range((max_buffer//2)-2):                        
        start_state.append(list("." * max_buffer))


    # leading empty faces

    # trailing empty faces
    cube = []
    for j in range(max_buffer):
        cube.append([]) # APPEND A FACE
        for i in range(max_buffer):                        
            cube[-1].append(list("." * max_buffer)) # APPEND EACH ROW TO THE FACE

    log(start_state)

    cube[len(cube)//2] = list(start_state) # MAKE THE MIDDLE FACE


    log(len(cube))
    input()



    try:

        state = list(cube)

        populated_faces = [len(cube) // 2]

        next_state = deepcopy(state)

        for cycle_no in range(6):



            print("Starting cycle", cycle_no)
            active_count = 0
            for z, face in enumerate(state):

                if any(["#" in row for row in face]):
                    log("active face", z, face)
                    active_face = True
                else:
                    active_face = False
            
                for y, row in enumerate(face):
                    for x, cell in enumerate(row):
                        cube = state[z][y][x]
                        n = list(get_neighbours(state, z, y, x))

                        if cycle_no == 0 and n.count("#") > 5:
                            log("neighbour error")
                            log("I'm at [{}, {}, {}] I am {} and got neighbours {}".format(z, y, x, cube, n))

                            n = list(get_neighbours(state, z, y, x, debug=True))
                            input()


                        if "#" in n:
                            log("I'm at [{}, {}, {}] I am {} and got neighbours {}".format(z, y, x, cube, n))

                    
                        if cube == "." and n.count("#") == 3:
                            
                            next_state[z][y][x] = "#"
                            
                            log("switch active")
  
                            active_count += 1

                            
                        elif cube == "#" and n.count("#") not in [2, 3]:
                            
                            next_state[z][y][x] = "."
                            log("switch inactive")
                        elif cube == "#":
                            
                            log("remain active")
      

                            active_count += 1

            

            log(active_count, "active")

            front = populated_faces[0]        
            back = populated_faces[-1]
            populated_faces = [front-1] + populated_faces + [back+1]

            log(populated_faces)

            populated_cube = [f for i, f in enumerate(next_state) if i in populated_faces]
            
            print_cube(populated_cube, faces=populated_faces)
            print("Finished cycle", cycle_no)

            state = deepcopy(next_state)

    

    except KeyboardInterrupt:
        return 0, state
                
    return sum([sum([row.count("#") for row in face]) for face in state]), state


LOG = False


print("Solving example")
result, data = solve(example_input, cap=2020)
print("results")
print(result)
print("Target")
print(target)


print("Success, solving puzzle input")

results = solve(puzzle_input, cap=30000000)
print("Result is", results[0])










