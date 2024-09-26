university_courses = {
    "Harvard University": "Computer Science",
    "Stanford University": "Engineering",
    "Massachusetts Institute of Technology (MIT)": "Computer Science",
    "University of Oxford": "Law",
    "University of Cambridge": "Medicine",
    "University of California, Berkeley": "Business",
    "University of the Philippines - Diliman": "Engineering", 
    "University of Pennsylvania": "Business"
}

print("a. Entire dictionary:", university_courses)

print("b. Course of the 3rd university:", university_courses["Massachusetts Institute of Technology (MIT)"])

university_courses["University of Cambridge"] = "Computer Science"

del university_courses["Harvard University"]

print("c. Updated dictionary:", university_courses)

last_key = list(university_courses.keys())[-1]
last_value = university_courses[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)