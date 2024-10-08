class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
        
        

class Library:
    def __init__(self):
        self.books:list[Book] = []
        
        
    def add_book(self, book:Book):
        self.books.append(book)
        
    def list_books(self):
        
        for book in self.books:
            if isinstance(book, PrintBook):
                print(f'PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}')
            
            elif isinstance(book, EBook):
                print(f'EBook: {book.title} by {book.author}, File Size: {book.file_size}')
            
            else:
                print(f"Book: {book.title} by {book.author}")
                


def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()