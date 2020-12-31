from copy import deepcopy
from random import shuffle, randint, randrange

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

def check_for_next_row(tiles, complete_rows):
    

    match = check_for_first_row(tiles)
    if match == -1:
        return -1, -1


    print(tiles[match])
    input()

    for i in range(match, match+num_tiles_surrounded+1):
        t = tiles[i]
        print("<{} ^{} v{} {}>".format(t["borders"]["L"], t["borders"]["T"], t["borders"]["B"], t["borders"]["R"]), end="|")

    print()
    for row in complete_rows:
        
        for t in row:
            print("<{} ^{} v{} {}>".format(t["borders"]["L"], t["borders"]["T"], t["borders"]["B"], t["borders"]["R"]), end="|")
        print()

    
    input("I found a row, can it match rows already got?")

    new_complete_row = [tiles[t] for t in range(match, match+num_tiles_surrounded)]

    for row_pos, check1, check2 in zip([0, len(complete_rows)-1], ["B", "T"], ["T", "B"]):
        check_row = complete_rows[row_pos]        
        for this_tile, that_tile in zip(new_complete_row, check_row):
            if this_tile["borders"][check1] != that_tile["borders"][check2]:
                return -1, -1
       
        else:
            input("valid row found starting from", i, "to match already complete row", row_pos)
            return match, row_pos
    

            
        
    
        


def check_for_first_row(tiles):

 
    
    # tile1   l 10 t 9 r 4 b 5
    # tile2   l 4 t ? r 9 b ?
    # tile3   l 9 t ? r 7 b ?

    print("I have", len(tiles), "to check")


    print(num_tiles_surrounded, "is the row length")
    for i in range(len(tiles[:-num_tiles_surrounded])):
        for j in range(num_tiles_surrounded):

            this_tile = tiles[i]
            next_tile = tiles[i+1]

            if this_tile["borders"]["R"] != next_tile["borders"]["L"]:
                break
        else:
            print("valid row found starting from", i)
            return i

    return -1


def randomise_tiles(tiles):

    new_tiles = deepcopy(tiles)

    end = len(tiles)

    for i in range(len(tiles)):

        move_tile = new_tiles.pop(i)
        

        if randint(0, 3) == 0:
            # flip
            x, y = ("L", "R") if randint(0, 1) else ("T", "B")
            print("Flipped", end=" ")
            temp = move_tile["borders"][x]
            move_tile["borders"][x] = move_tile["borders"][y]
            move_tile["borders"][y] = temp
                
            
        else:
            for j in range(randint(1, 3)):
                print("Rotated", end=" ")
                temp = move_tile["borders"]["L"]
                move_tile["borders"]["L"] = move_tile["borders"]["T"]
                move_tile["borders"]["T"] = move_tile["borders"]["R"]
                move_tile["borders"]["R"] = move_tile["borders"]["B"]
                move_tile["borders"]["B"] = temp

                
        new_pos = randrange(0, len(new_tiles))

        print("tile {} and moved it to {}".format(i, new_pos))
        new_tiles.insert(new_pos, move_tile)

                         
    return new_tiles
        

    

        

        


def solve(data):

    data = data.replace("#", "1").replace(".", "0")

    tiles = []
    tile = ""
    for line in data.split("\n"):
        

        if line.strip() == "":
            continue

        if "Tile" in line:


                

            tile = {"id":"".join([t for t in line if t.isdigit()]), "img":[]}
            tiles.append(tile)

            continue

        else:
            tiles[-1]["img"].append(line)


    for i, tile in enumerate(tiles):
        img = tile["img"]
        borders = {}
        borders["T"] = (int(img[0], 2))
        borders["B"] = (int(img[9], 2))
        borders["L"] = (int("".join(row[0] for row in img), 2))
        borders["R"] = (int("".join(row[-1] for row in img), 2))
        tiles[i]["borders"] = borders


    global num_tiles_surrounded
    num_tiles_surrounded = int(sqrt(len(tiles)))
    num_tiles_surrounded -= num_tiles_surrounded % 2

    first_row_found = False
    while not first_row_found:
        tiles = randomise_tiles(tiles)
        match = check_for_first_row(tiles)
        if match != -1:
            first_row_found = True

        
    print("Found first row")
    input()
    complete_rows = [list()]
    for t in range(match, match+num_tiles_surrounded+1):
        complete_rows[0].append(tiles.pop(t))

    print(tiles)
    input()

    while len(complete_rows) != num_tiles_surrounded + 1:

        next_row_found = False
        while not next_row_found:

            tiles = randomise_tiles(tiles)

            match, row_index = check_for_next_row(tiles, complete_rows)

            if match != -1:
                next_row_found = True
        input("Found next row!")


        new_row = []
        for t in range(match, match+num_tiles_surrounded):
            new_row.append(tiles.pop(t))

        
        complete_rows.insert(row_index, new_row)

        

        

        
        

        

solve(test_data)     
            
            
