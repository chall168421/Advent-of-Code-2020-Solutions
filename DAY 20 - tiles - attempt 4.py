from copy import deepcopy
from random import shuffle, randint, randrange, choice
from collections import Counter

LOG = False

def log(*s, end=""):
    if LOG:
        
        for i in s:
            print(i, end=end)

        print()

test_data = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###

.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""


tiles = {}


from random import shuffle
from math import sqrt

def flip(num):

    return int("".join(reversed(bin(num)[2:].zfill(10))), 2)

class Tile:

    def __init__(self):
        self.id = ""
        self.left = None
        self.right = None
        self.top =  None
        self.bottom = None
        self.similarities = Counter()

    def __repr__(self):
        
        x = "I am {} : <{} ^{} v{} {}>".format(self.id, self.left, self.top, self.bottom, self.right)
        f1 = self.flip(0)
        f2 = self.flip(1)
        x += " flips: <{} ^{} v{} {}>".format(f2.left, f1.top, f1.bottom, f2.right)
        return x

    def __getitem__(self, key):
        
        return self.__dict__[key]

    def rotate(self, rotations):
        r = deepcopy(self)
        for i in range(rotations):
            rotated = Tile()
            rotated.id = r.id
            rotated.left = r.top
            rotated.top = r.right
            rotated.right = r.bottom
            rotated.bottom = r.left
            r = rotated
        return rotated

    def flip(self, mode=0):
        flipped = Tile()
        flipped.id = self.id
        if mode == 0:
            flipped.left = self.right
            flipped.right = self.left
            flipped.top = int("".join(reversed(bin(self.top)[2:].zfill(10))), 2)
            self.flipped_top = flipped.top
            flipped.bottom = int("".join(reversed(bin(self.bottom)[2:].zfill(10))), 2)
            self.flipped_bottom = flipped.bottom
        else:

            flipped.left = int("".join(reversed(bin(self.left)[2:].zfill(10))), 2)
            flipped.right = int("".join(reversed(bin(self.right )[2:].zfill(10))), 2)
            flipped.top = self.bottom
            flipped.bottom = self.top
            self.flipped_left = flipped.left
            self.flipped_right = flipped.right

        
        return flipped

    def get_all_edges(self):

        return [self.left, self.top, self.right, self.bottom, self.flipped_left, self.flipped_right, self.flipped_top, self.flipped_bottom]
        
        


with open("day20.txt") as f:
    puzzle_input = f.read()

def print_tile(t):
    pass



                

                    

                

                    

def print_grid(grid):
    for row in grid:
        print_row(row)
 

def print_row(row):

    top = ""
    mid = ""
    bot = ""

    for t in row:
        
        
        above = "" if t.top is None else t.top
        left = "" if t.left is None else t.left
        right = "" if t.right is None else t.right
        below = "" if t.bottom is None else t.bottom


        top += "{:^15}".format(above)
        mid += "{:^5}{:^5}{:^5}".format(left, t.id, right)
        bot += "{:^15}".format(below)
    
    print(top)
    print(mid)
    print(bot)


def get_neighbours(grid, y, x):
    MAX = len(grid) - 1
    n = Tile()
    if y > 0:
        n.top = grid[y-1][x].bottom
    if y < MAX:
        n.bottom = grid[y+1][x].top

    if x > 0:
        n.left = grid[y][x-1].right
    if x < MAX:
        n.right = grid[y][x+1].left

    return n if any([n.left, n.right, n.top, n.bottom]) else None
            


def check_tesselate(n, t):
    strength = 0

 

    for side in "left,right,top,bottom".split(","):

        if t[side] == n[side] or n[side] == None:
            strength += 1

        elif n[side] is not None and n[side] != t[side]:
            log(""" Strength is 0

I am {}
Left {}
Right {}
Top {}
Bottom {}""".format(t, n.left, n.right, n.top, n.bottom))
            strength = 0
            break


            


    return strength
        
        
    

    
    

            

def solve(data):

    data = data.replace("#", "1").replace(".", "0")

    tiles = {}
    tile = ""
    for line in data.split("\n"):
        

        if line.strip() == "":
            continue

        if "Tile" in line:
                

            tile = Tile()
            tile.id = "".join([t for t in line if t.isdigit()])
            tile.img = []
            tiles[tile.id] = tile

            continue

        else:
            tiles[tile.id].img.append(line)


    for id_, t in tiles.items():
        img = t.img
        borders = {}
        t.top = (int(img[0], 2))
        t.bottom = (int(img[9], 2))
        t.left = (int("".join(row[0] for row in img), 2))
        t.right = (int("".join(row[-1] for row in img), 2))

        t.flip(0)
        t.flip(1)





    for tile in tiles.values():
        for other_tile in tiles.values():
            if tile == other_tile:  continue


            other_edges = other_tile.get_all_edges()
            count = 0 

            for side in "left,right,top,bottom,flipped_left,flipped_right,flipped_top,flipped_bottom".split(","):
                count += other_edges.count(tile[side])
                tile.similarities[other_tile.id] += count

    print("EDGES")
    final = Counter({t.id:sum(t.similarities.values()) for t in tiles.values()})

    print(final.most_common()[-4:])
    return final


                
        


 

    



        




     

                        
                            

                


    

def exemplar():

    d = """#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##....."""

    d = d.replace("#", "1").replace(".", "0")

    ids = """1951    2311    3079    2729    1427    2473    2971    1489    1171""".split("    ")
    grid = []
    for row in d.split("\n\n"):
        this_row = [Tile(), Tile(), Tile()]
        for t in this_row:
            t.left = ""
            t.right = ""
        for i, subrow in enumerate(row.split("\n")):

            
        
            for j,tile in enumerate(subrow.split(" ")):
                
                
                this_row[j].left += tile[0]
                this_row[j].right += tile[-1]

                if i == 0:

                    this_row[j].top = int(tile, 2)

                elif i == 9:
                    this_row[j].bottom = int(tile, 2)

                    this_row[j].left = int(this_row[j].left, 2)
                    this_row[j].right = int(this_row[j].right, 2)

        for t in this_row:
            print(ids)
            t.id = ids.pop(0)
        grid.append(this_row)


    print_grid(grid)




                


exemplar()
            



            

                
                
            
    
        

data = solve(puzzle_input)     
            
            
