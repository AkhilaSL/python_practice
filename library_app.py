class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __str__(self):
        return f"Book title:{self.title} , Author: {self.author}"
class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)
        print("Book "+ book.title + "has been successfully added .")
    
    def view_books(self):
        if not self.books:
            print("No books in the library..!")
        for i in self.books:
            print(i)
    def search_book(self,querry):
        found_book=[book for book in self.books if (querry.lower() in book.title.lower()) or (querry.lower() in book.author.lower())]
        if not found_book:
            print("Book not found...!")
        else:
            for book in found_book:
                print(book)

def main():
        lib=Library()
        while True:
            print('''Library Menu
            1.Add Book
            2.View Books 
            3.Search Books by Book name or Author name
            4.Exit ''')
            ch=input("Enter your choice: ")
            
            if ch=="1":
                title=input("Enter the book title:")
                author=input("Enter the author name:")
                book=Book(title,author)
                lib.add_book(book)
            elif ch=="2":
                lib.view_books()
            elif ch=="3":
                querry=input("Enter the book title or author name : ")
                lib.search_book(querry)
            elif ch == "4":
                print("Exiting the library application...")
                break

            else:
                print("Invalid choice..!Try again.")
if __name__=="__main__":
    main()




            
        
            
            