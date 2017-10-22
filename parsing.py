from bs4 import BeautifulSoup
from get_html import get_html
import requests
from transliterate import translit, get_available_language_codes


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
            for ingredient_name in ingredient.find_all('i'):
                ingredient_description['brand'] = ingredient_name.text
            for ingredient_name in ingredient.find_all('a', class_='ingredient-link'):
                ingredient_description['name'] = ingredient_name.text
            for ingredient_amount in ingredient.find_all('amount'):
                ingredient_description['amount'] = ingredient_amount.text
            for ingredient_unit in ingredient.find_all('unit'):
                ingredient_description['unit'] = ingredient_unit.text
            try:
                ingredient_description.update({'name': ingredient_description['name'].replace(ingredient_description['brand'], '')})
            except KeyError:
                pass
            ingredient_list.append(ingredient_description)
            ingredient_description = {}
        return ingredient_list

    if what_to_return == 'tool_list':
        # парсим штучки
        tool_list = []
        tool_description = {}
        tools = bs.find('dl', class_='tools')
        for tool in tools.find_all('dt', class_='good'):
            for tool_name in tool.find_all('a', class_='ingredient-link'):
                tool_description['name'] = tool_name.text
            for tool_amount in tool.find_all('amount'):
                tool_description['amount'] = tool_amount.text
            for tool_unit in tool.find_all('unit'):
                tool_description['unit'] = tool_unit.text
            tool_list.append(tool_description)
            tool_description = {}
        return tool_list


def get_cocktail_url(cocktail_name):
    search_url = 'http://ru.inshaker.com/cocktails?q={}'.format(cocktail_name.replace(' ', '%20'))
    html = get_html(search_url)
    bs = BeautifulSoup(html, 'html.parser')
    cocktails_common_list = bs.find('div', class_='cocktails common-list')
    for cocktail_url in cocktails_common_list.find_all('a', class_='cocktail-preview'):
        return 'http://ru.inshaker.com' + cocktail_url['href']


def get_cocktails_list(what_to_return='list'):
    cocktail_list = []
    search_url = 'http://ru.inshaker.com/cocktails?page=99'
    html = get_html(search_url)
    bs = BeautifulSoup(html, 'html.parser')
    cocktail_preview_desktop = bs.find_all('a', class_='cocktail-preview desktop')
    for cocktail_name in cocktail_preview_desktop:
        result = cocktail_name.find('div', class_='label').text.replace('\xa0', ' ')
        cocktail_list.append(result)
        # парсим картинки
        if what_to_return == 'image':
            img_url = cocktail_name.find('img', class_='image')['lazy-src']
            img = 'http://ru.inshaker.com/{}'.format(img_url)
            get_img = requests.get(img)
            out = open("./static/img/"+translit(result, 'ru', reversed=True).replace(' ', '_').lower()+".jpg", "wb")
            out.write(get_img.content)
            out.close()
    return cocktail_list


# def get_image(cocktail_name):
#     cocktail_url = get_cocktail_url(cocktail_name)
#     html = get_html(cocktail_url)
#     bs = BeautifulSoup(html, 'html.parser')
#
#     img_url = bs.find_all('img', class_='image')
#
#     print(img_url)

    # img = 'http://ru.inshaker.com/{}'.format()
    # p = requests.get(img)
    # out = open("./static/img/Martini_Royale-highres.jpg", "wb")
    # out.write(p.content)
    # out.close()


if __name__ == '__main__':
    print(get_recipe('http://ru.inshaker.com/cocktails/118-dzhokonda-shuter', what_to_return='ingredient_list'))

