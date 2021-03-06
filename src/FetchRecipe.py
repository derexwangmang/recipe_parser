import requests
from bs4 import BeautifulSoup as bs
from src.ParseMethods import parse_method
import re
import unicodedata as ud
from parse_ingredients import parse_ingredient
from src.parse_tools import parse_tool
import sys, os
from src.ParseSteps import parseSteps


# https://stackoverflow.com/questions/8391411/how-to-block-calls-to-print
# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


def fetchRecipe(url):
    blockPrint()

    # https://stackoverflow.com/questions/15190930/python-beautifulsoup-parsing-html-fractions
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
            # print(ingredient)
            try:
                # print(parse_ingredient(ingredient))
                parsed_ingredients.append(parse_ingredient(ingredient))
            except:
                if ingredient == "salt and pepper to taste":
                    parsed_ingredients.append(parse_ingredient("1 tsp salt and pepper, or to taste"))
                else:
                    print("failed to add that ingredient\n\n\n\n\n\n")
        recipe["ingredients"] = parsed_ingredients

        # Directions
        directions = soup.find_all("div", class_="section-body elementFont__body--paragraphWithin elementFont__body--linkWithin")
        # print(directions)
        recipe["directions"] = [method.text[:-2].encode('ascii', 'ignore').decode("utf-8") for method in directions]

        # Nutrition
        nutrition = soup.find("div", class_="recipeNutritionSectionBlock")
        recipe["nutrition"] = nutrition.text[1:-17]

        # Methods
        methods = []
        methoddirections = []
        direc = ' '.join([x.text[:-3] for x in directions]).split('.')
        # print(direc)
        for i in range(len(direc)):
            method = parse_method(direc[i], i)
            methods.append(method)
            methoddirections.append(method.direction)
            # print("this is a method: ", method.direction)
            # print(method.direction, method.primary_cooking, method.secondary_cooking)
        recipe["methods"] = methods

        # Tools
        recipe["tools"] = parse_tool(methoddirections)
        # print(recipe["tools"])

        # steps
        recipe['steps'] = parseSteps(methoddirections)

        enablePrint()

        return recipe
    except AssertionError as error:
        enablePrint()
        print(repr(error))
        return None

# fetchRecipe('https://www.allrecipes.com/recipe/244716/shirataki-meatless-meat-pad-thai/')