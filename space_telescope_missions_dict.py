space_telescopes = {
    "Hubble Space Telescope": "Observing distant galaxies and celestial objects",
    "Chandra X-ray Observatory": "Studying high-energy X-ray sources in the universe",
    "Spitzer Space Telescope": "Observing infrared radiation from celestial objects",
    "James Webb Space Telescope": "Observing the early universe and exoplanets",
    "Kepler Space Telescope": "Searching for exoplanets"
}

print("a. Entire dictionary:", space_telescopes)

print("b. Mission of the 3rd telescope:", space_telescopes["Spitzer Space Telescope"])

space_telescopes["Hubble Space Telescope"] = "Observing the universe in visible and ultraviolet light"

del space_telescopes["James Webb Space Telescope"]

print("c. Updated dictionary:", space_telescopes)

last_key = list(space_telescopes.keys())[-1]
last_value = space_telescopes[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)