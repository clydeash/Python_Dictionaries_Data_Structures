states_capitals = {
    "California": "Sacramento",
    "Texas": "Austin",
    "Florida": "Tallahassee",
    "New York": "Albany",
    "Illinois": "Springfield",
    "Pennsylvania": "Harrisburg",
    "Ohio": "Columbus",
    "Georgia": "Atlanta",
    "North Carolina": "Raleigh",
    "Michigan": "Lansing"
}

print("a. Entire dictionary:", states_capitals)

print("b. Capital of the 4th state:", states_capitals["Illinois"])

states_capitals["North Carolina"] = "Charlotte"

del states_capitals["Ohio"]

print("c. Updated dictionary:", states_capitals)

last_key = list(states_capitals.keys())[-1]
last_value = states_capitals[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)