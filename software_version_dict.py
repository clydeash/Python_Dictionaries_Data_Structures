software = {
    "Microsoft Word": "16.78",
    "Adobe Photoshop": "24.4.1",
    "Google Chrome": "116.0.5845.110",
    "Microsoft Excel": "16.78",
    "Zoom": "5.13.5",
    "Spotify": "1.2.72.958"
}

print("a. Entire dictionary:", software)

print("b. Version of the 4th software:", software["Microsoft Excel"])

software["Adobe Photoshop"] = "24.4.2" 

del software["Zoom"]

print("c. Updated dictionary:", software)

last_key = list(software.keys())[-1]
last_value = software[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)