"""
3. Seating Arrangements (permutations)

Three friends:

friends = ["Ana", "Leo", "Kai"]

Generate all possible seating orders.

"""

from itertools import permutations
from function_package import show_iterable

friends = ["Anna", "Elsa", "Sven", "Olaf"]

show_iterable(permutations(friends))


