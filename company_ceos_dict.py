company_ceos = {
    "Apple": "Tim Cook",
    "Microsoft": "Satya Nadella",
    "Amazon": "Andy Jassy",
    "Google": "Sundar Pichai",
    "Meta": "Mark Zuckerberg",
    "Tesla": "Elon Musk",
    "Netflix": "Reed Hastings",
    "IBM": "Arvind Krishna",
    "Samsung": "Han Jong-Hee",
    "Walmart": "Doug McMillon"
}

print("a. Entire dictionary:", company_ceos)

print("b. CEO of the 6th company:", company_ceos["Tesla"])

company_ceos["Amazon"] = "Jassy"  # Updating the CEO of the 3rd company

del company_ceos["Samsung"]  # Deleting the 9th company

print("c. Updated dictionary:", company_ceos)

last_key = list(company_ceos.keys())[-1]
last_value = company_ceos[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)