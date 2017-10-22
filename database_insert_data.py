import parsing
from database_engine import *


cocktails = parsing.get_cocktails_list()
ingredients = []
units = []

debug_mode = 1
if debug_mode == 1:
    cocktail_count = 0.0
    cocktail_all = len(cocktails)

for cocktail_name in cocktails:
    if debug_mode == 1:
        print(cocktail_name)

    cocktail_url = parsing.get_cocktail_url(cocktail_name)
    cocktail_recipe_text = parsing.get_recipe(cocktail_url, 'recipe_text')

    # cocktail_ingredients = parsing.get_recipe(cocktail_url, 'ingredient_list')
    #
    # for ingredient in cocktail_ingredients:
    #     ingredients.append(ingredient['name'])
    #     units.append(ingredient['unit'])

    # current_cocktail = User
    current_cocktail = Cocktail.query.filter(Cocktail.name == cocktail_name).first()
    current_cocktail.recipe_text = cocktail_recipe_text
    # db_session.add(current_cocktail)

    if debug_mode == 1:
        cocktail_count += 1
        print(str(round(cocktail_count/cocktail_all * 100, 2)) + '%')

# ingredients = list(set(ingredients))
# units = list(set(units))
# for ingredient in ingredients:
#     current_ingredient = Ingredient(name=ingredient)
#     db_session.add(current_ingredient)
# for unit in units:
#     current_unit = Unit(name=unit)
#     db_session.add(current_unit)


db_session.commit()
