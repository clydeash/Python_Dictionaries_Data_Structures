jobs_salaries = {
    "Software Engineer": 110000,
    "Data Scientist": 120000,
    "Nurse": 75000,
    "Teacher": 60000,
    "Accountant": 70000,
    "Marketing Manager": 85000,
    "Project Manager": 95000,
    "Web Developer": 90000,
    "Sales Representative": 65000,
    "Mechanic": 55000
}

print("a. Entire dictionary:", jobs_salaries)

print("b. Salary of the 3rd job:", jobs_salaries["Nurse"])

jobs_salaries["Project Manager"] = 105000

del jobs_salaries["Sales Representative"]

print("c. Updated dictionary:", jobs_salaries)

last_key = list(jobs_salaries.keys())[-1]
last_value = jobs_salaries[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)