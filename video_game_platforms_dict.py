games = {
    "The Legend of Zelda: Breath of the Wild": "Nintendo Switch",
    "Grand Theft Auto V": "PC, PlayStation 3, PlayStation 4, Xbox 360, Xbox One",
    "Minecraft": "PC, PlayStation 3, PlayStation 4, Xbox 360, Xbox One, Nintendo Switch, iOS, Android",
    "Mario Kart 8 Deluxe": "Nintendo Switch",
    "Super Mario Odyssey": "Nintendo Switch",
    "Red Dead Redemption 2": "PC, PlayStation 4, Xbox One",
    "Fortnite": "PC, PlayStation 4, Xbox One, Nintendo Switch, iOS, Android",
    "Call of Duty: Modern Warfare": "PC, PlayStation 4, Xbox One"
}

print("a. Entire dictionary:", games)

print("b. Platform of the 2nd video game:", games["Grand Theft Auto V"])

games["Red Dead Redemption 2"] = "PC, PlayStation 4, Xbox One, Google Stadia"

del games["Mario Kart 8 Deluxe"]

print("c. Updated dictionary:", games)

last_key = list(games.keys())[-1]
last_value = games[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)