
# Python| Using classes combinations, permutations and product from itertools

## 🤔 About combinations, permutations, and product

combinations, permutations, and product are classes from the library itertools and mathmatical concepts that can be useful for different situations.

### combinations() -> When order of elements doesn't matter

Used when the order of elements is not important. For example: ingredients of pudding. It doesn't matter if you add 3 eggs BEFORE the condensed milk inside the blender or the condensed milk before the eggs. Or if you add strawberry icecream before the chocolate icecream.

pudding recipe: 

    ingredients = ["eggs", "condensed milk", "milk"]

    inside_blender = list(combinations(ingredients, 3))

    print(inside_blender)

    ---> [('eggs', 'condensed milk', 'milk')]


icecream:

    icecream_flavors = ["Strawberry", "Chocolate", "Pistacchio"]

    print(list(combinations(icecream, 2)))

    ---> [('Strawberry', 'Chocolate'), ('Strawberry', 'Pistacchio'), ('Chocolate', 'Pistacchio')]


## permutations() -> When order of elements makes difference

We use permutations when the order of the elements is important. For example, a podium where we have first place, second, and third.

    # create a list of permutations

    def show_iterable(iterable):
    a = list(iterable)
    return a

    # define the podium (where order matters)

    def define_podium(runners):
        list_of_permutations = show_iterable(permutations(runners, 3))
        for n, element in enumerate(list_of_permutations):

        print(f"Podium {n}: {element}" , sep= '\n')


## product() --> order matters and unique values are repeated

Simple example to clarify:

    list_of_people1 = ["Clara", "Anna", "Michel", "Lauren"]
    list_of_people2 = ["Hugo", "Lara", "Oliver", "Lana"]
        
    list_of_possible_couples = list(product(list_of_people1, list_of_people2))
    print(list_of_possible_couples)


Starting with Clara. Clara has Hugo, Lara, Oliver and Lana as suitors. So for Clara, the possible arrangements are:

    --> ('Clara', 'Hugo'), ('Clara', 'Lara'), ('Clara', 'Oliver'), ('Clara', 'Lana')

And everyone else has the same list of suitors:

    --> ...('Anna', 'Hugo'), ('Anna', 'Lara'), ('Anna', 'Oliver'), ('Anna', 'Lana'), ('Michel', 'Hugo'), ('Michel', 'Lara'), ('Michel', 'Oliver'), ('Michel', 'Lana'), ('Lauren', 'Hugo'), ('Lauren', 'Lara'), ('Lauren', 'Oliver'), ('Lauren', 'Lana')


Product() also accepts another argument which is repeat:

    list_of_possible_couples = list(product(list_of_people1, list_of_people2, repeat = 2))
print(list_of_possible_couples)

Which results in:

    -->
    [('Clara', 'Hugo', 'Clara', 'Hugo'), ('Clara', 'Hugo', 'Clara', 'Lara'), ('Clara', 'Hugo', 'Clara', 'Oliver'), ('Clara', 'Hugo', 'Clara', 'Lana'), ('Clara', 'Hugo', 'Anna', 'Hugo'), ('Clara', 'Hugo', 'Anna', 'Lara'), ('Clara', 'Hugo', 'Anna', 'Oliver'), ('Clara', 'Hugo', 'Anna', 'Lana'), ('Clara', 'Hugo', 'Michel', 'Hugo'), ('Clara', 'Hugo', 'Michel', 'Lara'), ('Clara', 'Hugo', 'Michel', 'Oliver'), ('Clara', 'Hugo', 'Michel', 'Lana'), ('Clara', 'Hugo', 'Lauren', 'Hugo'), ('Clara', 'Hugo', 'Lauren', 'Lara'), ('Clara', 'Hugo', 'Lauren', 'Oliver'), ('Clara', 'Hugo', 'Lauren', 'Lana'), ('Clara', 'Lara', 'Clara', 'Hugo'), ('Clara', 'Lara', 'Clara', 'Lara'), ('Clara', 'Lara', 'Clara', 'Oliver'), ('Clara', 'Lara', 'Clara', 'Lana'), ('Clara', 'Lara', 'Anna', 'Hugo'), ('Clara', 'Lara', 'Anna', 'Lara'), ('Clara', 'Lara', 'Anna', 'Oliver'), ('Clara', 'Lara', 'Anna', 'Lana'), ('Clara', 'Lara', 'Michel', 'Hugo'), ('Clara', 'Lara', 'Michel', 'Lara'), ('Clara', 'Lara', 'Michel', 'Oliver'), ('Clara', 'Lara', 'Michel', 'Lana'), ('Clara', 'Lara', 'Lauren', 'Hugo'), ('Clara', 'Lara', 'Lauren', 'Lara'), ('Clara', 'Lara', 'Lauren', 'Oliver'), ('Clara', 'Lara', 'Lauren', 'Lana'), ('Clara', 'Oliver', 'Clara', 'Hugo'), ('Clara', 'Oliver', 'Clara', 'Lara'), ('Clara', 'Oliver', 'Clara', 'Oliver'), ('Clara', 'Oliver', 'Clara', 'Lana'), ('Clara', 'Oliver', 'Anna', 'Hugo'), ('Clara', 'Oliver', 'Anna', 'Lara'), ('Clara', 'Oliver', 'Anna', 'Oliver'), ('Clara', 'Oliver', 'Anna', 'Lana'), ('Clara', 'Oliver', 'Michel', 'Hugo'), ('Clara', 'Oliver', 'Michel', 'Lara'), ('Clara', 'Oliver', 'Michel', 'Oliver'), ('Clara', 'Oliver', 'Michel', 'Lana'), ('Clara', 'Oliver', 'Lauren', 'Hugo'), ('Clara', 'Oliver', 'Lauren', 'Lara'), ('Clara', 'Oliver', 'Lauren', 'Oliver'), ('Clara', 'Oliver', 'Lauren', 'Lana'), ('Clara', 'Lana', 'Clara', 'Hugo'), ('Clara', 'Lana', 'Clara', 'Lara'), ('Clara', 'Lana', 'Clara', 'Oliver'), ('Clara', 'Lana', 'Clara', 'Lana'), ('Clara', 'Lana', 'Anna', 'Hugo'), ('Clara', 'Lana', 'Anna', 'Lara'), ('Clara', 'Lana', 'Anna', 'Oliver'), ('Clara', 'Lana', 'Anna', 'Lana'), ('Clara', 'Lana', 'Michel', 'Hugo'), ('Clara', 'Lana', 'Michel', 'Lara'), ('Clara', 'Lana', 'Michel', 'Oliver'), ('Clara', 'Lana', 'Michel', 'Lana'), ('Clara', 'Lana', 'Lauren', 'Hugo'), ('Clara', 'Lana', 'Lauren', 'Lara'), ('Clara', 'Lana', 'Lauren', 'Oliver'), ('Clara', 'Lana', 'Lauren', 'Lana'), ('Anna', 'Hugo', 'Clara', 'Hugo'), ('Anna', 'Hugo', 'Clara', 'Lara'), ('Anna', 'Hugo', 'Clara', 'Oliver'), ('Anna', 'Hugo', 'Clara', 'Lana'), ('Anna', 'Hugo', 'Anna', 'Hugo'), ('Anna', 'Hugo', 'Anna', 'Lara'), ('Anna', 'Hugo', 'Anna', 'Oliver'), ('Anna', 'Hugo', 'Anna', 'Lana'), ('Anna', 'Hugo', 'Michel', 'Hugo'), ('Anna', 'Hugo', 'Michel', 'Lara'), ('Anna', 'Hugo', 'Michel', 'Oliver'), ('Anna', 'Hugo', 'Michel', 'Lana'), ('Anna', 'Hugo', 'Lauren', 'Hugo'), ('Anna', 'Hugo', 'Lauren', 'Lara'), ('Anna', 'Hugo', 'Lauren', 'Oliver'), ('Anna', 'Hugo', 'Lauren', 'Lana'), ('Anna', 'Lara', 'Clara', 'Hugo'), ('Anna', 'Lara', 'Clara', 'Lara'), ('Anna', 'Lara', 'Clara', 'Oliver'), ('Anna', 'Lara', 'Clara', 'Lana'), ('Anna', 'Lara', 'Anna', 'Hugo'), ('Anna', 'Lara', 'Anna', 'Lara'), ('Anna', 'Lara', 'Anna', 'Oliver'), ('Anna', 'Lara', 'Anna', 'Lana'), ('Anna', 'Lara', 'Michel', 'Hugo'), ('Anna', 'Lara', 'Michel', 'Lara'), ('Anna', 'Lara', 'Michel', 'Oliver'), ('Anna', 'Lara', 'Michel', 'Lana'), ('Anna', 'Lara', 'Lauren', 'Hugo'), ('Anna', 'Lara', 'Lauren', 'Lara'), ('Anna', 'Lara', 'Lauren', 'Oliver'), ('Anna', 'Lara', 'Lauren', 'Lana'), ('Anna', 'Oliver', 'Clara', 'Hugo'), ('Anna', 'Oliver', 'Clara', 'Lara'), ('Anna', 'Oliver', 'Clara', 'Oliver'), ('Anna', 'Oliver', 'Clara', 'Lana'), ('Anna', 'Oliver', 'Anna', 'Hugo'), ('Anna', 'Oliver', 'Anna', 'Lara'), ('Anna', 'Oliver', 'Anna', 'Oliver'), ('Anna', 'Oliver', 'Anna', 'Lana'), ('Anna', 'Oliver', 'Michel', 'Hugo'), ('Anna', 'Oliver', 'Michel', 'Lara'), ('Anna', 'Oliver', 'Michel', 'Oliver'), ('Anna', 'Oliver', 'Michel', 'Lana'), ('Anna', 'Oliver', 'Lauren', 'Hugo'), ('Anna', 'Oliver', 'Lauren', 'Lara'), ('Anna', 'Oliver', 'Lauren', 'Oliver'), ('Anna', 'Oliver', 'Lauren', 'Lana'), ('Anna', 'Lana', 'Clara', 'Hugo'), ('Anna', 'Lana', 'Clara', 'Lara'), ('Anna', 'Lana', 'Clara', 'Oliver'), ('Anna', 'Lana', 'Clara', 'Lana'), ('Anna', 'Lana', 'Anna', 'Hugo'), ('Anna', 'Lana', 'Anna', 'Lara'), ('Anna', 'Lana', 'Anna', 'Oliver'), ('Anna', 'Lana', 'Anna', 'Lana'), ('Anna', 'Lana', 'Michel', 'Hugo'), ('Anna', 'Lana', 'Michel', 'Lara'), ('Anna', 'Lana', 'Michel', 'Oliver'), ('Anna', 'Lana', 'Michel', 'Lana'), ('Anna', 'Lana', 'Lauren', 'Hugo'), ('Anna', 'Lana', 'Lauren', 'Lara'), ('Anna', 'Lana', 'Lauren', 'Oliver'), ('Anna', 'Lana', 'Lauren', 'Lana'), ('Michel', 'Hugo', 'Clara', 'Hugo'), ('Michel', 'Hugo', 'Clara', 'Lara'), ('Michel', 'Hugo', 'Clara', 'Oliver'), ('Michel', 'Hugo', 'Clara', 'Lana'), ('Michel', 'Hugo', 'Anna', 'Hugo'), ('Michel', 'Hugo', 'Anna', 'Lara'), ('Michel', 'Hugo', 'Anna', 'Oliver'), ('Michel', 'Hugo', 'Anna', 'Lana'), ('Michel', 'Hugo', 'Michel', 'Hugo'), ('Michel', 'Hugo', 'Michel', 'Lara'), ('Michel', 'Hugo', 'Michel', 'Oliver'), ('Michel', 'Hugo', 'Michel', 'Lana'), ('Michel', 'Hugo', 'Lauren', 'Hugo'), ('Michel', 'Hugo', 'Lauren', 'Lara'), ('Michel', 'Hugo', 'Lauren', 'Oliver'), ('Michel', 'Hugo', 'Lauren', 'Lana'), ('Michel', 'Lara', 'Clara', 'Hugo'), ('Michel', 'Lara', 'Clara', 'Lara'), ('Michel', 'Lara', 'Clara', 'Oliver'), ('Michel', 'Lara', 'Clara', 'Lana'), ('Michel', 'Lara', 'Anna', 'Hugo'), ('Michel', 'Lara', 'Anna', 'Lara'), ('Michel', 'Lara', 'Anna', 'Oliver'), ('Michel', 'Lara', 'Anna', 'Lana'), ('Michel', 'Lara', 'Michel', 'Hugo'), ('Michel', 'Lara', 'Michel', 'Lara'), ('Michel', 'Lara', 'Michel', 'Oliver'), ('Michel', 'Lara', 'Michel', 'Lana'), ('Michel', 'Lara', 'Lauren', 'Hugo'), ('Michel', 'Lara', 'Lauren', 'Lara'), ('Michel', 'Lara', 'Lauren', 'Oliver'), ('Michel', 'Lara', 'Lauren', 'Lana'), ('Michel', 'Oliver', 'Clara', 'Hugo'), ('Michel', 'Oliver', 'Clara', 'Lara'), ('Michel', 'Oliver', 'Clara', 'Oliver'), ('Michel', 'Oliver', 'Clara', 'Lana'), ('Michel', 'Oliver', 'Anna', 'Hugo'), ('Michel', 'Oliver', 'Anna', 'Lara'), ('Michel', 'Oliver', 'Anna', 'Oliver'), ('Michel', 'Oliver', 'Anna', 'Lana'), ('Michel', 'Oliver', 'Michel', 'Hugo'), ('Michel', 'Oliver', 'Michel', 'Lara'), ('Michel', 'Oliver', 'Michel', 'Oliver'), ('Michel', 'Oliver', 'Michel', 'Lana'), ('Michel', 'Oliver', 'Lauren', 'Hugo'), ('Michel', 'Oliver', 'Lauren', 'Lara'), ('Michel', 'Oliver', 'Lauren', 'Oliver'), ('Michel', 'Oliver', 'Lauren', 'Lana'), ('Michel', 'Lana', 'Clara', 'Hugo'), ('Michel', 'Lana', 'Clara', 'Lara'), ('Michel', 'Lana', 'Clara', 'Oliver'), ('Michel', 'Lana', 'Clara', 'Lana'), ('Michel', 'Lana', 'Anna', 'Hugo'), ('Michel', 'Lana', 'Anna', 'Lara'), ('Michel', 'Lana', 'Anna', 'Oliver'), ('Michel', 'Lana', 'Anna', 'Lana'), ('Michel', 'Lana', 'Michel', 'Hugo'), ('Michel', 'Lana', 'Michel', 'Lara'), ('Michel', 'Lana', 'Michel', 'Oliver'), ('Michel', 'Lana', 'Michel', 'Lana'), ('Michel', 'Lana', 'Lauren', 'Hugo'), ('Michel', 'Lana', 'Lauren', 'Lara'), ('Michel', 'Lana', 'Lauren', 'Oliver'), ('Michel', 'Lana', 'Lauren', 'Lana'), ('Lauren', 'Hugo', 'Clara', 'Hugo'), ('Lauren', 'Hugo', 'Clara', 'Lara'), ('Lauren', 'Hugo', 'Clara', 'Oliver'), ('Lauren', 'Hugo', 'Clara', 'Lana'), ('Lauren', 'Hugo', 'Anna', 'Hugo'), ('Lauren', 'Hugo', 'Anna', 'Lara'), ('Lauren', 'Hugo', 'Anna', 'Oliver'), ('Lauren', 'Hugo', 'Anna', 'Lana'), ('Lauren', 'Hugo', 'Michel', 'Hugo'), ('Lauren', 'Hugo', 'Michel', 'Lara'), ('Lauren', 'Hugo', 'Michel', 'Oliver'), ('Lauren', 'Hugo', 'Michel', 'Lana'), ('Lauren', 'Hugo', 'Lauren', 'Hugo'), ('Lauren', 'Hugo', 'Lauren', 'Lara'), ('Lauren', 'Hugo', 'Lauren', 'Oliver'), ('Lauren', 'Hugo', 'Lauren', 'Lana'), ('Lauren', 'Lara', 'Clara', 'Hugo'), ('Lauren', 'Lara', 'Clara', 'Lara'), ('Lauren', 'Lara', 'Clara', 'Oliver'), ('Lauren', 'Lara', 'Clara', 'Lana'), ('Lauren', 'Lara', 'Anna', 'Hugo'), ('Lauren', 'Lara', 'Anna', 'Lara'), ('Lauren', 'Lara', 'Anna', 'Oliver'), ('Lauren', 'Lara', 'Anna', 'Lana'), ('Lauren', 'Lara', 'Michel', 'Hugo'), ('Lauren', 'Lara', 'Michel', 'Lara'), ('Lauren', 'Lara', 'Michel', 'Oliver'), ('Lauren', 'Lara', 'Michel', 'Lana'), ('Lauren', 'Lara', 'Lauren', 'Hugo'), ('Lauren', 'Lara', 'Lauren', 'Lara'), ('Lauren', 'Lara', 'Lauren', 'Oliver'), ('Lauren', 'Lara', 'Lauren', 'Lana'), ('Lauren', 'Oliver', 'Clara', 'Hugo'), ('Lauren', 'Oliver', 'Clara', 'Lara'), ('Lauren', 'Oliver', 'Clara', 'Oliver'), ('Lauren', 'Oliver', 'Clara', 'Lana'), ('Lauren', 'Oliver', 'Anna', 'Hugo'), ('Lauren', 'Oliver', 'Anna', 'Lara'), ('Lauren', 'Oliver', 'Anna', 'Oliver'), ('Lauren', 'Oliver', 'Anna', 'Lana'), ('Lauren', 'Oliver', 'Michel', 'Hugo'), ('Lauren', 'Oliver', 'Michel', 'Lara'), ('Lauren', 'Oliver', 'Michel', 'Oliver'), ('Lauren', 'Oliver', 'Michel', 'Lana'), ('Lauren', 'Oliver', 'Lauren', 'Hugo'), ('Lauren', 'Oliver', 'Lauren', 'Lara'), ('Lauren', 'Oliver', 'Lauren', 'Oliver'), ('Lauren', 'Oliver', 'Lauren', 'Lana'), ('Lauren', 'Lana', 'Clara', 'Hugo'), ('Lauren', 'Lana', 'Clara', 'Lara'), ('Lauren', 'Lana', 'Clara', 'Oliver'), ('Lauren', 'Lana', 'Clara', 'Lana'), ('Lauren', 'Lana', 'Anna', 'Hugo'), ('Lauren', 'Lana', 'Anna', 'Lara'), ('Lauren', 'Lana', 'Anna', 'Oliver'), ('Lauren', 'Lana', 'Anna', 'Lana'), ('Lauren', 'Lana', 'Michel', 'Hugo'), ('Lauren', 'Lana', 'Michel', 'Lara'), ('Lauren', 'Lana', 'Michel', 'Oliver'), ('Lauren', 'Lana', 'Michel', 'Lana'), ('Lauren', 'Lana', 'Lauren', 'Hugo'), ('Lauren', 'Lana', 'Lauren', 'Lara'), ('Lauren', 'Lana', 'Lauren', 'Oliver'), ('Lauren', 'Lana', 'Lauren', 'Lana')]

Translation:
I'm asking the product class to repeat 2 times the whole iterable. It's something like this: 

    product(list_of_people1, list_of_people2, list_of_people1, list_of_people2)

    --> person1, person2, person3, person4
    --> Clara, Hugo, Clara, Hugo

person1 from list_of_people1

person2 from list_of_people2

person3 from list_of_people1

person4 from list_of_people2


## Exercises AI Generated

To practice these concepts in Python, I used AI generated challenges from beginner to intermediate level.

# Beginner Level

## Ice Cream Flavor Combinations
Generate all possible ice cream flavor pairs using `combinations()`.

File:
```python
icecream_flav_comb.py
```

---

## 2-Digit Password Generator
Generate all possible 2-digit passwords using `product()`.

File:
```python
password_2digits_product.py
```

---

## Seating Arrangements
Generate all seating orders using `permutations()`.

File:
```python
seating_orders_perm.py
```

---

# Intermediate Level

## Pizza Toppings
Generate pizza topping combinations.

File:
```python
pizza_toppings.py
```

## Outfit Combinations
Generate outfit possibilities using `product()`.

File:
```python
outfit_combinations.py
```

## Podium Permutations
Generate race podium possibilities using `permutations()`.
```python
podium_permutations.py
```

## Future Improvements

- Add advanced level challenges to the repository 