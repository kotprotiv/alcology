from bs4 import BeautifulSoup
from get_html import get_html


def get_recipe(url):

    html = get_html(url)
    bs = BeautifulSoup(html, 'html.parser')

    # парсим шаги рецепта
    step_num = 0
    recipe = bs.find('ul', class_='steps')
    for step in recipe.find_all('li'):
        step_num += 1
        print(str(step_num) + '. ' + step.text)

    # парсим ингридиенты
    ingredients = bs.find('dl', class_='ingredients')
    for ingredient in ingredients.find_all('dt', class_='good'):
        for ingredient_name in ingredient.find_all('a', class_='ingredient-link'):
            print(ingredient_name.text)
        for ingredient_amount in ingredient.find_all('amount'):
            print(ingredient_amount.text)
        for ingredient_unit in ingredient.find_all('unit'):
            print(ingredient_unit.text)

    # парсим штучки (дописать)


def get_cocktail_url(cocktail_name):
    search_url = 'http://ru.inshaker.com/cocktails?q={}'.format(cocktail_name.replace(' ', '%20'))
    html = get_html(search_url)
    bs = BeautifulSoup(html, 'html.parser')
    cocktail_url = bs.find_all('a', class_='cocktail-preview')
    return cocktail_url #['href']


def get_cocktails_list():
    return 0


print(get_cocktail_url('Крестный отец'))
