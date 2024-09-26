movie_directors = {
    "The Shawshank Redemption": "Frank Darabont",
    "The Godfather": "Francis Ford Coppola",
    "The Dark Knight": "Christopher Nolan",
    "Pulp Fiction": "Quentin Tarantino",
    "The Lord of the Rings: The Return of the King": "Peter Jackson",
    "Inception": "Christopher Nolan",
    "The Matrix": "Lana Wachowski",
    "Forrest Gump": "Robert Zemeckis",
    "Fight Club": "David Fincher",
    "The Silence of the Lambs": "Jonathan Demme"
}

print("a. Entire dictionary:", movie_directors)

print("b. Director of the 5th movie:", movie_directors["The Lord of the Rings: The Return of the King"])

movie_directors["Fight Club"] = "David Fincher and Brad Pitt"

del movie_directors["The Matrix"]

print("c. Updated dictionary:", movie_directors)

last_key = list(movie_directors.keys())[-1]
last_value = movie_directors[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)