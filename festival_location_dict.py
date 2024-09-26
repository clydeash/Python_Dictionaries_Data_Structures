festivals_locations = {
    "Oktoberfest": "Munich, Germany",
    "Chinese New Year": "China",
    "Burning Man": "Black Rock Desert, Nevada, USA",
    "Cannes Film Festival": "Cannes, France",
    "Tokyo International Film Festival": "Tokyo, Japan",
    "Edinburgh International Festival": "Edinburgh, Scotland",
    "SXSW": "Austin, Texas, USA",
    "Berlin International Film Festival": "Berlin, Germany" 
}

print("a. Entire dictionary:", festivals_locations)

print("b. Location of the 4th festival:", festivals_locations["Cannes Film Festival"])

festivals_locations["Edinburgh International Festival"] = "Edinburgh, Scotland, UK"

del festivals_locations["Chinese New Year"]

print("c. Updated dictionary:", festivals_locations)

last_key = list(festivals_locations.keys())[-1]
last_value = festivals_locations[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)