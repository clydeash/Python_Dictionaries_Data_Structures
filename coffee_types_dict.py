coffee_types = {
    "Espresso": "A strong, concentrated coffee brewed by forcing hot water through finely-ground coffee beans under pressure.",
    "Cappuccino": "A coffee drink made with espresso, steamed milk, and a layer of foamed milk.",
    "Latte": "A coffee drink made with espresso and steamed milk, typically with a thin layer of foam.",
    "Americano": "A coffee drink made with espresso diluted with hot water.",
    "Mocha": "A coffee drink made with espresso, chocolate, and steamed milk.",
    "Macchiato": "A coffee drink made with espresso and a small amount of steamed or foamed milk.",
    "Flat White": "A coffee drink made with espresso and steamed milk, with a thinner layer of foam than a latte.",
    "Cold Brew": "A coffee concentrate made by steeping coarsely ground coffee beans in cold water for an extended period of time.",
    "Iced Coffee": "Brewed coffee that is served chilled over ice.",
    "Frappuccino": "A blended iced coffee drink made with coffee, ice, milk, and various flavorings."
}

print("a. Entire dictionary:", coffee_types)

print("b. Description of the 4th type of coffee:", coffee_types["Americano"])

coffee_types["Cold Brew"] = "A smooth, low-acidity coffee concentrate made by steeping coarsely ground coffee beans in cold water for 12-24 hours."

del coffee_types["Macchiato"]

print("c. Updated dictionary:", coffee_types)

last_key = list(coffee_types.keys())[-1]
last_value = coffee_types[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)