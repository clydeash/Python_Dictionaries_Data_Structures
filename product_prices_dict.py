products = {
    "Laptop": 1200,
    "Smartphone": 800,
    "Headphones": 150,
    "Keyboard": 75,
    "Mouse": 30,
    "Monitor": 300,
    "Webcam": 50,
    "Printer": 100,
    "Tablet": 350,
    "Charger": 25
}

print("a. Entire dictionary:", products)

print("b. Price of the 4th product:", products["Keyboard"])

products["Tablet"] = 400

del products["Monitor"]

print("c. Updated dictionary:", products)

last_key = list(products.keys())[-1]
last_value = products[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)