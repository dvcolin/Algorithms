#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    max_recipes = 0
    for key in recipe.keys():
        if key not in ingredients.keys():
            return 0

    def check_values():
        nonlocal max_recipes
        for key, value in ingredients.items():
            if value >= 0:
                if value - recipe[key] >= 0:
                    ingredients[key] = value - recipe[key]
                else:
                    return max_recipes
        max_recipes += 1
        return check_values()

    return check_values()


# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
