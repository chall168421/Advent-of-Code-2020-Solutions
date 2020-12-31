from collections import Counter


with open('day21.txt') as f:

    data = f.read()


##
##data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
##trh fvjkl sbzzf mxmxvkd (contains dairy)
##sqjhc fvjkl (contains soy)
##sqjhc mxmxvkd sbzzf (contains fish)"""
##

data = data.strip().split("\n")

all_allergens = Counter()

allergen_map = {}

all_ingredients = []


for line in data:


    ingredients, allergens = line.split(" (contains ")

    if len(allergens) == 0:
        input("help")

    for allergen in allergens[:-1].split(", "):
        ing =  ingredients.split(" ")
        all_ingredients.extend(list(ing))

        all_allergens.update([allergen])
        if allergen in allergen_map:
            allergen_map[allergen].update(ing)
        else:
            allergen_map[allergen] = Counter(ing)



sorted_allergens = sorted(list([k, v] for k, v in allergen_map.items()), key=lambda x: x[1].most_common()[0])



final_choices = {}
for s in sorted_allergens:
    allergen, ing = s
    print("should be", all_allergens[allergen])
    print(allergen, ing)
    input()
    final_choices[allergen] = [k for k, v in ing.items() if v == max(ing.values())]



while any([len(v) > 1 for v in final_choices.values()]):

    for allergen, ings in final_choices.items():

        print("looking at ", allergen, "should appear", all_allergens[allergen], "times")
        print(ings)
        input()

        if len(ings) == 1:
           
            rem = ings[0]
            print(f"This means {rem} must be {allergen}")

            [i.remove(rem) for a, i in final_choices.items() if a != allergen and rem in i]


for line in data:

    ingredients = line.split(" (contains")[0].split(" ")
    allergens = line.split(" (contains ")[1][:-1].split(", ")
    
    for allergen, ingredient in final_choices.items():
        ingredient = ingredient[0]
##
##        if ingredient in ingredients and allergen not in allergens:
##            print("allergen not listed,", ingredient, "found")

        if ingredient not in ingredients and allergen in allergens:
            print("allergen listed but", ingredient, "not found")


print(len(all_ingredients))

for allergen, ing in final_choices.items():

    i = ing[0]

    while i in all_ingredients:

        all_ingredients.remove(i)

print("No allergens")

print(len(all_ingredients))

final_allergens = [i[0] for i in final_choices.values()]

tot = 0
for line in data:

    ingredients = line.split(" (")[0].strip().split(" ")

    for ing in ingredients:

        if ing not in final_allergens:
            tot += 1








print(result)
        



        
