movie_genres = {
    "Action": "The Matrix",
    "Comedy": "The Hangover",
    "Horror": "The Conjuring",
    "Sci-Fi": "Interstellar",
    "Romance": "The Notebook",
    "Thriller": "The Silence of the Lambs",
    "Fantasy": "The Lord of the Rings",
    "Drama": "The Godfather" 
}

print("a. Entire dictionary:", movie_genres)

print("b. Example movie of the 3rd genre:", movie_genres["Horror"])

movie_genres["Romance"] = "Titanic"

del movie_genres["Fantasy"]

print("c. Updated dictionary:", movie_genres)

last_key = list(movie_genres.keys())[-1]
last_value = movie_genres[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)