from copy import deepcopy
from random import shuffle, randint, randrange, choice

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

    def __repr__(self):
        
        return "I am {} : <{} ^{} v{} {}>".format(self.id, self.left, self.top, self.bottom, self.right)

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
            flipped.bottom = int("".join(reversed(bin(self.bottom)[2:].zfill(10))), 2)
        else:
            flipped.left = int("".join(reversed(bin(self.left)[2:].zfill(10))), 2)
            flipped.right = int("".join(reversed(bin(self.right )[2:].zfill(10))), 2)
            flipped.top = self.bottom
            flipped.bottom = self.top

            
        return flipped
        
        


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

        print(t)
        


 

    # make a grid of size 3 x 3

    starting_grid = [[Tile() for i in range(3)] for j in range(3)]

    update_tree = []

    chosen_tile = choice(list(tiles.keys()))

    first = tiles['1427'].flip(1)

    starting_grid[1][1] = first


    used = [first.id]

    updates = []

    

    # grid must always have perimeter free
    while not walk_grid(deepcopy(tiles), [], starting_grid):

        starting_grid = [[Tile() for i in range(3)] for j in range(3)]
        chosen_tile = choice(list(tiles.keys()))



        starting_grid[1][1] = first
        
        print("try again!")

def walk_grid(tiles, updates, grid=None):

    global LOG

    if grid is None:       grid = [[Tile() for i in range(3)] for j in range(3)]

    

    
    

    # until solved
    solved = False

    tile_key_list = list(tiles.keys())

    variant_max = 12

    count = 0

    while not solved:

        count += 1


    

        

        possibilities = []

        # for each grid cell

        
        no_poss = True
        for y, row in enumerate(grid):
            for x, cell in enumerate(grid):
         
                neighbours = get_neighbours(grid, y, x)
                possibilities = []
                if neighbours is None:
                    #print("no neighbours at {} {}".format(y, x))
                    pass

                else:
                   

                    for variant in range(variant_max):
             
                        for tile_key in tile_key_list:
                            t = deepcopy(tiles[tile_key])

                            if variant in [4, 5, 6, 7]:
                                t = t.flip(0)
                            elif variant in [8, 9, 10, 11]:
                                t = t.flip(1)
                            if variant in [1, 5, 9]:
                                t = t.rotate(1)
                            elif variant in [2, 6, 10]:
                                t = t.rotate(2)
                            elif variant in [3, 7, 11]:
                                t = t.rotate(3)
                                
                      
                            
                            s = check_tesselate(neighbours, t)
                            
                            log("strength", s)
                            if s != 0:
                                possibilities.append([s, t, y, x])

                    if len(possibilities):
                        no_poss = False
                        #input("{} {} has {} poss".format(y, x, len(possibilities)))


                            

                                        

                 


            
                    

                        
                        shuffle(possibilities)
                        s, new_tile, y, x = sorted(possibilities, key=lambda x: x[0], reverse=True)[0]


                        grid[y][x] = new_tile

                        updates.append([y, x])
                        tile_key_list.remove(new_tile.id)

                        if len(tile_key_list) == 2:
                            input()
                        if len(tile_key_list) == 0:
                            print_grid(grid)
                            return True

                       

                        

                        


                        if y == len(grid)-1 or x == len(grid)-1 or x == 0 or y == 0:

                            length = len(grid) + 2
                            
                            new_grid = [[Tile() for i in range(length)]]

                            
                            for row in grid:
                                new_grid.append([Tile()] + deepcopy(row) + [Tile()])
                                

                            new_grid.append([Tile() for i in range(length)])


                            grid = new_grid
                            
                        print_grid(grid)

        if no_poss:

            #try to flip single connected vertices

            flippy = False

            while not flippy:
                
                y = randint(0, len(grid)-2)
                x = randint(0, len(grid)-2)
                print("flip {} {}?".format(y, x))
                if grid[y-1][x].bottom == None or y-1 < 0:
                    if grid[y+1][x].top == None or y+1 >= len(grid):
                        grid[y][x] = grid[y][x].flip(1)
                        flippy = True

                if grid[y][x-1].right == None or x-1 < 0:
                    if grid[y][x+1].left == None or x+1 >= len(grid):
                        grid[y][x] = grid[y][x].flip(0)
                        flippy = True

            print("flippy")
            print_grid(grid)
                        
            return False


     

                        
                            

                
                    

                # check agreed positions

            # record variants

            # go for position 1 but save options in state tree

            # keep perimeter space free

            # if dead end, resume at last branch split

            # record dead leaves

                


    

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
            



            

                
                
            
    
        

data = solve(test_data)     
            
            
