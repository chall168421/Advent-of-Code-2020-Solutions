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

class Tile:

    def __init__(self):
        self.id = ""
        self.left = ""
        self.right = ""
        self.top = ""
        self.bottom = ""

    def __repr__(self):
        return self.id

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
            flipped.top = self.top
            flipped.bottom = self.bottom
        else:
            flipped.left = self.left
            flipped.right = self.right
            flipped.top = self.bottom
            flipped.bottom = self.top

            
        return flipped
        
        


with open("day20.txt") as f:
    puzzle_input = f.read()

def print_tile(t):
    print("<{} ^{} v{} {}>".format(t.left, t.top, t.bottom, t.right))



                

                    

                

                    


 

def print_row(row):

    top = ""
    mid = ""
    bot = ""

    for t in row:

        top += "{:^15}".format(t.top)
        mid += "{:^5}{:^5}{:^5}".format(t.left, t.id, t.right)

        bot += "{:^15}".format(t.bottom)
    
    print(top)
    print(mid)
    print(bot)

def find_all_rows(tiles, row_length):

    end = []

    row = []

    possibilities = []
    attempt_counter = 0

    while True:

        

    
        start = choice(tiles)

        row = (start, )

        b, L, R, T, B = "borders", "left", "right", "top", "bottom"
        



        other_tiles = [t for t in tiles if t != start]



        MAX = len(tiles) * len(tiles) * 6
        for attempt in other_tiles:

            
            
            
            attempt_counter += 1
            if attempt_counter > MAX:
                print("reset")
                row = (choice(tiles), )
                attempt_counter = 0
                print("Abandon attempt")
                possibilities = []
                tiles = deepcopy(tiles)

                shuffle(tiles)
                continue
    
   

            if row[0].left == attempt.right:

                row = (attempt, *row)
                continue

            elif row[-1].right == attempt.left:

                row = (*row, attempt)
                continue

            for r in range(1, 4):

                if row[0].left == attempt.rotate(r).right:
                    log("Needed to rotate tile {} {} times".format(attempt.id, r))
                    row = (attempt.rotate(r), *row)
                    break

                elif row[-1].right == attempt.rotate(r).left:
                    log("Needed to rotate tile {} {} times".format(attempt.id, r))
                    row = (*row, attempt.rotate(r))
                    break

            else:
                if row[0].left == attempt.flip(0).right:
                    log("Needed to flip tile {} horizontally".format(attempt.id, r))
                    row = (attempt.flip(0), *row)
                    continue

                elif row[-1].right == attempt.flip(0).left:
                    log("Needed to flip tile {} horizontally".format(attempt.id, r))
                    row = (*row, attempt.flip(0))
                    continue

        if len(row) == row_length:
            tile_format = "\t".join([t.id for t in row])
            if tile_format not in possibilities:
                possibilities.append(tile_format)
                print(tile_format)


            if len(possibilities) == 3:
                input()
                
                


def solve(data):

    data = data.replace("#", "1").replace(".", "0")

    tiles = []
    tile = ""
    for line in data.split("\n"):
        

        if line.strip() == "":
            continue

        if "Tile" in line:
                

            tile = Tile()
            tile.id = "".join([t for t in line if t.isdigit()])
            tile.img = []
            tiles.append(tile)

            continue

        else:
            tiles[-1].img.append(line)


    for i, t in enumerate(tiles):
        img = t.img
        borders = {}
        t.top = (int(img[0], 2))
        t.bottom = (int(img[9], 2))
        t.left = (int("".join(row[0] for row in img), 2))
        t.right = (int("".join(row[-1] for row in img), 2))
 

    
    global num_tiles_surrounded
    num_tiles_surrounded = int(sqrt(len(tiles)))
    num_tiles_surrounded -= num_tiles_surrounded % 2


    find_all_rows(tiles, num_tiles_surrounded+1)

 

                        ## rotate accordingly and insert into tile map at correct pos

                


    
   

        

data = solve(test_data)     
            
            
