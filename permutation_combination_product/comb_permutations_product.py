from itertools import  combinations,permutations, product

# permutations --> order matters
# combinations --> order doesn't matter
# product --> order matters and repeats unique values  (cartesian product, equivalent to a nested for-loop)
def print_iterators(iterator):
    print(*list(iterator), sep= "\n")
    print()

list_of_clothes = ["Shirt", "Dress", "Skirt"]
list_clothes_and_clients = [["Alessandra", "Otávio", "Pedro"],
                ["Shirt", "Dress", "Skirt"],
                # ["Blue", "Red", "Green"]
               ]

# print_iterators(combinations(list_of_clothes, 2)) # the list will make groups of 2
# print_iterators(permutations(list_of_clothes, 2))
# print_iterators(product(list_of_clothes))
# print_iterators(product(*list_clothes_and_clients))



A = [1, 2, 3, 4]
B = [4, 3, 2, 1]

a_list = [(x, y) for x in A for y in B]

print(a_list)
