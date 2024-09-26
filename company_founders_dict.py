companies = {
    "Apple": "Steve Jobs, Steve Wozniak, Ronald Wayne",
    "Microsoft": "Bill Gates, Paul Allen",
    "Amazon": "Jeff Bezos",
    "Google": "Larry Page, Sergey Brin",
    "Facebook": "Mark Zuckerberg",
    "Tesla": "Elon Musk",
    "Netflix": "Reed Hastings, Marc Randolph",
    "SpaceX": "Elon Musk"
}

print("a. Entire dictionary:", companies)

print("b. Founder of the 6th company:", companies["Tesla"])

companies["Microsoft"] = "Bill Gates, Paul Allen, Steve Ballmer"

del companies["SpaceX"]

print("c. Updated dictionary:", companies)

last_key = list(companies.keys())[-1]
last_value = companies[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)