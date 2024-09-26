sports_events = {
    "FIFA World Cup": 2026,
    "Summer Olympics": 2024,
    "UEFA Champions League": 2024,
    "Cricket World Cup": 2027,
    "Super Bowl": 2024,
    "Wimbledon": 2024,
    "Tour de France": 2024
}

print("a. Entire dictionary:", sports_events)

print("b. Year of the 3rd sports event:", sports_events["UEFA Champions League"])

sports_events["Wimbledon"] = 2025

del sports_events["Super Bowl"]

print("c. Updated dictionary:", sports_events)

last_key = list(sports_events.keys())[-1]
last_value = sports_events[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)