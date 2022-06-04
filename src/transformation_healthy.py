UNHEALTHY_MAPPING = {"oil": "corn oil", "butter": "vegetable oil"}
HEALTHY_MAPPING = {"oil": "avocado oil", "butter": "coconut oil"}

CARBS = set(["noodles", "rice", "tofu", "pasta", "crackers", "flour"])
FLAVORS = set(["salt", "sugar", "sauce"])

from dataclasses import dataclass

@dataclass
class Ingredient:
    name : str
    quantity : int
    unit : str
    comment : str
    original_string : str

# Transforms steps into version by
#   - Replacing oils with healthy/unhealthy versions
#   - Doubling/halving carb amounts
#   - Quadrupling/halving flavors
# Expected arguments:
#   - recipe: Recipe
#   - health: 0 (unhealthy), 1 (healthy)
def transform(recipe, health):
    for ingredient in recipe['ingredients']:
        if health == 0:
            # Replace oil with unhealthy
            for oil in UNHEALTHY_MAPPING:
                if oil in ingredient.name.lower():
                    ingredient.name = UNHEALTHY_MAPPING[oil]
                    break
        else:
            # Replace oil with healthy
            for oil in HEALTHY_MAPPING:
                if oil in ingredient.name.lower():
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

# Checking unhealthy
recipe = {'url': '', 'title': '', 'info': '', 'ingredients': [Ingredient(name='Salt', quantity=1.0, unit='cup', comment='', original_string='1 cup of salt'), Ingredient(name='granola oil', quantity=1.0, unit='oz', comment='', original_string='1 cup of salt')], 'methods': [], 'tools': []}
print(recipe)
transform(recipe, 0)
print(recipe)

# Checking healthy
recipe = {'url': '', 'title': '', 'info': '', 'ingredients': [Ingredient(name='Salt', quantity=1.0, unit='cup', comment='', original_string='1 cup of salt'), Ingredient(name='granola oil', quantity=1.0, unit='oz', comment='', original_string='1 cup of salt')], 'methods': [], 'tools': []}
print(recipe)
transform(recipe, 1)
print(recipe)