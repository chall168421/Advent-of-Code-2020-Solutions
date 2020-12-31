import timeit
import re

    
TAB = '\t'
NL = '\n'

example_input = list('''389125467''')
puzzle_input = list('789465123')


TARGET = 149245887792


def log(*s, end=NL):
    if LOG:
        for i in s:
            print(i, end=" ")
        print(end, end="")


class Node:
    def __init__(self):
        self.n = 0
        self.next = None

class CircularQueue:

    def __init__(self, items):


        self.head = Node
        self.max = max(items)
        self.min = min(items)
        self.create_cups(items)
        

    def create_cups(self, items):
        
        current = self.head
        
        for i in items[:-1]:
            current.n = i
            new = Node()
            current.next = new
            current = new

        current.n = items[-1]
        current.next = self.head


    def traverse(self):

        current = self.head
        #log(f"({current.n})", end=", ")
        current = current.next

        while current != self.head:
            log(current.n, end=", ")
            current = current.next
        #log()

    def final_result(self):
        current = self.start
        while current.n != 1:
            current = current.next

        one_node = current
        current = current.next
        final = ""
        while current != one_node:
            final += str(current.n)
            current = current.next
        return final

    def part_b_final_result(self):
        current = self.start
        while current.n != 1:
            current = current.next

        return current.next.n * current.next.next.n
            

    def find_destination(self):

        target = self.head.n - 1

        if target < self.min:
                target = self.max

        while target in self.pickup_nums:
            
            target -= 1
            if target < self.min:   
                target = self.max

        current = self.start

        while current.n != target:          
            current = current.next

        self.destination = current
        #log("Destination: ", self.destination.n)

    def pick_up_three(self):

        self.pickup = []

        current = self.head.next

        self.pickup_nums = [current.n, current.next.n, current.next.next.n]
        self.pickup = current        

        last = current.next.next.next
        self.head.next = last

        #log("pick up :", self.pickup_nums)
        self.start = last

    def place_three(self):
        old_link = self.destination.next
        self.destination.next = self.pickup
        self.pickup.next.next.next = old_link

        
        

    def update_current(self):
        self.head = self.head.next
    
            
            



def solve(data):

    data = list(map(int, list(data)))


    



    cups = CircularQueue(data)
    for move in range(FINAL):
        log("-- move {} --".format(move+1))
        cups.pick_up_three()
        cups.find_destination()
        cups.place_three()
        cups.update_current()


    return cups.final_result(), cups


    



    
def solve2(data):    

    data = list(map(int, list(data)))

    data += list(range(max(data)+1, 1000001))

    cups = CircularQueue(data)

    timer = None
    
    for move in range(FINAL):
        if move % 1000 == 0:
            print("-- move {} --".format(move+1))
            if timer is not None:
                print("That took", timeit.default_timer()-timer, "seconds")
            timer = timeit.default_timer()
        cups.pick_up_three()
        cups.find_destination()
        cups.place_three()
        cups.update_current()


    return cups.part_b_final_result(), cups

    


FINAL = 10000000

PARTB = False



LOG = True



results, data = solve2(example_input)
print("Example test results", results)

if results == TARGET:
    print("Success, solving puzzle input")
    #input()
    results, data = solve2(puzzle_input)
    print("Result is", results)










