rivers_lengths = {
    "Amazon River": 6992,
    "Nile River": 6650,
    "Yangtze River": 6300,
    "Mississippi River": 3730,
    "Yenisei River": 5539,
    "Ob River": 5410
}

print("a. Entire dictionary:", rivers_lengths)

print("b. Length of the 2nd river:", rivers_lengths["Nile River"])

rivers_lengths["Yenisei River"] = 5550  

del rivers_lengths["Mississippi River"] 

print("c. Updated dictionary:", rivers_lengths)

last_key = list(rivers_lengths.keys())[-1]
last_value = rivers_lengths[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)