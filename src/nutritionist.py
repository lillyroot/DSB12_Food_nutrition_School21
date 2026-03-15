#!/usr/bin/env python3
from recipes import Ingredient, Recipe, Menu

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError('Not enough arguments')
    elif (sys.argv[1] == 'Menu'):
        menu = Menu()
        menu.generate_menu()
        menu.print_menu()
    else:
        ingredients_list = []
        for i in range(1, len(sys.argv)):
            ingredient = Ingredient(sys.argv[i].replace(",", ""))
            ingredients_list.append(ingredient)
        recipe = Recipe(ingredients_list)
        recipe.get_forecast()
        recipe.get_nutrition_facts()    
        recipe.get_three_dishes()
