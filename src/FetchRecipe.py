import requests
from bs4 import BeautifulSoup as bs
from ParseMethods import parse_method
import re
import unicodedata as ud
from parse_ingredients import parse_ingredient
from parse_tools import parse_tool

def fetchRecipe(url):
    numerator = {
        'ONE':1,
        'TWO':2,
        'THREE':3,
        'FOUR':4,
        'FIVE':5,
        'SIX':6,
        'SEVEN':7,
        'EIGHT':8,
        'NINE':9,
        'ZERO':0,
        }
    denominator = {
        'QUARTER':4,
        'HALF':2,
        'SEVENTH':7,
        'NINTH':9,
        'THIRD':3,
        'FIFTH':5,
        'SIXTH':6,
        'EIGHTH':8,
        'SIXTEENTH':16
        }

    fraction = {}
    for num in range(0x110000):
        s = chr(num)
        try:
            name = ud.name(s)
        except ValueError:
            continue
        match = re.search('FRACTION ({n}) ({d})'.format(
            n = '|'.join(numerator.keys()),
            d = '|'.join(denominator.keys()),
            ) , name)
        if match:
            fraction[num] = str(
            float(numerator[match.group(1)])/denominator[match.group(2)]).lstrip('0')

    try:
        if not re.search("allrecipes.com/recipe/", url):
            raise AssertionError("Not a valid AllRecipes URL!")
        
        recipe = {}

        page = requests.get(url)
        soup = bs(page.content, "html.parser")

        # Recipe Title
        recipe["title"] = soup.find("h1", class_="headline heading-content elementFont__display").text

        ''' Recipe Info
            - Format is (TYPE, AMOUNT)
            - TYPE is "prep", "cook", "total" (time based) or "servings" or "yield"
        '''
        recipe_info = [x.text[:-1] for x in soup.find_all("div", class_="recipe-meta-item-header elementFont__subtitle--bold elementFont__transformCapitalize")]
        recipe_info_details = [x.text[:-1] for x in soup.find_all("div", class_="recipe-meta-item-body elementFont__subtitle")]
        recipe["info"] = zip(recipe_info, recipe_info_details)

        ## Ingredients
        ingredients = [x.text[:-1] for x in soup.find_all("span", class_="ingredients-item-name elementFont__body")]
        ingredients = [ingredient.strip().translate(fraction).encode('ascii', 'ignore').decode("utf-8") for ingredient in ingredients]

        parsed_ingredients = []
        for ingredient in ingredients:
            print(parse_ingredient(ingredient))
            parsed_ingredients.append(parse_ingredient(ingredient))
        recipe["ingredients"] = parsed_ingredients

        # Directions
        directions = soup.find_all("div", class_="section-body elementFont__body--paragraphWithin elementFont__body--linkWithin")
        print(directions)
        recipe["directions"] = [method.strip().encode('ascii', 'ignore').decode("utf-8") for method in directions]

        # Nutrition
        nutrition = soup.find("div", class_="recipeNutritionSectionBlock")
        recipe["nutrition"] = nutrition.text[1:-17]

        # Methods
        methods = []
        for i in range(len(directions)):
            method = parse_method(directions[i], i)
            methods.append(method)
            print(method.direction, method.primary_cooking, method.secondary_cooking)
        recipe["methods"] = methods

        # Tools
        # recipe["tools"] = parse_tool(methods)

        print(recipe['methods'])

        return recipe


    except AssertionError as error:
        print(repr(error))
        return None

fetchRecipe('https://www.allrecipes.com/recipe/228285/teriyaki-salmon/')