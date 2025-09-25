import requests

# API endpoint
url = "http://127.0.0.1:5000/books"

try:
    response = requests.get(url)
    if response.status_code == 200:
        books = response.json()
        print("Books in API:")
        for book in books:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
    else:
        print(f"Failed to fetch books. Status code: {response.status_code}")
except requests.exceptions.ConnectionError:
    print("Could not connect to the API. Is the server running?")
