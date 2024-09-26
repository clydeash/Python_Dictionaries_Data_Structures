country_capitals = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Brazil": "Brasília",
    "Argentina": "Buenos Aires",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "China": "Beijing",
    "India": "New Delhi",
    "Australia": "Canberra",
    "United Kingdom": "London"
}

print("a. Entire dictionary:", country_capitals)

print("b. Capital of the 5th country:", country_capitals["Argentina"])

country_capitals["Japan"] = "Kyoto" 

del country_capitals["Australia"]

print("c. Updated dictionary:", country_capitals)

last_key = list(country_capitals.keys())[-1]
last_value = country_capitals[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)