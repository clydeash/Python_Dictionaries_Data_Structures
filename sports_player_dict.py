sports_players = {
    "Basketball": "Michael Jordan",
    "Soccer": "Lionel Messi",
    "Baseball": "Babe Ruth",
    "Tennis": "Roger Federer",
    "Cricket": "Sachin Tendulkar",
    "Golf": "Tiger Woods",
    "American Football": "Tom Brady",
    "Boxing": "Muhammad Ali",
    "Formula 1": "Lewis Hamilton",
    "Swimming": "Michael Phelps"
}

print("a. Entire dictionary:", sports_players)

print("b. Player of the 4th sport:", sports_players["Tennis"])

sports_players["Golf"] = "Jack Nicklaus"

del sports_players["Swimming"]

print("c. Updated dictionary:", sports_players)

last_key = list(sports_players.keys())[-1]
last_value = sports_players[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)