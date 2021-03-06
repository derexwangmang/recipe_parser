from pyparsing import opAssoc
from src.FetchRecipe import fetchRecipe
# from src.ParseMethods import parse_method
from src.transformation_health import transform_healthy
from src.transformation_vegetarian import transform_vegetarian
from printpretty import prettyprint
from src.transformation_free import transform_free
from src.transformation_chinese import transformation_chinese
from src.DoubleHalfIngredients import doubleHalfIngredients


print("Welcome to our recipe parser and interactive cookbook!")
print("Please provide the URL of a recipe from AllRecipes.com: ", end='')
url = str(input())

while not url.startswith("https://www.allrecipes.com/"):
    print("{} does not start with https://www.allrecipes.com/".format(url))
    print("Please provide the URL of a recipe from AllRecipes.com: ", end='')
    url = str(input())

recipe = fetchRecipe(url)
print("\nFetched from {}".format(url))
print("\nWhat would you like to do with the recipe?\n")
print("Option 1: To vegetarian")
print("Option 2: To non-vegetarian")
print("Option 3: To healthy")
print("Option 4: To non-healthy")
print("Option 5: To Chinese cuisine")
print("Option 6: Double the amount")
print("Option 7: Half the amount")
print("Option 8: To gluten-free")
print("Option 9: To lactose-free")
print("\nInput a number 1-9: ", end='')

option = input()
while not option.isdigit() or not 1 <= int(option) <= 9:
    print("ERROR: {} not within 1-9".format(option))
    print("Input a number 1-9: ", end='')
    option = input()


option = int(option)

if option == 1:
    print("\nYou chose to transform your recipe to vegetarian.\n")
    newrecipe = transform_vegetarian(recipe, 'vegetarian')
    transformation = "vegetarian"
    prettyprint(newrecipe, transformation)
elif option == 2:
    print("\nYou chose to transform your recipe to non-vegetarian.\n")
    newrecipe = transform_vegetarian(recipe, 'non-vegetarian')
    transformation = "non-vegetarian"
    prettyprint(newrecipe, transformation)
elif option == 3:
    print("\nYou chose to transform your recipe to healthy.\n")
    newrecipe = transform_healthy(recipe, 1)
    transformation = "healthy"
    prettyprint(newrecipe, transformation)
elif option == 4:
    print("\nYou chose to transform your recipe to unhealthy.\n")
    newrecipe = transform_healthy(recipe, 0)
    transformation = "unhealthy"
    prettyprint(newrecipe, transformation)
elif option == 5:
    print("\nYou chose to transform the cuisine of your recipe to Chinese.\n")
    newrecipe = transformation_chinese(recipe)
    prettyprint(newrecipe, "Chinese")
elif option == 6:
    print("\nYou chose to double the ingredients in your recipe.\n")
    newrecipe = doubleHalfIngredients(recipe, double=True)
    prettyprint(newrecipe, "double the ingredients")
elif option == 7:
    print("\nYou chose to half the ingredients in your recipe.\n")
    newrecipe = doubleHalfIngredients(recipe, double=False)
    prettyprint(newrecipe, "half the ingredients")
elif option == 8:
    print("\nYou chose to transform your recipe to gluten-free.\n")
    newrecipe = transform_free(recipe, 'gluten-free')
    transformation = "gluten-free"
    prettyprint(newrecipe, transformation)
elif option == 9:
    print("\nYou chose to transform your recipe to lactose-free.\n")
    newrecipe = transform_free(recipe, 'lactose-free')
    transformation = "lactose-free"
    prettyprint(newrecipe, transformation)
