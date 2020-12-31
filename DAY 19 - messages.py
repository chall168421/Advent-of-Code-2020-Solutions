from itertools import combinations, permutations
import heapq
from copy import deepcopy

import re

from numpy import array


def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString


class MyList(array):

    def replace(self, substring, replace_string):
        new = deepcopy(self)
        for i, item in enumerate(self):

            new[i] = replace_string if item == substring else item

        return " ".join(new)

    def split(self, delim=" "):

      

        components = [[]]
        for i, item in enumerate(self):
            if item == delim or item == " ":
                components.append([])
            else:
                components[-1] += [item]



        #input("problem?")

        return [" ".join(c) for c in components]
             

    
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


        
            


def solve(data, cap=None):
    answer = None



    
    
    rules, messages = data.split(NL+NL)


    

    print(rules)


    rules = rules.split(NL)

    
    rules = {rule.split(": ")[0]:MyList(rule.split(": ")[1].split()) for rule in rules}
    

    RULES = len(rules)
    master_rule = rules["0"]



    
    try:

        resolved = {r:j for r, j in rules.items() if re.match('\"[a-z]\"', " ".join(j))}

        still_to_resolve = True
        rules_copy = deepcopy(rules)
        
        while still_to_resolve:
            still_to_resolve = False



            log("resolved", resolved)
            alter = False
            
            for rule_num, rule in rules.items():

              
                

                #log("checking rule", rule_num, ":", rule)
                    
                


                
                for sub_rule_num, sub_rule in resolved.items():
                    expand_rule = []
                    #log("Checking for ", sub_rule_num)
                    if sub_rule_num in rule:
                        alter = True
                        #log("found!")
                        for sub_rule_poss in sub_rule.split("|"):                                                

                            expand_rule.append(rule.replace(sub_rule_num, sub_rule_poss))

                     

                        
                        rule = " | ".join(expand_rule)
                        rule = MyList(rule.split(" "))           
                        #log("new rule: ", rule)
            
                    #log("Not found")

                    

                    rules_copy[rule_num] = deepcopy(rule)

                if rules == rules_copy:
           
                    print("no change")

                if rule_num in resolved:
                    rules_copy.pop(rule_num)

            
                rules = deepcopy(rules_copy)

                if any([r.isdigit() for r in rule]):
                    still_to_resolve = True
                else:
                    resolved.update({rule_num:rule})
                    print("{} still to resolve".format(RULES - len(resolved)))
                    continue

            
                  
    except KeyboardInterrupt:

        return 0, [resolved, rules_copy]

                

   

    

    master_rule = " ".join(rules["0"])
    regex_format = ""
    open_bracket = False
    for i, char in enumerate(master_rule):
        if char == '"':
            if not open_bracket:
                open_bracket = True
                regex_format += "["
            else:
                open_bracket = False
                regex_format += "]"
        else:
            regex_format += char


    regex_format = r"^(" + regex_format.replace(" ", "") + ")$"


    count = 0

    for msg in messages.split(NL):
        if re.search(regex_format, msg) is not None:
            print(msg, "matches", regex_format)
            count += 1

        

        
    
    
    return count, regex_format

given = 2
count = 0

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










