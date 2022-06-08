UNHEALTHY_MAPPING = {"oil": "corn oil", "butter": "vegetable oil"}
HEALTHY_MAPPING = {"oil": "avocado oil", "butter": "coconut oil"}

CARBS = set(["noodles", "rice", "tofu", "pasta", "crackers", "flour"])
FLAVORS = set(["salt", "sugar", "sauce"])

# Transforms steps into version by
#   - Replacing oils with healthy/unhealthy versions
#   - Doubling/halving carb amounts
#   - Quadrupling/halving flavors
# Expected arguments:
#   - recipe: Recipe
#   - health: 0 (unhealthy), 1 (healthy)
def transform_healthy(recipe, health):
    replaced_ingredients = {}
    ### health == 0 means unhealthy, health == 1 means healthy
    for ingredient in recipe['ingredients']:
        if health == 0:
            # Replace oil with unhealthy
            for oil in UNHEALTHY_MAPPING.keys():
                if oil in ingredient.name.lower():
                    replaced_ingredients[ingredient.name] = UNHEALTHY_MAPPING[oil]
                    ingredient.name = UNHEALTHY_MAPPING[oil]
                    break
        else:
            # Replace oil with healthy
            for oil in HEALTHY_MAPPING:
                if oil in ingredient.name.lower():
                    replaced_ingredients[ingredient.name] = HEALTHY_MAPPING[oil]
                    ingredient.name = HEALTHY_MAPPING[oil]
                    break
        
        # Double/half carbs
        if set.intersection(set(ingredient.name.lower().split()), CARBS):
            if health == 0:
                ingredient.quantity = ingredient.quantity * 2
            else:
                ingredient.quantity = ingredient.quantity / 2
        
        # Quadruple/half flavors
        if set.intersection(set(ingredient.name.lower().split()), FLAVORS):
            if health == 0:
                ingredient.quantity = ingredient.quantity * 4
            else:
                ingredient.quantity = ingredient.quantity / 2

    # print(replaced_ingredients)
    for i in range(len(recipe['steps'])):
        for j, step in enumerate(recipe['steps'][i]):
            for replaced in replaced_ingredients.keys():
                # print('replaced={}'.format(replaced))
                if 'oil' in replaced:
                    # print("STEP={}, looking for={}".format(step, replaced))
                    # See if full name of oil is in step
                    if replaced in step:
                        # print('67')
                        recipe['steps'][i][j] = step.replace(replaced, replaced_ingredients[replaced])
                    # Assume that only 'oil' is in step
                    else:
                        recipe['steps'][i][j] = step.replace('oil', replaced_ingredients[replaced])

                elif 'butter' in replaced:
                    # print('73')
                    recipe['steps'][i][j] = step.replace('butter', replaced_ingredients[replaced])

    return recipe

# # Checking unhealthy
# recipe = {'url': '', 'title': '', 'info': '', 'ingredients': [Ingredient(name='Salt', quantity=1.0, unit='cup', comment='', original_string='1 cup of salt'), Ingredient(name='olive oil', quantity=1.0, unit='oz', comment='', original_string='1 cup of salt'), Ingredient(name='butter', quantity=1.0, unit='stick', comment='', original_string='1 stick of butter')], 'steps': [['Heat oil in skillet', 'Heat olive oil in a large skillet over medium-high heat.', 'Microwave butter.']],'methods': [], 'tools': []}
# print(recipe)
# transform_healthy(recipe, 0)
# print(recipe)

# # Checking healthy
# recipe = {'url': '', 'title': '', 'info': '', 'ingredients': [Ingredient(name='Salt', quantity=1.0, unit='cup', comment='', original_string='1 cup of salt'), Ingredient(name='olive oil', quantity=1.0, unit='oz', comment='', original_string='1 cup of salt'), Ingredient(name='butter', quantity=1.0, unit='stick', comment='', original_string='1 stick of butter')], 'steps': [['Heat oil in skillet', 'Heat olive oil in a large skillet over medium-high heat.', 'Microwave butter.']],'methods': [], 'tools': []}
# print(recipe)
# transform_healthy(recipe, 1)
# print(recipe)