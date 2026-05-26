"""
2. Password Variations (product)

Generate every possible 2-digit password using:

digits = "12"

Example outputs:

('1', '1')
('1', '2')
('2', '1')
('2', '2')

"""

from permutation_combination_product.beginner_level.function_package.function_show_iter import show_iterable
from itertools import product

digits = "12"

using_list_comprehension = [(x,y) for x in digits for y in digits]
print("Using List Comprehension:",*using_list_comprehension)

print()
print("Using product class")

show_iterable(product(digits, repeat=2))