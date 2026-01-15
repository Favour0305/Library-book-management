NAME: OWOSENI OLUWASEYIFUNMI FAVOUR 
MATRIC NUMBER:24/15187
import json
import os

FILE_NAME = "books.json"

def load_books():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    books = load_books()
    book_id = len(books) + 1
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "year": year
    }

    books.append(book)
    save_books(books)
    print("Book added successfully.")

def view_all_books():
    books = load_books()
    if not books:
        print("No books found.")
        return

    for book in books:
        print(f"{book['id']}. {book['title']} by {book['author']} ({book['year']})")

def view_book_detail():
    books = load_books()
    book_id = int(input("Enter book ID: "))

    for book in books:
        if book["id"] == book_id:
            print("Book Details")
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Year:", book["year"])
            return

    print("Book not found.")

def delete_book():
    books = load_books()
    book_id = int(input("Enter book ID to delete: "))

    new_books = [b for b in books if b["id"] != book_id]

    if len(new_books) == len(books):
        print("Book not found.")
    else:
        save_books(new_books)
        print("Book deleted successfully.")

def main():
    while True:
        print("\n=== LIBRARY BOOK MANAGEMENT ===")
        print("1. Add Book")
        print("2. View All Books")
        print("3. View Book Detail")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_all_books()
        elif choice == "3":
            view_book_detail()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()