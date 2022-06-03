print("Welcome to our recipe parser and interactive cookbook!")
print("Please provide the URL of a recipe from AllRecipes.com: ", end='')
url = str(input())

while not url.startswith("https://www.allrecipes.com/"):
    print("{} does not start with https://www.allrecipes.com/".format(url))
    print("Please provide the URL of a recipe from AllRecipes.com: ", end='')
    url = str(input())

print("Fetched from {}".format(url))
print("What would you like to do with the recipe?")
print("Option 1: To vegetarian")
print("Option 2: To non-vegetarian")
print("Option 3: To healthy")
print("Option 4: To non-healthy")
print("Option 5: To an additional style of cuisine")
print("Option 6: To an additional style of cuisine")
print("Option 7: Double the amount")
print("Option 8: Half the amount")
print("Input a number 1-8: ", end='')

option = input()
while not option.isdigit() or not 1 <= int(option) <= 8:
    print("{} not within 1-8".format(option))
    print("Input a number 1-8: ", end='')
    option = input()

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