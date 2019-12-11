#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # Step 1: Check keys in recipe and ingredients, return 0 if key doesn't exist in ingredients
    def check_keys():
        for key in recipe.keys():
            if key not in ingredients.keys():
                return -1
            else:
                pass

    def compare_amounts(recipe, ingredients):
        for key, value in recipe.items():
            if ingredients[key] < value:
                return -1

    if check_keys() != -1 and compare_amounts(recipe, ingredients) != -1:
        return 'Hello'
    else:
        return 0

    # Else set num_recipes += 1

    # Step 2: Subtract values in ingredients from recipes

    # Step 3: Repeat Steps 1 and 2


print(recipe_batches({"eggs": 5, "flour": 2}, {"eggs": 5, "flour": 2}))


# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
