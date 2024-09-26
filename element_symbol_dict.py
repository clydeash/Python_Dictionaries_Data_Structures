elements = {
    "Hydrogen": "H",
    "Helium": "He",
    "Lithium": "Li",
    "Beryllium": "Be",
    "Boron": "B",
    "Carbon": "C",
    "Nitrogen": "N",
    "Oxygen": "O",
    "Fluorine": "F",
    "Neon": "Ne"
}

print("a. Entire dictionary:", elements)

print("b. Symbol of the 6th element:", elements["Carbon"])

elements["Oxygen"] = "Ox"  # Updating the symbol of the 8th element

del elements["Fluorine"]  # Deleting the 9th element

print("c. Updated dictionary:", elements)

last_key = list(elements.keys())[-1]
last_value = elements[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)