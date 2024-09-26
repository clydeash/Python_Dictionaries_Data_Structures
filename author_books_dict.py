authors_books = {
    "Jane Austen": "Pride and Prejudice",
    "William Shakespeare": "Hamlet",
    "J.R.R. Tolkien": "The Lord of the Rings",
    "Charles Dickens": "A Tale of Two Cities",
    "Stephen King": "The Shining",
    "Agatha Christie": "Murder on the Orient Express",
    "Ernest Hemingway": "The Old Man and the Sea",
    "Harper Lee": "To Kill a Mockingbird"
}

print("a. Entire dictionary:", authors_books)

print("b. Book of the 5th author:", authors_books["Stephen King"])

authors_books["Ernest Hemingway"] = "For Whom the Bell Tolls"

del authors_books["Agatha Christie"]

print("c. Updated dictionary:", authors_books)

last_key = list(authors_books.keys())[-1]
last_value = authors_books[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)