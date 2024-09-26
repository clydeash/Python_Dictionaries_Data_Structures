festivals = {
    "Christmas": "December 25th",
    "Halloween": "October 31st",
    "Thanksgiving": "Fourth Thursday of November",
    "Diwali": "October 24th - November 2nd",
    "Easter": "Sunday between March 22nd and April 25th",
    "New Year's Day": "January 1st",
    "Chinese New Year": "January 22nd, 2024",
    "Ramadan": "March 23rd - April 21st, 2024",
    "Hanukkah": "December 18th - December 26th",
    "Kwanzaa": "December 26th - January 1st"
}

print("a. Entire dictionary:", festivals)

print("b. Date of the 3rd festival:", festivals["Thanksgiving"])

festivals["Chinese New Year"] = "February 10th, 2025"  # Update to next year's date

del festivals["Easter"]

print("c. Updated dictionary:", festivals)

last_key = list(festivals.keys())[-1]
last_value = festivals[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)