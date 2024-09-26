programming_languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich",
    "PHP": "Rasmus Lerdorf",
    "Ruby": "Yukihiro Matsumoto",
    "C#": "Anders Hejlsberg"
}

print("a. Entire dictionary:", programming_languages)

print("b. Developer of the 4th programming language:", programming_languages["JavaScript"])

programming_languages["Ruby"] = "Yukihiro 'Matz' Matsumoto"

del programming_languages["Java"]

print("c. Updated dictionary:", programming_languages)

last_key = list(programming_languages.keys())[-1]
last_value = programming_languages[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)