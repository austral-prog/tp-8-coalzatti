

def clean_ingredients(dish_name, dish_ingredients):
    dish_ingr_set= set(dish_ingredients)
    fdish= dish_name, dish_ingr_set
    return fdish   

from sets_categories_data import (ALCOHOLS)

def check_drinks(drink_name, drink_ingredients):
    if len(set(drink_ingredients.intersection(ALCOHOLS))) != 0:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"
