from copy import deepcopy


example = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

with open("day24.txt", "r") as f:
    puzzle = f.read().strip()

TARGET = 10


class Tile:
    def __init__(self):
        self.colour = 1
        self.se = None
        self.sw = None
        self.nw = None
        self.ne = None
        self.w = None
        self.e = None

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, val):
        self.__dict__[key] = val

    def make_neighbours(self):
        self.se = Tile()
        self.sw = Tile()
        self.nw = Tile()
        self.ne = Tile()
        self.w = Tile()
        self.e = Tile()

        return [self.se, self.sw, self.ne, self.nw, self.w, self.e]


def move(d, x, y):

    if d == "e":
        x += 2

    elif d == "w":
        x -= 2

    elif d == "ne":
        y -= 1
        x += 1
    elif d == "se":
        x += 1
        y += 1
    elif d == "nw":
        y -= 1
        x -= 1
    else:
        y += 1
        x -= 1
        

    return x, y


class Floor:

    def __init__(self):

        
        self.grid = [[1 for i in range(300)] for j in range(300)]



        

        self.black = 0
        self.white = 0

        


    def follow_paths(self, data):

        data = data.split("\n")

      
      
        for line in data:

            x, y = 150, 150

            

            line = list(line)

            i = 0

            line_test = ""
            while True:
                char2 = None

                try:
                    char1 = line.pop(0)
                except:
                    break

                try:
                
                    char2 = line.pop(0)
                except:
                    pass
                



                if char2 is None:

                    direction = char1
                elif char1 in "we":
                    line = [char2] + deepcopy(line)
                    direction = char1
                else:
                    direction = char1+char2

                

     
                #print(direction, end=" ")

                x, y = move(direction, x, y)

                line_test += direction

                if char2 is None:
                    break


            print("    end at ", y, x)
            self.grid[y][x] = int(not self.grid[y][x])


        for row in self.grid:
            if all([cell==1 for cell in row]): continue
            for cell in row:
                print(cell if cell == 0 else " ", end="")
            print()
            
        black = sum([row.count(0) for row in self.grid])
        return black


    def get_neighbours(self, y, x):

        for x_adj, y_adj in [[-1, -1], [-1, 1], [2, 0], [-2, 0], [1, -1], [1, 1]]:

            new_x = x + x_adj
            new_y = y + y_adj

            if new_y < 0 or new_x < 0 or new_y > len(self.grid)-1 or new_x > len(self.grid)-1:
                continue

            yield self.grid[new_y][new_x]



    def part2(self):


        for day in range(1, 101):

            
            flipped = deepcopy(self.grid)

            

            for y, row in enumerate(self.grid):

                for x, tile in enumerate(row):

                    n = list(self.get_neighbours(y, x))
                    if tile == 0 and n.count(0) > 2 or n.count(0) == 0:
                        flipped[y][x] = 1
                    elif tile == 1 and  n.count(0) == 2:
                        flipped[y][x] = 0


            print("Day {} : {} black tiles".format(day, sum([row.count(0) for row in flipped])))

            self.grid = deepcopy(flipped)

                    

                    


Floor().follow_paths("wweswwnwseewseswewswswnwnenw")

#ne e sw se e se e e e e se e e e e e e se e e
#ne e sw se e se e e e e se e e e e e e se e e
                    

for data in [example, puzzle]:

    this = Floor()

    
    result = this.follow_paths(data)
    this.part2()
    print("Result is {} black".format(result))
    if result != TARGET:
        break

            

        
