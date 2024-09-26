athletes = {
    "Usain Bolt": "World record holder in the 100m, 200m, and 4 × 100 m relay",
    "Michael Phelps": "Most Olympic gold medals (23)",
    "Serena Williams": "23 Grand Slam singles titles",
    "Lionel Messi": "7 Ballon d'Or awards (most in history)",
    "Cristiano Ronaldo": "5 Ballon d'Or awards",
    "Tiger Woods": "15 major championships in golf",
    "Roger Federer": "20 Grand Slam singles titles",
    "Simone Biles": "Most decorated gymnast in World Championship history"
}

print("a. Entire dictionary:", athletes)

print("b. Achievement of the 5th athlete:", athletes["Cristiano Ronaldo"])

athletes["Serena Williams"] = "23 Grand Slam singles titles and 14 Grand Slam doubles titles"

del athletes["Roger Federer"]

print("c. Updated dictionary:", athletes)

last_key = list(athletes.keys())[-1]
last_value = athletes[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)