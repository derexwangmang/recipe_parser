# from src.FetchRecipe import fetchRecipe

TO_VEG = {'ground beef':'crumbled tofu', 'beef':'tofu', 'hamburger':'black bean veggie hamburger', 'chicken':'tempeh', 
'bacon':'tempeh', 'duck':'seitan', 'steak':'king oyster mushroom', 'sausage':'vegetarian sausage', 'pork':'jackfruit', 
'shrimp':'king oyster mushroom', 'oyster sauce': 'soy sauce', 'fish sauce': 'tamari'
}

TO_MEAT = {'tofu': "chicken", 'tempeh': 'bacon', 'seitan':'duck', 
'jackfruit':'pork', 'black bean burger':'hamburger'}

def transform_vegetarian(recipe, switch):
    swapdict = None
    if switch == 'vegetarian':
        swapdict = TO_VEG
    elif switch == 'non-vegetarian':
        swapdict = TO_MEAT
    ingredients = recipe['ingredients']
    methods = recipe['methods']
    swapped = {}

    ## changing ingredients
    for i in range(len(ingredients)):
        ingredient = ingredients[i]
        # plural = False
        subbed = False
        name = ingredient.name

        print(swapdict.keys())
        for option in swapdict.keys():
            if option in name:
                subbed = True
                sub = swapdict.get(option)
                swapped[option] = sub
                break
                # print('SUBSTITUTE IS: ', sub)
                # if plural == True:
                    # sub += 's'
        if subbed == True:
            ingredients[i].name = sub
            ingredients[i].original_string = ingredients[i].original_string.replace(name,sub,1)

    ## changing methods
    for original in swapped.keys():
        swap = swapped.get(original)

        for method in methods:
            direction = method.direction
            changed = False
            if original in direction:
                # print("SWAP FOUND BETWEEN ", original, "and", swap)
                changed = True
                newdirection = direction.replace(original, swap)
            if changed == True:
                method.direction = newdirection

    return recipe

# recipe = fetchRecipe('https://www.allrecipes.com/recipe/244716/shirataki-meatless-meat-pad-thai/')
# transform_vegetarian(recipe, 'to non-vegetarian')