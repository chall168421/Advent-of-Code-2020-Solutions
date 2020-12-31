

f = open("results.txt", "r")

data = f.readlines()
f.close()


buses = list(enumerate(map(int, "1789,37,47,1889".split(","))))

from chinese_remainder import find_chinese_remainder



c = find_chinese_remainder([[buses[0][1], b[1]] for b in buses[1:]],
                           [[b[0], 0] for b in buses[1:]])

                  

results = [30414, 110920, 9225876]



lowest_idx = results.index(min(results))




result_found = False

lowest = results[lowest_idx]

increment = buses[lowest_idx+1][1] *  buses[lowest_idx+1][0]

          

     

     

     

          

          

          

     
