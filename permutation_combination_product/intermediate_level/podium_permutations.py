from itertools import permutations
from function_package import show_iterable

"""
6. Race Podium (permutations)

Four runners participated:

runners = ["A", "B", "C", "D"]

Generate every possible 1st, 2nd, and 3rd place podium arrangement.
"""

runners = ["A", "B", "C", "D"]

def define_podium(runners):
    list_of_permutations = show_iterable(permutations(runners, 3))
    for n, element in enumerate(list_of_permutations):

        print(f"Podium {n}: {element}" , sep= '\n')



define_podium(runners)