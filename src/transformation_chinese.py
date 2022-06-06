import random


CN_SWAPS = {"salt": "soy sauce", "white vinegar": "black vinegar", "red pepper": "chili oil", 
"chili flakes": "sichaun peppercorns", "olive oil": "sesame oil", "vegetable oil": "sesame oil", "oil": "sesame oil",
"oyster sauce": "hoisin sauce", "rice": "jasmine rice", "bell pepper": "latern pepper", "pepper": "sichaun pepper",
"cabbage": "napa cabbage", "celery": "chinese celery", "broccoli":"chinese broccoli", "bean sprout": "mung bean sprout",
"leek": "chinese leek", "radish": "chinese white radish", "eggplant" : "chinese eggplant", "mushroom": "cloud ear"}

CN_SEASONING = ["green onion", "ginger", "chili powder", "five spice powder"]

CN_VEGETABLES = ["bamboo shoots", "bitter melon", "bok choy", "silk squash", "pea shoots", "chrysanthemum", "yam leaves",
"yu choy", "watercress"]

VEGETABLES = ["cucumber","carrot","capsicum","raddish","beetroot","lettuce","spinach","cauliflower","bell pepper",
"turnip","corn","jalepeño","pease","broccoli", "celery"]

OTHER_TOOLS = ["skillet", "frying pan", "sauce pan", "pot", "saucepan", "pan"]

PRIMARY_COOKING = {'saute': 'stir fry', 'pan fry': 'stir fry', 'poach': 'steam', 'broil': 'steam', 'deep fry': 'stir fry', 'fry': 'stir fry'}



def transformation_chinese(recipe):
    ingredients = recipe['ingredients']
    methods = recipe['methods']
    tools = recipe['tools']
    swapped = {}

    ## changing ingredients
    for i in range(len(ingredients)):
        ingredient = ingredients[i]
        # plural = False
        subbed = False
        name = ingredient.name
        #print(ingredient)

        #print(swapdict.keys())
        for option in CN_SWAPS.keys():
            if option in name:
                subbed = True
                sub = CN_SWAPS.get(option)
                swapped[name] = [sub, option]
                break
                # print('SUBSTITUTE IS: ', sub)
                # if plural == True:
                    # sub += 's'
        if subbed == True:
            ingredients[i].name = sub
            ingredients[i].original_string = ingredients[i].original_string.replace(name,sub,1)
        else:
            for veg in VEGETABLES:
                if veg in name:
                    replacement = random.choice(CN_VEGETABLES)
                    ingredients[i].name = replacement
                    ingredients[i].original_string = ingredients[i].original_string.replace(name,replacement,1)
                    swapped[name] = [replacement, veg]
                    break

    ## changing tools
    for i in range(len(tools)):
        tool = tools[i]
        for j in OTHER_TOOLS:
            if j in tool:
                #swapped[j] = ["wok", tool]
                tools[i] = tools[i].replace(j,"wok",1)
                break

    print(swapped)
    ## changing methods
    for original in swapped.keys():
        swap = swapped.get(original)

        for method in methods:
            direction = method.direction
            changed = False
            if original in direction:
                #print("SWAP FOUND BETWEEN ", original, "and", swap)
                changed = True
                direction = direction.replace(original, swap[0])
            elif swap[1] in direction:
                #print("SWAP FOUND BETWEEN ", original, "and", swap)
                changed = True
                direction = direction.replace(swap[1], swap[0])

            for ctool in OTHER_TOOLS:
                changed = True
                if ctool in direction:
                    direction = direction.replace(ctool, "wok")

            for cooking in PRIMARY_COOKING.keys():
                changed = True
                if cooking in direction:
                    direction = direction.replace(cooking,PRIMARY_COOKING[cooking])
            if changed == True:
                method.direction = direction

    return recipe
