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

example_input = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''



with open("day14.txt") as f:
    puzzle_input = f.read()

example_input = example_input.split(NL)
puzzle_input = puzzle_input.split(NL)

TARGET = 208


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


def get_variations(mask):


    floats = mask.count("f")


    


    combinations = [bin(i)[2:].zfill(floats) for i in range(2**floats)]

        

    return combinations
            

    
            

                
        
            


def solve(data, param):

    data_new = []
    for line in data:
        if line.startswith("mask"):
            data_new.append([line[7:], []])
        else:
            value = int(line.split(" ")[-1])
            register = line.split("[")
            register = register[1].split("]")[0]
            
            data_new[-1][1].append([register, value])


    memory = {}

    for ins in data_new:

        mask = ins[0]

        mem_changes = ins[1]


        for register, value in mem_changes:

            val = value

            
            
            register = bin(int(register))[2:].zfill(36)

            log("going to write")
            log(val)
            log("to memory address")
            log(register)
            log("using mask")
            log(mask)

            master_mask = ""
            float_count = 0
            for b, m in zip(register, mask):

                if m == '0':
                    master_mask += b
                elif m == '1':
                    master_mask += '1'
                else:
                    master_mask += 'f'
                    

            log("master mask")
            log(master_mask)

            
            variants = set(get_variations(master_mask))

            log("variants")
            for v in variants:
                log(v)
            
            for v in variants:                

                this_variant = list(v)

                this_add = ""
                
                for reg_bit, mask_bit in zip(register, master_mask):

                    if mask_bit == "f":
                        this_add += this_variant.pop(0)
                    else:
                        this_add += mask_bit

                    

                log(this_add)
              
                log("result")

                this_add = int(this_add, 2)

                log("writing to", this_add)

                memory[this_add] = val

            

    return sum(memory.values()), memory
        


    
    
    
def solve2(data, target=10884537):    
    return result, data
    


    



LOG = False

puzzle_input.remove("")
print("Solving example")
results = solve(example_input, param=5)
print("Result is", results[0])
if results[0] == TARGET:
    print("Success, solving puzzle input")

    results = solve(puzzle_input, param=25)
    print("Result is", results[0])
    

    







