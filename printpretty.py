from src.FetchRecipe import fetchRecipe
# from src.transformation_vegetarian import transform_vegetarian
from src.transformation_free import transform_free
from src.transformation_vegetarian import transform_vegetarian

class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def prettyprint(recipe, transformation):
    title = recipe["title"]
    ingredients = recipe['ingredients']
    methods = recipe['methods']
    tools = recipe['tools']

    ##print title
    print(color.BOLD + "Your Transformed Recipe: {t}, made {change}\n".format(
        t = title,
        change = transformation
    ) + color.END)

    ##print ingredients
    print(color.BOLD + "Ingredients: " + color.END)
    for ingredient in ingredients:
        name = ingredient.name
        quantity = str(ingredient.quantity)
        unit = str(ingredient.unit)
        comment = ingredient.comment
        string = quantity + ' ' + unit + ' ' + name + ', ' + comment
        print(string)
    
    ##print tools
    print(color.BOLD + "\nTools:" + color.END)
    for tool in tools:
        print(tool)

    ##print directions
    print(color.BOLD + "\nDirections:" + color.END)
    for i in range(len(methods)):
        direction = methods[i].direction
        if direction == '':
            break
        print(color.UNDERLINE + "Step {}:".format(i+1) + color.END)
        print(direction)
        print("\n")
    
    ## print thank you
    print(color.BOLD + "\nThank you for using our recipe parser and interactive cookbook!" + color.END)

# recipe = fetchRecipe('https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/')
# # newrecipe = transform_free(recipe, 'lactose-free')
# # prettyprint(newrecipe, 'lactose-free')

# newrecipe = transform_vegetarian(recipe, 'vegetarian')
# prettyprint(newrecipe, 'vegetarian')