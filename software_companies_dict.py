software_companies = {
    "Microsoft": "Redmond, Washington",
    "Google": "Mountain View, California",
    "Amazon": "Seattle, Washington",
    "Apple": "Cupertino, California",
    "Meta": "Menlo Park, California",
    "IBM": "Armonk, New York",
    "Oracle": "Austin, Texas",
    "Salesforce": "San Francisco, California",
    "Adobe": "San Jose, California",
    "SAP": "Walldorf, Germany"
}

print("a. Entire dictionary:", software_companies)

print("b. Headquarters of the 3rd company:", software_companies["Amazon"])

software_companies["Salesforce"] = "San Francisco, California (and others)"

del software_companies["Adobe"]

print("c. Updated dictionary:", software_companies)

last_key = list(software_companies.keys())[-1]
last_value = software_companies[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)