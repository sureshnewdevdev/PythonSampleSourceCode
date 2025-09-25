from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store (list of dictionaries)
books = [
    {"id": 1, "title": "Python Basics", "author": "John Doe"},
    {"id": 2, "title": "Flask for Beginners", "author": "Jane Smith"}
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Book API!"

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    data = request.get_json()
    book.update(data)
    return jsonify(book)

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    index = next((i for i, b in enumerate(books) if b["id"] == book_id), None)
    if index is None:
        return jsonify({"error": "Book not found"}), 404
    deleted = books.pop(index)
    return jsonify(deleted)

if __name__ == '__main__':
    app.run(debug=True)
        