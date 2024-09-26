continents_countries = {
    "Africa": ["Egypt", "Nigeria", "South Africa"],
    "Asia": ["China", "India", "Japan"],
    "Europe": ["Germany", "France", "United Kingdom"],
    "North America": ["United States", "Canada", "Mexico"],
    "South America": ["Brazil", "Argentina", "Colombia"],
    "Australia": ["Australia", "New Zealand", "Papua New Guinea"]
}

print("a. Entire dictionary:", continents_countries)

print("b. Countries of the 4th continent:", continents_countries["North America"])

continents_countries["South America"] = ["Brazil", "Peru", "Chile"]

del continents_countries["Australia"]

print("c. Updated dictionary:", continents_countries)

last_key = list(continents_countries.keys())[-1]
last_value = continents_countries[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)