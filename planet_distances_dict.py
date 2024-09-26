planets = {
    "Mercury": 57.9,
    "Venus": 108.2,
    "Earth": 149.6,
    "Mars": 227.9,
    "Jupiter": 778.5,
    "Saturn": 1434.0,
    "Uranus": 2871.0,
    "Neptune": 4495.0
}

print("a. Entire dictionary:", planets)

print("b. Distance of the 3rd planet:", planets["Earth"])

planets["Jupiter"] = 778.3 

del planets["Uranus"]

print("c. Updated dictionary:", planets)

last_key = list(planets.keys())[-1]
last_value = planets[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)