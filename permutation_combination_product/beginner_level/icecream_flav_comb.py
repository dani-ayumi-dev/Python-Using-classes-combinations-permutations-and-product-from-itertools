# 1. Ice Cream Flavor Pairs (combinations)

# You have these flavors:

# flavors = ["Chocolate", "Vanilla", "Strawberry", "Mint"]

# Generate all possible pairs of flavors without repetition.

# Expected idea:
# ("Chocolate", "Vanilla") and ("Vanilla", "Chocolate") should NOT both appear.

from itertools import combinations
from function_package import show_iterable
flavors = ["Chocolate", "Vanilla", "Strawberry", "Mint"]
# create a function that will show the iterable 

show_iterable(combinations(flavors, r= 2))

'''
('Chocolate', 'Vanilla')
('Chocolate', 'Strawberry')
('Chocolate', 'Mint')
('Vanilla', 'Strawberry')
('Vanilla', 'Mint')
('Strawberry', 'Mint')
'''