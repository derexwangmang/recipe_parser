from FetchRecipe import fetchRecipe

TO_VEG = {'ground beef':'crumbled tofu', 'beef':'tofu', 'hamburger':'black bean veggie hamburger', 'chicken':'tempeh', 
'bacon':'tempeh', 'duck':'seitan', 'steak':'king oyster mushroom', 'sausage':'vegetarian sausage', 'pork':'jackfruit', 
'shrimp':'king oyster mushroom', 'oyster sauce': 'soy sauce', 'fish sauce': 'tamari'
}

TO_MEAT = {'tofu': "chicken", 'tempeh': 'bacon', 'seitan':'duck', 
'jackfruit':'pork', 'black bean burger':'hamburger'}

def transform_vegetarian(recipe, switch):
    swapdict = None
    if switch == 'to vegetarian':
        swapdict = TO_VEG
    elif switch == 'to non-vegetarian':
        swapdict = TO_MEAT
    ingredients = recipe['ingredients']
    newingredients = []
    newmethods = []
    methods = recipe['methods']
    swapped = {}

    ## changing ingredients
    for i in range(len(ingredients)):
        ingredient = ingredients[i]
        # plural = False
        subbed = False
        name = ingredient.name
        # if name[-1] == 's':
        #     plural = True
        for option in swapdict.keys():
            if option in name:
                # print(name, "FOUND IN DICTIONARY")
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
        newingredients.append(ingredients[i])

    recipe['ingredients'] = newingredients

    ## changing methods
    for method in methods:
        direction = method.direction
        changed = False
        # print(direction)
        for original in swapped.keys():
            swap = swapped.get(original)
            if original in direction:
                changed = True
                newdirection = direction.replace(original, swap)
        if changed == True:
            method.direction = newdirection
        newmethods.append(method)
        print(method.direction)
            
    recipe['methods'] = newmethods
    return recipe

recipe = fetchRecipe('https://www.allrecipes.com/recipe/244716/shirataki-meatless-meat-pad-thai/')
transform_vegetarian(recipe, 'to non-vegetarian')