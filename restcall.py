import requests

BASE_URL = "http://127.0.0.1:5000"

def get_all_books():
    print("\nGET /books")
    response = requests.get(f"{BASE_URL}/books")
    print("Status:", response.status_code)
    print("Response:", response.json())

def get_book(book_id):
    print(f"\nGET /books/{book_id}")
    response = requests.get(f"{BASE_URL}/books/{book_id}")
    print("Status:", response.status_code)
    print("Response:", response.json())

def add_book(book):
    print("\nPOST /books")
    response = requests.post(f"{BASE_URL}/books", json=book)
    print("Status:", response.status_code)
    print("Response:", response.json())

def update_book(book_id, update_data):
    print(f"\nPUT /books/{book_id}")
    response = requests.put(f"{BASE_URL}/books/{book_id}", json=update_data)
    print("Status:", response.status_code)
    print("Response:", response.json())

def delete_book(book_id):
    print(f"\nDELETE /books/{book_id}")
    response = requests.delete(f"{BASE_URL}/books/{book_id}")
    print("Status:", response.status_code)
    print("Response:", response.json())

if __name__ == "__main__":
    # 1. Get all books
    get_all_books()

    # 2. Get a single book by ID
    get_book(1)

    # 3. Add a new book
    new_book = {"id": 3, "title": "RESTful APIs", "author": "Alex Lee"}
    add_book(new_book)

    # 4. Update the new book
    update_data = {"title": "RESTful APIs with Python"}
    update_book(3, update_data)

    # 5. Delete the new book
    delete_book(3)

    # 6. Final list of books
    get_all_books()
