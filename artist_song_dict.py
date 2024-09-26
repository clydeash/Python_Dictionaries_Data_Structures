artists = {
    "Taylor Swift": "All Too Well (10 Minute Version)",
    "Drake": "God's Plan",
    "The Weeknd": "Blinding Lights",
    "Beyoncé": "Single Ladies (Put a Ring on It)",
    "Ed Sheeran": "Shape of You",
    "BTS": "Dynamite",
    "Billie Eilish": "Bad Guy",
    "Justin Bieber": "Baby"
}

print("a. Entire dictionary:", artists)

print("b. Top song of the 3rd artist:", artists["The Weeknd"])

artists["BTS"] = "Butter"

del artists["Billie Eilish"]

print("c. Updated dictionary:", artists)

last_key = list(artists.keys())[-1]
last_value = artists[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)