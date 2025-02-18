import json

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author, year, genre):
        self.books.append({
            "title": title,
            "author": author,
            "year": year,
            "genre": genre
        })
        print(f"Book '{title}' added successfully!")
    
    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"Book '{title}' removed successfully!")
                return
        print("Book not found!")
    
    def search_by_title(self, title):
        results = [book for book in self.books if title.lower() in book["title"].lower()]
        if results:
            for book in results:
                print(f"Found: {book['title']} by {book['author']}, Year: {book['year']}, Genre: {book['genre']}")
        else:
            print("No books found with that title.")

if __name__ == "__main__":
    library = Library()
    
    while True:
        print("\nLibrary System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search by Title")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            genre = input("Enter book genre: ")
            library.add_book(title, author, year, genre)
        
        elif choice == "2":
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        
        elif choice == "3":
            title = input("Enter book title to search: ")
            library.search_by_title(title)
        
        elif choice == "4":
            break
        
        else:
            print("Invalid choice! Try again.")
