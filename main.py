from pyparsing import opAssoc
from src.FetchRecipe import fetchRecipe
from src.ParseMethods import parse_method
from src.transformation_healthy import transform_healthy
from src.transformation_vegetarian import transform_vegetarian
from printpretty import prettyprint
from src.transformation_free import transform_free


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
print("Option 5: To an additional style of cuisine")
print("Option 6: To an additional style of cuisine")
print("Option 7: Double the amount")
print("Option 8: Half the amount")
print("Option 9: To gluten-free")
print("Option 10: To lactose-free")
print("\nInput a number 1-10: \n", end='')

option = input()
while not option.isdigit() or not 1 <= int(option) <= 10:
    print("ERROR: {} not within 1-10".format(option))
    print("Input a number 1-10: ", end='')
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
    pass
elif option == 6:
    pass
elif option == 7:
    pass
elif option == 8:
    pass
elif option == 9:
    print("\nYou chose to transform your recipe to gluten-free.\n")
    newrecipe = transform_free(recipe, 'gluten-free')
    transformation = "gluten-free"
    prettyprint(newrecipe, transformation)
elif option == 10:
    print("\nYou chose to transform your recipe to lactose-free.\n")
    newrecipe = transform_free(recipe, 'lactose-free')
    transformation = "lactose-free"
    prettyprint(newrecipe, transformation)



''' 
a Recipe is a map of:
- "url" => str
- "title" => str, name of Recipe
    - e.g. "Matthew's Lasagna"
- "info" => List of 2-Tuple of str 
    - e.g. [("prep", "10 minutes"), ...]
- "ingredients" => List of Ingredient
- "directions" => List of str
- "nutrition" => str
- "steps" => List of List of str
    - Each sub List of str corresponds to matching direction
    - e.g. Heat oil in a skillet; cook tofu until browned, 5 min. Transfer tofu to a plate.
        => [..., ["Heat oil in a skillet;", "cook tofu until browned, 5 min", "Transfer tofu to a plate."], ...]
- "methods" => is a Map
    - "master" => List of str (each method used)
    - "steps" => List of List of ???
- "tools" => is a Map
    - "master" => List of str (each tool used)
    - "steps" => List of List of ???
- "processed_directions" =>
    - unsure how to tackle this but it needs to know all the methods, tools, etc. 
      used in each step and direction


"Drop your chicken nuggies in hot oil and fry for 10 minutes"
[deep fryer]
=> changing our tool to [air fryer]
What we want is "Place your chicken nuggies in air fryer for XX minutes"
How do we get there?

"Place [INGREDIENT] in air fryer for [TIME]"


"Drop your chicken nuggies in hot oil and fry for 10 minutes"
ingredients: chicken nuggies, oil
methods: deep frying
tools: deep fryer
time: 10 minutes
"Deep fry chicken nuggies and oil in deep fryer for 10 minutes"
ACTION your INGREDIENTS for TIME
ACTION your CORE INGREDIENTS with SIDE INGREDIENTS (e.g. salt) for TIME

-----

"Stir the batter until right consistency"
[bowl, spoon]
=> changing our tool to [microwave]

How to tackle this? Do we need logic to change methods when tools are changed, and vice versa?
Or, can we keep it simple, and relate "spoon" to "Stir" to make changes later



'''