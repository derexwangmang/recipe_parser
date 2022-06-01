




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