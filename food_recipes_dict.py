foods_recipes = {
    "Pizza": "1. Preheat oven to 450°F (230°C). 2. Prepare dough and sauce. 3. Spread sauce on dough. 4. Add cheese and toppings. 5. Bake for 10-15 minutes.",
    "Spaghetti": "1. Cook spaghetti according to package directions. 2. Prepare meat sauce. 3. Drain spaghetti and toss with sauce.",
    "Chicken Soup": "1. Sauté onions, carrots, and celery. 2. Add chicken broth, chicken, and herbs. 3. Simmer for 30 minutes. 4. Add noodles and cook until tender.",
    "Tacos": "1. Heat tortillas. 2. Fill with meat, cheese, lettuce, and other toppings.",
    "Brownies": "1. Preheat oven to 350°F (175°C). 2. Combine dry ingredients. 3. Combine wet ingredients. 4. Mix together and bake for 25-30 minutes.",
    "Cookies": "1. Preheat oven to 375°F (190°C). 2. Cream together butter and sugar. 3. Add eggs and vanilla. 4. Mix in dry ingredients. 5. Drop by spoonfuls onto baking sheet. 6. Bake for 10-12 minutes.",
    "Salad": "1. Wash and chop lettuce. 2. Add vegetables, cheese, and dressing of your choice.",
    "Sandwich": "1. Spread bread with butter or mayonnaise. 2. Add meat, cheese, and vegetables. 3. Close the sandwich."
}

print("a. Entire dictionary:", foods_recipes)

print("b. Recipe of the 5th food:", foods_recipes["Brownies"])

foods_recipes["Chicken Soup"] = "1. Sauté onions, carrots, and celery. 2. Add chicken broth, chicken, and herbs. 3. Simmer for 30 minutes. 4. Add noodles, potatoes, and carrots. 5. Cook until vegetables are tender."

del foods_recipes["Salad"]

print("c. Updated dictionary:", foods_recipes)

last_key = list(foods_recipes.keys())[-1]
last_value = foods_recipes[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)