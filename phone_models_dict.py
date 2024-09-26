phones = {
    "iPhone 14 Pro Max": "Apple",
    "Samsung Galaxy S23 Ultra": "Samsung",
    "Google Pixel 7 Pro": "Google",
    "OnePlus 11": "OnePlus",
    "Xiaomi 13 Pro": "Xiaomi",
    "Sony Xperia 1 V": "Sony",
    "Motorola Edge 40 Pro": "Motorola",
    "Vivo X90 Pro+": "Vivo",
    "Oppo Find X6 Pro": "Oppo",
    "Realme GT3 Pro": "Realme"
}

print("a. Entire dictionary:", phones)

print("b. Manufacturer of the 2nd phone model:", phones["Samsung Galaxy S23 Ultra"])

phones["Vivo X90 Pro+"] = "Vivo"  # Update to correct manufacturer

del phones["Sony Xperia 1 V"]

print("c. Updated dictionary:", phones)

last_key = list(phones.keys())[-1]
last_value = phones[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)