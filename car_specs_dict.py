cars = {
    "Toyota Camry": "2.5L 4-cylinder engine",
    "Honda Civic": "1.5L 4-cylinder engine",
    "Ford Mustang": "5.0L V8 engine",
    "Tesla Model 3": "Electric motor",
    "Chevrolet Corvette": "6.2L V8 engine",
    "BMW 3 Series": "2.0L 4-cylinder engine",
    "Audi A4": "2.0L 4-cylinder engine",
    "Mercedes-Benz C-Class": "2.0L 4-cylinder engine",
    "Porsche 911": "3.0L 6-cylinder engine",
    "Subaru Impreza": "2.0L 4-cylinder engine"
}

print("a. Entire dictionary:", cars)

print("b. Specifications of the 4th car model:", cars["Tesla Model 3"])

cars["Porsche 911"] = "3.8L 6-cylinder engine"

del cars["Chevrolet Corvette"]

print("c. Updated dictionary:", cars)

last_key = list(cars.keys())[-1]
last_value = cars[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)