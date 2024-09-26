flower_meanings = {
    "Rose": "Love, passion, beauty",
    "Lily": "Purity, innocence, rebirth",
    "Sunflower": "Happiness, longevity, adoration",
    "Daisy": "Innocence, purity, loyal love",
    "Tulip": "Perfect love, declaration of love, fame",
    "Carnation": "Fascination, motherly love, admiration",
    "Hydrangea": "Thankfulness for understanding, heartfelt emotions",
    "Orchid": "Love, beauty, refinement, luxury" 
}

print("a. Entire dictionary:", flower_meanings) 

print("b. Meaning of the 5th flower:", flower_meanings["Tulip"])

flower_meanings["Hydrangea"] = "Gratitude, abundance, understanding" 

del flower_meanings["Carnation"]

print("c. Updated dictionary:", flower_meanings)

last_key = list(flower_meanings.keys())[-1]
last_value = flower_meanings[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)