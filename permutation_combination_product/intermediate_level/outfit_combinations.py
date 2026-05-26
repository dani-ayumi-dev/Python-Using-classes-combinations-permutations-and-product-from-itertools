"""
5. Outfit Generator (product)

You have:

shirts = ["Black", "White"]
pants = ["Jeans", "Shorts"]
shoes = ["Sneakers", "Boots"]

Generate every possible outfit combination.
"""
from itertools import product
from function_package import show_iterable
shirts = ["Black", "White"]
pants = ["Jeans", "Shorts"]
shoes = ["Sneakers", "Boots"]

def making_an_outfit(*kwargs): # receives n lists
    list_of_outfits = []
    for n, element in enumerate(show_iterable(product(*kwargs))):
        print(f"Outfit {n} : {element}", sep= '\n')

    


making_an_outfit(shirts, pants, shoes)


