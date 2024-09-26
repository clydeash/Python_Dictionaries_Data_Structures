cities_landmarks = {
    "Paris": "Eiffel Tower",
    "Rome": "Colosseum",
    "London": "Big Ben",
    "New York City": "Statue of Liberty",
    "Tokyo": "Tokyo Skytree",
    "Sydney": "Sydney Opera House",
    "Rio de Janeiro": "Christ the Redeemer",
    "Dubai": "Burj Khalifa"
}

print("a. Entire dictionary:", cities_landmarks)

print("b. Landmark of the 6th city:", cities_landmarks["Sydney"])

cities_landmarks["Rome"] = "Trevi Fountain"

del cities_landmarks["Rio de Janeiro"]

print("c. Updated dictionary:", cities_landmarks)

last_key = list(cities_landmarks.keys())[-1]
last_value = cities_landmarks[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)