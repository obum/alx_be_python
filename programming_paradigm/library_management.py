class Book:
    
    def __init__(self, title, author) -> None:
        self.title: str = title
        self.author: str = author
        self.___is_checked_out = False
        
    # def __str__(self) -> str:
    #     return f'Book title: {self.title} by Book author: {self.author}'
    
    
class Library:
    
    def __init__(self):
        self.___books: list[Book] = []
        self.checked_out_books = ""
        
    def add_book(self, book):
        self.___books.append(book)
        # print(f'{book.title} has been added to {self}')
        
    def check_out_book(self, title):
        title_list = [book.title for book in self.___books]
        # print(title_list)
        
        if title not in title_list: 
            pass         
            # print(f'{title} is not available, checking out : Failed ')      
        else:         
            # print(f'{title} is Available, checking out : Successful')
            index_of_title = title_list.index(title)
            self.checked_out_books = self.___books[index_of_title]
            self.___books.remove(self.___books[index_of_title])
            
            
        
        

            
    def list_available_books(self):
        
        for book in self.___books:
            print(f'{book.title} by {book.author}')
        print()
        
    def return_book(self, title: str):
        if title == self.checked_out_books.title:
            self.add_book(self.checked_out_books)
        
            
            
        
        
def main():
        
    # book_1 = Book("Things fall apart", "Chinwe Achebe")
    book_2 = Book("1984", "George Orwell")
    book_3 = Book("Brave New World", "Aldous Huxley")


    library = Library()

    # library.add_book(book_1)
    library.add_book(book_2)
    library.add_book(book_3)

    print('Available books after setup:')
    library.list_available_books()

    library.check_out_book('1984')
    print("\nAvailable books after checking out '1984'")
    library.list_available_books()

    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()


if __name__ == "__main__":
    main()    

# print(library.checked_out_books)

# print(new_book, new_book._Book___is_checked_out, sep="\n")