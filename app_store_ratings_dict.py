app_ratings = {
    "Instagram": 4.5,
    "WhatsApp": 4.3,
    "TikTok": 4.2,
    "YouTube": 4.7,
    "Facebook": 3.8,
    "Twitter": 3.9,
    "Snapchat": 4.1,
    "Spotify": 4.6,
    "Netflix": 4.4,
    "Amazon Prime Video": 4.3
}

print("a. Entire dictionary:", app_ratings)

print("b. Rating of the 6th app:", app_ratings["Twitter"])

app_ratings["Spotify"] = 4.8

del app_ratings["Netflix"]

print("c. Updated dictionary:", app_ratings)

last_key = list(app_ratings.keys())[-1]
last_value = app_ratings[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)