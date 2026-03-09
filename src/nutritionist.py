#!/usr/bin/env python3
from recipes import Ingredient, Recipe

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError('Not enough arguments')
    else:
        ingredients_list = []
        for i in range(1, len(sys.argv)):
            ingrident = Ingredient(sys.argv[i])
            ingredients_list.append(ingrident)
        recipe = Recipe(ingredients_list)    

        