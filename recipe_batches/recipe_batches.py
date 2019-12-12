#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    # Step 1: Check keys in recipe and ingredients, return -1 if key doesn't exist in ingredients
    def check_keys():
        for key in recipe.keys():
            if key not in ingredients.keys():
                return -1

    # Step 2: Check values in recipe and ingredients, return -1 if ingredient value is less than recipe value
    def compare_amounts():
        for key, value in recipe.items():
            if ingredients[key] < value:
                return -1

    # Step 3: Subtract values from ingredients and num += 1, while ingredients values are greater than recipe value
    def num_recipes():
        cache = []
        for key, value in ingredients.items():
            num = 0
            while value - recipe[key] >= 0:
                value = value - recipe[key]
                num += 1
            cache.append(num)
        return min(cache)

    # STEP 1, STEP 2
    if check_keys() != -1 and compare_amounts() != -1:
        # STEP 3
        return num_recipes()
    else:
        return 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
