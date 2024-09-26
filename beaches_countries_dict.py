beaches_countries = {
    "Copacabana Beach": "Brazil",
    "Whitehaven Beach": "Australia",
    "Navagio Beach": "Greece",
    "Waikiki Beach": "United States (Hawaii)",
    "Bondi Beach": "Australia",
    "South Beach": "United States (Florida)",
    "Maya Bay": "Thailand",
    "Ipanema Beach": "Brazil"
}

print("a. Entire dictionary:", beaches_countries)

print("b. Country of the 3rd beach:", beaches_countries["Navagio Beach"])

beaches_countries["South Beach"] = "United States (Miami, Florida)"

del beaches_countries["Bondi Beach"]

print("c. Updated dictionary:", beaches_countries)

last_key = list(beaches_countries.keys())[-1]
last_value = beaches_countries[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)