animal_sounds = {
    "Lion": "Roar",
    "Elephant": "Trumpet",
    "Dog": "Bark",
    "Cat": "Meow",
    "Bird": "Chirp",
    "Cow": "Moo",
    "Snake": "Hiss",
    "Frog": "Croak"
}

print("Entire dictionary:", animal_sounds)

print("Sound of the 4th animal:", animal_sounds["Cat"])

animal_sounds["Snake"] = "Hiss Hiss"

del animal_sounds["Bird"]

print("Updated dictionary:", animal_sounds)

last_key = list(animal_sounds.keys())[-1]
last_value = animal_sounds[last_key]
print("Last key-value pair:", last_key, last_value)