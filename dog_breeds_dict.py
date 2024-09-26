dog_breeds = {
    "Chihuahua": "small",
    "French Bulldog": "small",
    "Golden Retriever": "medium",
    "Labrador Retriever": "medium",
    "Pomeranian": "small",
    "German Shepherd": "large",
    "Beagle": "medium",
    "Rottweiler": "large",
    "Pug": "small",
    "Bulldog": "medium"
}

print("a. Entire dictionary:", dog_breeds)

print("b. Size of the 5th breed:", dog_breeds["Pomeranian"])

dog_breeds["Rottweiler"] = "large"

del dog_breeds["German Shepherd"]

print("c. Updated dictionary:", dog_breeds)

last_key = list(dog_breeds.keys())[-1]
last_value = dog_breeds[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)