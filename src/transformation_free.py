# from src.FetchRecipe import fetchRecipe

LACTOSE_FREE = {'heavy cream':'coconut cream', 'heavy whipping cream':'coconut cream','mozzarella':'lactose-free mozarella',
'provolone':'lactose-free provolone', 'goat cheese':'cashew cheese', 'cream cheese':'cashew cream cheese',
'ricotta cheese':'silken tofu', 'whipping cream': 'coconut cream', 'milk chocolate':'dark chocolate', 'milk':'oat milk',
'yogurt': 'pureed silken tofu', 'butter':'margarine', 'mascarpone cheese':'lactose-free mascarpone cheese', 'lady fingers': 'gluten-free lady fingers'
}

GLUTEN_FREE = {'linguine':'chickpea linguine', 'spaghetti':'chickpea spaghetti',
'macaroni':'chickpea macaroni', 'penne':'chickpea penne', 'rotini':'chickpea rotini', 'fettuccine':'chickpea fettuccine', 
'farfalle':'chickpea farfalle', 'rigatoni':'chickpea rigatoni', 'whole wheat tortilla':'almond flour tortilla',
'tortilla':'almond flour tortilla', 'bread':'gluten-free bread',
'lasagna':'chickpea lasagna',
'pasta': 'chickpea pasta'
 }

def transform_free(recipe, switch):
    swapdict = None
    if switch == 'lactose-free':
        swapdict = LACTOSE_FREE
    elif switch == 'gluten-free':
        swapdict = GLUTEN_FREE
    ingredients = recipe['ingredients']
    methods = recipe['methods']
    swapped = {}

    ## changing ingredients
    for i in range(len(ingredients)):
        ingredient = ingredients[i]
        plural = False
        subbed = False
        name = ingredient.name
        if name[-1] == 's':
            plural = True
        for option in swapdict.keys():
            if option in name:
                # print(name, "FOUND IN DICTIONARY")
                subbed = True
                sub = swapdict.get(option)
                swapped[option] = sub
                
                # print('SUBSTITUTE IS: ', sub)
                if plural == True:
                    sub += 's'
                break
        if subbed == True:
            ingredients[i].name = sub
            ingredients[i].original_string = ingredients[i].original_string.replace(name,sub,1)

    ## changing methods
    for original in swapped.keys():
        splt = original.split()
        if splt[-1] == 'cheese':
            # print("LAST WORD WAS CHEESE FOR", original)
            neworiginal = " ".join(splt[:-1])
            # print("NEW WORD IS ", neworiginal)
        else:
            neworiginal = original
        swap = swapped.get(original)

        for method in methods:
            direction = method.direction
            changed = False
            if original in direction:
                # print("SWAP FOUND BETWEEN ", original, "and", swap)
                changed = True
                newdirection = direction.replace(original, swap)
                # print('THE NEW DIRECTION IS ', newdirection)
            elif neworiginal in direction:
                # print("SWAP FOUND BETWEEN ", neworiginal, "and", swap)
                changed = True
                newdirection = direction.replace(neworiginal, swap)
            if changed == True:
                method.direction = newdirection

    return recipe

# recipe = fetchRecipe('https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/')
# transform_free(recipe, 'lactose-free')