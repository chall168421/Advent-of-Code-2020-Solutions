from itertools import combinations,permutations
import heapq
from copy import deepcopy
import zlib
import json

import re

from numpy import array


def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString



    
TAB = '\t'
NL = '\n'

example_input = '''0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"'''

puzzle_input = """"""


examples = ['''0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"

aab
aba''',
            '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb''']

targets = [2, 2]



with open("day19.txt") as f:
    puzzle_input = f.read()



def reformat_rule(string, substring, replacestring):

    substring = f" {substring} "
    replacestring = f" {replacestring} "
    startstring = f" {string} "
    while substring in startstring:
        startstring = startstring.replace(substring, replacestring)

    return startstring.strip()





def pack_rule(rule):
    if type(rule) == bytes:
        return rule

    c = zlib.compress(rule.encode('utf-8'))
    return c

 

def unpack_rule(rule):
    if type(rule) == str:
        return rule
    
    c= zlib.decompress(rule)

    return c.decode('utf-8')



            

        


def log(*s, end=NL):
    if LOG:
        for i in s:
            i = str(i)[:500]
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


        
def check_resolved(rule):
    log("checkin rule", rule)

    if type(rule) == bytes:
        rule = unpack_rule(rule)

    for term in rule.split():
        
            if term.replace("{", "").replace("}", "") not in ['', 'a', 'b', '|']:
                log("not resolved")

                return False

    log('resolved')
    return True




def solve(data, cap=None):
    answer = None



    
    
    rules, messages = data.split(NL+NL)



    log(rules)


    rules = rules.replace('"a"', 'a').replace('"b"', 'b')
    rules = rules.split(NL)
    rule_map = {}
    resolve_map = {}

    for rule in rules:

        rule_id, rule_def = rule.split(": ")

        resolved = check_resolved(rule_def)
        
        if resolved:
            resolve_map[int(rule_id)] = pack_rule(rule_def)
        else:
            rule_map[int(rule_id)] = pack_rule(rule_def)
        

    global LOG
    RULES = len(rules)
    master_rule = rule_map[0]

    try:
        while len(rule_map):
            print(len(rule_map), "left to resolve")


                        


            rule_count = 0
            rules = list(rule_map.keys())
            while rule_count < len(rule_map):

                rule_id = rules[rule_count]

                    
                for resolve_id, resolve_def in resolve_map.items():
                    log(f"Checking for resolved id {resolve_id}")
                    new_rule = []

                    resolve_def = unpack_rule(resolve_def)
                    rule_def = rule_map[rule_id]
                    rule_def = unpack_rule(rule_def)
                    
                    if " "+str(resolve_id)+" " in " " +rule_def+" ":

                        sections = resolve_def.split(" | ")

                        
                        new_rule = []
                        for i in range(len(sections)):
                            if sections[i].strip() == "":
                                continue
                            new_rule.append(reformat_rule(rule_def, str(resolve_id), sections[i]))
                            

                    if len(new_rule):
                        log("rule modded", rule_id)

                        rule_map[rule_id] = " | ".join(set(new_rule))

                rule_map[rule_id] = pack_rule(rule_map[rule_id])
           
                if check_resolved(rule_map[rule_id]):
                    newly_resolved = rule_map.pop(rule_id)
                    resolve_map[rule_id] = newly_resolved
                    log(rule_id, "now resolved")

                rule_count += 1

    except KeyboardInterrupt:
        return "err", resolve_map

                
    keys = list(resolve_map.keys())
    for key in keys:
        if key != 0:
            del resolve_map[key]

    print(len(resolve_map))
    master_rule = unpack_rule(resolve_map[0]).replace(" ", "")
    return finalise(master_rule, messages)



def finalise(master_rule, messages):

    
    print("removed backets")
    master_rule = set(master_rule.split("|"))
    count = 0
    messages = messages.split(NL)
    for i, msg in enumerate(messages):
        print(len(messages)-i, " to go.")
        if msg.strip() in master_rule: #if re.search(regex_format, msg) is not None:
            print(msg, "matches")
            count += 1
    
    return count, master_rule

given = 2
count = 0

##
##f = open('msg.txt')
##x = f.read()
##length = len(x)
##from numpy import array
##
##sections = array([None] * length)
##print("Created array size", length)
##
##finalise(
##
##
##print("populated array")
##input(len(sections))



LOG = False

for example, target in zip(examples, targets):
    print("Solving example")
    result, data = solve(example, cap=2020)
    print("results")
    print(result)
    print("Target")
    print(target)
    input()
    count += 1 if target==result else 0

count = 2
if count == given:


    print("Success, solving puzzle input")

    result, data = solve(puzzle_input, cap=30000000)
    print("Result is", result)










