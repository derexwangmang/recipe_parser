UNHEALTHY_MAPPING = {"oil": "corn oil", "butter": "vegetable oil"}
HEALTHY_MAPPING = {"oil": "avocado oil", "butter": "coconut oil"}

CARBS = set(["noodles", "rice", "tofu", "pasta", "crackers", "flour"])
FLAVORS = set(["salt", "sugar", "sauce"])

# Transforms steps into unhealthy version by
#   - Replacing oils with unhealthy versions
#   - Doubling carb amounts
#   - Quadrupling flavors (which are often heavily salted or processed)
# Expected argument is Recipe
def transform_unhealthy(recipe):
    for i in range(len(recipe.steps)):
        ingredient = recipe.steps[i].ingredient
        # Replace oil with unhealthy
        for oil in UNHEALTHY_MAPPING:
            if oil in ingredient.name:
                ingredient.name = UNHEALTHY_MAPPING[oil]
                break
        
        # If ingredient contains carbs, double it
        if set.intersection(set(ingredient.name.split()), CARBS):
            ingredient.quantity = ingredient.quantity * 2

        # If ingredient contains FLAVORS, quadruple it
        elif set.intersection(set(ingredient.name.split()), FLAVORS):
            ingredient.quantity = ingredient.quantity * 4



# Transforms steps into healthy version by replacing healthy ingredients with unhealthy ingredients
# Expected argument is Recipe
def transform_unhealthy(recipe):
    pass