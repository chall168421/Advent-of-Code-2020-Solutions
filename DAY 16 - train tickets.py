from itertools import combinations, permutations
import heapq

from random import choice

import re

from collections import OrderedDict

def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString

    
TAB = '\t'
NL = '\n'

ex2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

example_input = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''

puzzle_input = """"""

TARGET = 71



with open("day16.txt") as f:
    puzzle_input = f.read()

example_input = example_input.split(NL)
puzzle_input = puzzle_input.split(NL)
ex2 = ex2.split(NL)

examples = [example_input, ex2]
targets = [TARGET, None]


def sudoku(d):
    
    print("{:<20}".format("X"), end=" ")
    for i in range(20):

        print("{:<4}".format(i), end= " ")

    print()

    for f, j in d.items():

        print("{:<20}".format(f), end=" ")
        for i in range(20):
            if i in j:
                print("{:<4}".format(i), end= " ")
            else:
                print("{:<4}".format(" "), end= " ")
        print()

        



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


        
def solve(data, cap):

    result = None

    details = {}

    tickets = {} 
    
    stuff = ""
    ticket = False
    nearby = False
    for line in data:
        
        if ticket:
            ticket = False
            tickets["your ticket"] = list(map(int, line.split(",")))

        if nearby:            
            try:
                tickets["nearby"].append(list(map(int, line.split(","))))
            except:
                tickets["nearby"] = [list(map(int, line.split(",")))]


        if "your ticket" in line:
            ticket = True
            continue

        elif "nearby" in line:
            nearby = True
            continue


        
        if ":" in line:
            x, y = line.split(":")

            details[x] = y.split(" or ")

    print(len(tickets["nearby"]), 'nearby tyickets remain')
    input()
    invalid = []
    for ticket in tickets["nearby"]:
        #print(ticket)
        ticket_valid = True
        for t in ticket:
            valid = False
            #print("t is", t)
            for field, params in details.items():                
              
                for p in params:

                    mini, maxi = p.split("-")
                    #print(t, mini, maxi, field)
                    if int(t) >= int(mini) and int(t) <= int(maxi):
                        valid = True
                        continue

            if not valid:
                ticket_valid = False
                invalid.append(t)

        if not ticket_valid:
            tickets["nearby"].remove(ticket)
            print(invalid)



    print(len(tickets["nearby"]), 'nearby tyickets remain')
    input()
    return sum(invalid), details, tickets


def solve2(details, tickets):
    
    
    field_map = {f:{"valid":set(), "range":v} for f, v in details.items()}

    valid_map = OrderedDict({f:[] for f in details.keys()})
    

    print(len(tickets["nearby"]), 'nearby tyickets remain')
    input()

    all_tickets = list([tickets["your ticket"]])


    all_tickets.extend(tickets["nearby"])
   
    
    
    field_list = list(field_map.keys())
    print(field_list)
    
    #print(field_list)
    ## loop through each field
    i = 0
    
    while i < len(field_list):

        
        
        field = str(field_list[i])
        lo1, hi1 = map(int, field_map[field]["range"][0].split("-"))
        lo2, hi2 = map(int, field_map[field]["range"][1].split("-"))
        

        print("field", field_list[i])

        ## loop through column
        for column in range(len(tickets["nearby"][0])):


            column_valid_for_field = True

            
        

            for ticket in all_tickets: ## loop through each ticket
                
               
                t = int(ticket[column])               
                            
                if not ((t >= lo1 and t <= hi1) or (t >= lo2 and t <= hi2)):

                    column_valid_for_field = False
                    
            

            if column_valid_for_field:
                log("column", column, "VALID for field", field_list[i])
                if LOG:
                    input()
                #print(field_list[i])
                valid_map[field].append(column)
                print(valid_map)
                input("change to valid map")

        i += 1

    print("finished loop")

    log(valid_map)




    chosen_field = choice(list(valid_map.keys()))
    log("Chose", chosen_field)

    all_poss = set()
    [all_poss.update(v) for v in valid_map.values()]

    log("possibilities are", all_poss)





    print(valid_map)
            
    final_valid_map = {k:list(v) for k, v in valid_map.items()}

    [final_valid_map.pop(key) for key in valid_map.keys() if not key.startswith("departure")]

    
    

    print(final_valid_map)

    


    sudoku(final_valid_map)

    input("help")

    
    ## match columns to tickets

    my_ticket = list(map(int, ['157', '73', '79', '191', '113', '59', '109', '61', '103', '101', '67', '193', '97', '179', '107', '89', '53', '71', '181', '83']))

    final_ticket = {k:None for k in my_ticket}


    final_poss = []

    while True:
        this_poss = []
        

        while len(this_poss) < 6:
            
            
            for key, possibilities in final_valid_map.items():
            
            
                removed = possibilities.pop(0)

                if removed not in this_poss and len(this_poss) < 6:
                    this_poss.append(removed)
            
            
                possibilities.append(removed)
                
            
            
        
        
        print(this_poss)
                    
        final_poss.append(this_poss)

        if final_poss.count(final_poss[-1]) > 1:
            break
        
                    



    ## go through unknown columns, check values against ranges
            
    



    
    

        
        

        

            
            
    

  

        
        
LOG = False

d = OrderedDict([('departure location', {6, 7, 10, 13, 16, 17}), ('departure station', {16, 10, 6, 7}), ('departure platform', {4, 6, 7, 10, 13, 16, 17}), ('departure track', {1, 4, 6, 7, 10, 13, 16, 17}), ('departure date', {4, 6, 7, 10, 13, 16, 17}), ('departure time', {6, 7, 10, 16, 17}), ('arrival location', {7}), ('arrival station', {1, 4, 6, 7, 10, 13, 16, 17}), ('arrival platform', {0, 1, 4, 6, 7, 10, 11, 13, 16, 17}), ('arrival track', {10, 6, 7}), ('class', {0, 1, 4, 6, 7, 10, 13, 16, 17}), ('duration', {10, 6, 7}), ('price', {7}), ('route', {16, 10, 6, 7}), ('row', {0, 1, 4, 6, 7, 10, 13, 16, 17}), ('seat', {10, 6, 7}), ('train', {10, 6, 7}), ('type', {6, 7}), ('wagon', {1, 4, 6, 7, 10, 13, 16, 17}), ('zone', {0, 1, 4, 6, 7, 10, 11, 12, 13, 16, 17})])

sudoku(d)

    

    


##print("Solving example")
##results, details, tickets = solve(ex2, cap=2020)
##print("results")
##print(results)
##print("Target")
##print(TARGET)
##print("task 2")
##result = solve2(details, tickets)
##print(results)


    

print("Success, solving puzzle input")

results, details, tickets = solve(puzzle_input, cap=30000000)
result = solve2(details, tickets)
print("Result is", result)










