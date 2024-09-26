city_population = {
    "New York": 8537673,
    "Los Angeles": 3979576,
    "Chicago": 2693976,
    "Houston": 2320268,
    "Phoenix": 1680992,
    "Philadelphia": 1584064,
    "San Antonio": 1547253,
    "San Diego": 1425976,
    "Dallas": 1343573,
    "San Jose": 1030119
}

print("a. Entire dictionary:", city_population)

print("b. Population of the 6th city:", city_population["Philadelphia"])

city_population["Chicago"] = 2716000

del city_population["San Diego"]

print("c. Updated dictionary:", city_population)

last_key = list(city_population.keys())[-1]
last_value = city_population[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)