car_brands = {
    "Toyota": "Japan",
    "Honda": "Japan",
    "Ford": "United States",
    "Chevrolet": "United States",
    "BMW": "Germany",
    "Mercedes-Benz": "Germany",
    "Volvo": "Sweden",
    "Audi": "Germany",
    "Volkswagen": "Germany",
    "Tesla": "United States" 
}

print("a. Entire dictionary:", car_brands)

print("b. Country of origin of the 3rd car brand:", car_brands["Ford"])

car_brands["Volvo"] = "China"

del car_brands["Audi"]

print("c. Updated dictionary:", car_brands)

last_key = list(car_brands.keys())[-1]
last_value = car_brands[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)