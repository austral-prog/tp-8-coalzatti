
def clean_ingredients(dish_name, dish_ingredients):
    dish_ingr_set= set(dish_ingredients)
    fdish= dish_name, dish_ingr_set
    return fdish   



def check_drinks(drink_name, drink_ingredients):
    alcohols = {"whiskey", "whisky", "white rum", "dark rum", "bourbon", "rye", "scotch", "vodka",
            "tequila", "gin", "dry vermouth", "sweet vermouth", "prosecco","aperol", "brandy", "mezcal",
            "triple sec", "coffee liqueur", "almond liqueur", "champagne", "orange curacao", "rum"}
    if len(set(drink_ingredients.intersection(alcohols))) != 0:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"

