space_missions = {
    "Apollo 11": 1969,
    "Voyager 1": 1977,
    "Hubble Space Telescope": 1990,
    "Mars Pathfinder": 1997,
    "SpaceX Falcon Heavy Test Flight": 2018 
}

print("a. Entire dictionary:", space_missions)

print("b. Year of the 3rd mission:", space_missions["Hubble Space Telescope"])

space_missions["Voyager 1"] = 1977  # Updating the year of the 2nd mission (already correct)

del space_missions["Mars Pathfinder"]  # Deleting the 4th mission

print("c. Updated dictionary:", space_missions)

last_key = list(space_missions.keys())[-1]
last_value = space_missions[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)