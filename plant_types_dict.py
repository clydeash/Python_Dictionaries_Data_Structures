plants = {
    "Rose": "Shrub",
    "Oak": "Tree",
    "Basil": "Herb",
    "Fern": "Fern",
    "Sunflower": "Flower",
    "Cactus": "Cactus",
    "Lavender": "Herb",
    "Palm": "Tree"
}

print("a. Entire dictionary:", plants)

print("b. Type of the 5th plant:", plants["Sunflower"])

plants["Oak"] = "Shrub"

del plants["Cactus"]

print("c. Updated dictionary:", plants)

last_key = list(plants.keys())[-1]
last_value = plants[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)