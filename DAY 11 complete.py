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

example_input = 


with open("day11.txt") as f:
    puzzle_input = f.read()

example_input = [list(row) for row in list(example_input.split(NL))]
puzzle_input = [list(row) for row in list(puzzle_input.split(NL))]

TARGET = 26


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



def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end="")
        print()
        
def solve(data, param):
    grid = [list(row) for row in list(data)]

    state_change = True

    overall_change = True

    count = 0

    last_three = []
    while overall_change:
        
        count += 1

        overall_change = False

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                seat = data[y][x]
                if seat == ".":
                    #print(x, y)
                    continue
                state_change = False
                #print(x, y)

                #If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
                #If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
                
                
                n = get_los(data, x, y)
                neighbours = list(n)

                if count > 9999:
                
                    print("{} {} is {}, can see {}".format(x, y, seat, neighbours))
                    print(seat)
                    print(neighbours)
                    print(all([i in list("L.") for i in neighbours]))
                    print(len([i=="#" for i in neighbours]) >= 5)
                    input()
                if seat == "L" and all([i in "L." for i in neighbours]):
                    grid[y][x] = "#"
                    state_change = True
                elif seat == "#" and [i=="#" for i in neighbours].count(True) >= 5:
##                    print("Happens")
                    grid[y][x] = "L"
                    state_change = True
##
                if state_change:
                    overall_change = True
                    if count > 9999:
                        print(x, y, "state change")
                        input()

                
                



        if data == grid:            
            occupied = sum([row.count("#") for row in grid])            
            return occupied, last_three
        else:
            data = [list(row) for row in list(grid)]
            #print_grid(grid)
            #print()
            #input()
            
    
        
             
 



   
         
    
    
    
def solve2(data, target=10884537):    
    return result, data
    


def get_neighbours(grid, x, y):

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue
            
            new_y = i + y
            new_x = j + x

            if new_y >= len(grid) or new_y < 0:
                continue
            elif new_x >= len(grid[0]) or new_x < 0:
                continue

            try:
                yield grid[new_y][new_x]
            except:
                print(new_y, new_x)
                input()


def get_los(grid, x, y):

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue

           

            new_y = i + y
            new_x = j + x

            if new_y >= len(grid) or new_y < 0:
                continue
            elif new_x >= len(grid[0]) or new_x < 0:
                continue

            #print("Can I see", new_x, new_y)
            
            empty_los = grid[new_y][new_x] == "."

            out_of_range = False
            while empty_los and not out_of_range:
##                print("yes")
                
               
                #print(i)
                #print("empty")
                new_y += i
                new_x += j
##                print("Can I see", new_x, new_y)
##                input()
                #print(new_x, new_y)
                

                if new_y >= len(grid) or new_y < 0:
##                    print("out of range")
                    out_of_range = True
                elif new_x >= len(grid[0]) or new_x < 0:
##                    print("out of range")                    
                    out_of_range = True
                elif grid[new_y][new_x] != ".":
                    empty_los = False

                

                if out_of_range:
                    new_y -= i
                    new_x -= j
                    
                if grid[new_y][new_x] == "L":
                    last_empty = new_y, new_x
                
            try:
                seat = grid[new_y][new_x]
                if seat == ".":
                    seat = grid[last_empty[0]][last_empty[1]]
                yield seat
            except:
                #print(new_y, new_x)
                #input()
                pass



LOG = True
input()


print("Solving example")



results = solve(example_input, param=5)
print("Result is", results[0])


if results[0] == TARGET:
    print("Success, solving puzzle input")
    input()
    results = solve(puzzle_input, param=25)
    print("Result is", results[0])
    

    







