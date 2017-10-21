from bs4 import BeautifulSoup
from get_html import get_html


def get_recipe(url, what_to_return='recipe_text'):

    html = get_html(url)
    bs = BeautifulSoup(html, 'html.parser')

    if what_to_return == 'recipe_text':
        # парсим шаги рецепта
        step_num = 0
        full_text = ''
        recipe = bs.find('ul', class_='steps')
        for step in recipe.find_all('li'):
            step_num += 1
            full_text += str(step_num) + '. ' + step.text + '\n'
        return full_text

    if what_to_return == 'ingredient_list':
        ingredient_list = []
        ingredient_description = {}
        # парсим ингридиенты
        ingredients = bs.find('dl', class_='ingredients')
        for ingredient in ingredients.find_all('dt', class_='good'):
            for ingredient_name in ingredient.find_all('a', class_='ingredient-link'):
                ingredient_description['name'] = ingredient_name.text
            for ingredient_amount in ingredient.find_all('amount'):
                ingredient_description['amount'] = ingredient_amount.text
            for ingredient_unit in ingredient.find_all('unit'):
                ingredient_description['unit'] = ingredient_unit.text
            ingredient_list.append(ingredient_description)
        return ingredient_list

    if what_to_return == 'thing':
        # парсим штучки (дописать)
        return None


def get_cocktail_url(cocktail_name):
    search_url = 'http://ru.inshaker.com/cocktails?q={}'.format(cocktail_name.replace(' ', '%20'))
    html = get_html(search_url)
    bs = BeautifulSoup(html, 'html.parser')
    cocktails_common_list = bs.find('div', class_='cocktails common-list')
    for cocktail_url in cocktails_common_list.find_all('a', class_='cocktail-preview'):
        return cocktail_url['href']


def get_cocktails_list():
    cocktail_list = []
    search_url = 'http://ru.inshaker.com/cocktails?page=99'
    html = get_html(search_url)
    bs = BeautifulSoup(html, 'html.parser')
    cocktail_preview_desktop = bs.find_all('a', class_='cocktail-preview desktop')
    for cocktail_name in cocktail_preview_desktop:
        result = cocktail_name.find('div', class_='label').text.replace('\xa0', ' ')
        cocktail_list.append(result)
    return cocktail_list


if __name__ == '__main__':
    print(get_cocktails_list())
