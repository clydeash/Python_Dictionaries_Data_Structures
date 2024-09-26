technologies = {
    "World Wide Web": "Tim Berners-Lee",
    "Automobile": "Karl Benz",
    "Computer": "Charles Babbage",
    "Aeroplane": "Wright Brothers",
    "Electricity": "Thomas Edison", 
    "Radio": "Guglielmo Marconi"
}

print("a. Entire dictionary:", technologies)

print("b. Inventor of the 4th technology:", technologies["Aeroplane"])

technologies["World Wide Web"] = "Tim Berners-Lee and Robert Cailliau" 

del technologies["Radio"]

print("c. Updated dictionary:", technologies)

last_key = list(technologies.keys())[-1]
last_value = technologies[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)