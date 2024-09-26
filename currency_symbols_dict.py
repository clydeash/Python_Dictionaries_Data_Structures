currencies = {
    "US Dollar": "$",
    "Euro": "€",
    "Japanese Yen": "¥",
    "British Pound": "£",
    "Australian Dollar": "A$",
    "Canadian Dollar": "C$",
    "Swiss Franc": "CHF",
    "Indian Rupee": "₹",
    "Chinese Yuan": "¥",
    "Russian Ruble": "₽"
}

print("a. Entire dictionary:", currencies)

print("b. Symbol of the 5th currency:", currencies["Australian Dollar"])

currencies["Chinese Yuan"] = "元" 

del currencies["Japanese Yen"]

print("c. Updated dictionary:", currencies)

last_key = list(currencies.keys())[-1]
last_value = currencies[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)