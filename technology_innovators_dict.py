technologies_innovators = {
    "Telephone": "Alexander Graham Bell",
    "Light Bulb": "Thomas Edison",
    "Computer": "Charles Babbage",
    "Internet": "Vinton Cerf and Robert Kahn",
    "World Wide Web": "Tim Berners-Lee",
    "Smartphone": "Martin Cooper",
    "Electric Car": "Robert Anderson",
    "Personal Computer": "Apple Inc. (Steve Jobs, Steve Wozniak, Ronald Wayne)"
}

print("a. Entire dictionary:", technologies_innovators)

print("b. Innovator of the 4th technology:", technologies_innovators["Internet"])

technologies_innovators["Light Bulb"] = "Joseph Swan"

del technologies_innovators["Smartphone"]

print("c. Updated dictionary:", technologies_innovators)

last_key = list(technologies_innovators.keys())[-1]
last_value = technologies_innovators[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)