from re import finditer
from collections import OrderedDict

##########################################################
### ADVENT OF CODE 2020 - DAY 18 - c.hall - 18/12/2020 ###
##########################################################
    
TAB = '\t'
NL = '\n'

with open("day18.txt", "r") as f:
    puzzle_input = [line.strip() for line in f.readlines()]


def log(*s, end=NL):
    if LOG:
        for i in s:
            print(i, end=" ")
        print(end, end="")


def my_eval(expression):
    result = None
    op = None
    n = ""
    expression = expression.split()
    for part in expression:

        if part in "+-":
            op = part
        else:
            part = part.replace("(", "").replace(")", "")
            if op is None:
                result = int(part)
            else:
                calc = "{} {} {}".format(result, op, part)
                result = eval(calc)

    return str(result)


def my_eval2(expression):

    expression = " " + expression # hacky fix to stop 15 + 5 evaluating as 1(5+5) etc.
    expression = expression.replace("(", "").replace(")", "")

    while "+" in expression:    
        add_exps = list(m.group(0) for m in finditer(r"\d+\s\+\s\d+", expression))
        for exp in add_exps:
            expression = expression.replace(" "+exp, " "+str(eval(exp)), 1)


    return str(eval(expression))


def solve(data):
    total = 0

    if type(data) == str:
        data = data.split(NL)

    for line in data:        

        for pass_ in range(2):
            inner_exps = []

            for sub_exp in [m.group(0) for m in finditer(r"\((\d|\+|\-|\*|\/|\s)*\)", line)]:
                if "+" in sub_exp: # should bracketed expressions containing only * have less precedence? don't think this matters but do it anyway.
                    inner_exps.insert(0, [sub_exp, None])
                else:
                    inner_exps.append([sub_exp, None])

            inner_exps = OrderedDict({i:my_eval2(i) for (i, j) in inner_exps})
            
   
            for i_exp, i_res in inner_exps.items():
                line = line.replace(i_exp, i_res)
    
        final_eval = int(my_eval2(line))
        total +=  final_eval


    return total, [inner_exps, line]



LOG = False


examples = '''1 + (2 * 3) + (4 * (5 + 6)) becomes 51.
2 * 3 + (4 * 5) becomes 46.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.'''


count = 1
examples = [[line.split(" becomes ")[0], int(line.split(" becomes ")[1][:-1])]  for line in examples.split(NL)]

for example, target in examples:

    result, data = solve(example)
    print("Result:", result, "Target:", target)
    if result == target:
        print("success!")
        count += 1
        

if count == 6:

    print("Success, solving puzzle input")
    result, data = solve(puzzle_input)
    print("Result is", result)










