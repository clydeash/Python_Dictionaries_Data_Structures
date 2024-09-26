historical_events = {
    "World War I": 1914,
    "World War II": 1939,
    "The Great Depression": 1929,
    "The French Revolution": 1789,
    "The American Revolution": 1775,
    "The Renaissance": 1300,
    "The Industrial Revolution": 1760,
    "The Fall of the Berlin Wall": 1989
}

print("a. Entire dictionary:", historical_events)

print("b. Year of the 2nd event:", historical_events["World War II"])

historical_events["The Industrial Revolution"] = 1750

del historical_events["The American Revolution"]

print("c. Updated dictionary:", historical_events)

last_key = list(historical_events.keys())[-1]
last_value = historical_events[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)