#!/usr/bin/env python3
from recipes import Ingredient, Recipe

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError('Not enough arguments')
    else:
        ingredients_list = []
        for i in range(1, len(sys.argv)):
            ingredient = Ingredient(sys.argv[i].replace(",", ""))
            ingredients_list.append(ingredient)
        for ingredient in ingredients_list:
            print(ingredient.name_)
        recipe = Recipe(ingredients_list)
        recipe.get_nutrition_facts()    
        recipe.get_three_dishes()

        