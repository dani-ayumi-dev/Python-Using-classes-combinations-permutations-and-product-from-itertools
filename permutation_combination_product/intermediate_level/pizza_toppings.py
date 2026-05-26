"""
4. Pizza Toppings (combinations)

A pizza shop allows customers to choose 3 toppings from:

toppings = ["Cheese", "Pepperoni", "Bacon", "Olives", "Mushrooms"]

Generate all possible pizza combinations of exactly 3 toppings.

Challenge: Count how many combinations exist.

"""

from function_package import show_iterable
from itertools import combinations, count

toppings = ["Cheese", "Pepperoni", "Bacon", "Olives", "Mushrooms"]

def combinating_and_counting(the_list, r=0):
    comb = combinations(the_list, r )
    counting = 0
    for elem in show_iterable(comb):
        counting += 1
    print("Combinations: ", show_iterable(combinations(toppings, 3)), '\n')
    print("Number of combinations:", counting)


combinating_and_counting(toppings, 3)








# Challenge: Count how many combinations exist.
