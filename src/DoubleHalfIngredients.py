

def doubleHalfIngredients(recipe, double):
    ingredients = recipe['ingredients']
    m = .5
    if double:
        m = 2
    
    for i, ing in enumerate(ingredients):
        ing.quantity = round(m * ing.quantity, 1)
        if ing.quantity % 1 == 0:
            ing.original_string = str(int(ing.quantity)) + ' '
        else:
            ing.original_string = str(ing.quantity) + ' '
        
        ing.original_string += ing.unit
        if ing.quantity > 1.0:
            ing.original_string += 's '
        
        ing.original_string += ing.name

        if len(ing.comment) > 0:
            ing.original_string += ', ' + ing.comment

        ingredients[i] = ing
    recipe['ingrients'] = ingredients
    
    return recipe
        
