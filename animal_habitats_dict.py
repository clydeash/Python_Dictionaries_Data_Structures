animal_habitats = {
    "Lion": "Savanna",
    "Elephant": "Savanna",
    "Tiger": "Rainforest",
    "Giraffe": "Savanna",
    "Polar Bear": "Arctic Tundra",
    "Monkey": "Rainforest",
    "Kangaroo": "Grassland",
    "Dolphin": "Ocean"
}

print("a. Entire dictionary:", animal_habitats)

print("b. Habitat of the 3rd animal:", animal_habitats["Tiger"])

animal_habitats["Polar Bear"] = "Arctic"

del animal_habitats["Kangaroo"]

print("c. Updated dictionary:", animal_habitats)

last_key = list(animal_habitats.keys())[-1]
last_value = animal_habitats[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)