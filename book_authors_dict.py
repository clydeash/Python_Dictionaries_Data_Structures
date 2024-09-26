book_authors = {
    "To Kill a Mockingbird": "Harper Lee",
    "Pride and Prejudice": "Jane Austen",
    "1984": "George Orwell",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "The Catcher in the Rye": "J.D. Salinger",
    "The Lord of the Rings": "J.R.R. Tolkien",
    "Harry Potter and the Sorcerer's Stone": "J.K. Rowling",
    "The Hobbit": "J.R.R. Tolkien",
    "The Hitchhiker's Guide to the Galaxy": "Douglas Adams",
    "The Da Vinci Code": "Dan Brown",
    "Gone Girl": "Gillian Flynn",
    "The Girl with the Dragon Tattoo": "Stieg Larsson"
}

print("a. Entire dictionary:", book_authors)

print("b. Author of the 9th book:", book_authors["The Hitchhiker's Guide to the Galaxy"])

book_authors["The Catcher in the Rye"] = "Jerome David Salinger"

del book_authors["1984"]

print("c. Updated dictionary:", book_authors)

last_key = list(book_authors.keys())[-1]
last_value = book_authors[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)