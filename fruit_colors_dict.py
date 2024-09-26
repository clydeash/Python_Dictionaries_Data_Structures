fruit_colors = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Orange": "Orange",
    "Grape": "Purple",
    "Strawberry": "Red",
    "Blueberry": "Blue",
    "Mango": "Yellow",
    "Watermelon": "Red"
}

print("a. Entire dictionary:", fruit_colors)

print("b. Color of the 6th fruit:", fruit_colors["Blueberry"])

fruit_colors["Grape"] = "Green"

del fruit_colors["Mango"]

print("c. Updated dictionary:", fruit_colors)

last_key = list(fruit_colors.keys())[-1]
last_value = fruit_colors[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)