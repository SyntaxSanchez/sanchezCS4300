# task5.py

# List of books (title, author)
books = [
    ("1984", "George Orwell"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("Brave New World", "Aldous Huxley"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("The Catcher in the Rye", "J.D. Salinger")
]

# Student database dictionary: {name: student_id}
studentDatabase = {
    "Alice": "S1",
    "Chris": "S2",
    "Jessie": "S3",
    "Diana": "S4"
}

# Functions for testability
def booksThree():
    return books[:3]

def studentID(name):
    return studentDatabase.get(name)

