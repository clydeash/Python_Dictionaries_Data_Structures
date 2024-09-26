holidays = {
    "New Year's Day": "January 1st",
    "Martin Luther King Jr. Day": "Third Monday of January",
    "Presidents' Day": "Third Monday of February",
    "St. Patrick's Day": "March 17th",
    "Earth Day": "April 22nd",
    "Memorial Day": "Last Monday of May",
    "Independence Day": "July 4th",
    "Labor Day": "First Monday of September",
    "Columbus Day": "Second Monday of October",
    "Thanksgiving Day": "Fourth Thursday of November" 
}

print("a. Entire dictionary:", holidays)

print("b. Date of the 4th holiday:", holidays["St. Patrick's Day"])

holidays["Columbus Day"] = "Second Monday of October"  # Updating the date of the 9th holiday (already correct)

del holidays["Martin Luther King Jr. Day"]  # Deleting the 2nd holiday

print("c. Updated dictionary:", holidays)

last_key = list(holidays.keys())[-1]
last_value = holidays[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)