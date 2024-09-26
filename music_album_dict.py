albums = {
    "Thriller": 1982,
    "Back in Black": 1980,
    "Abbey Road": 1969,
    "The Dark Side of the Moon": 1973,
    "Born to Run": 1975,
    "Rumours": 1977,
    "Led Zeppelin IV": 1971,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Nevermind": 1991,
    "Appetite for Destruction": 1987
}

print("a. Entire dictionary:", albums)

print("b. Release year of the 3rd album:", albums["Abbey Road"])

albums["Sgt. Pepper's Lonely Hearts Club Band"] = 1968

del albums["Born to Run"]

print("c. Updated dictionary:", albums)

last_key = list(albums.keys())[-1]
last_value = albums[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)