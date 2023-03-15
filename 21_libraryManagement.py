class Library:
    def __init__(self):
        self.books = []

    def addBook(self, bookName):
        self.books.append(bookName)

    def removeBook(self, bookName):
        self.books.remove(bookName)

    def showBooksList(self):
        numberOfBooks = len(self.books)
        if (self.numberOfBooks > 0):
            print(f"There are {numberOfBooks} books in library")
            for i in range(0, numberOfBooks):
                print(f"{i+1}. {self.books[i]}")

    @property
    def numberOfBooks(self):
        return len(self.books)


# Creating Library class object
l = Library()

quit = False
while (not (quit)):
    print("\nEnter\n1---->To add new book to library\n2---->To remove book from the library\n3---->To list all books\n4---->To know the number of books in library\n0---->To quit")
    n = int(input("Enter your choice: "))
    match n:
        case 1:
            l.addBook(input("Enter name of the book: "))
        case 2:
            l.removeBook(input("Enter name of the book: "))
        case 3:
            l.showBooksList()
        case 4:
            print(f"Total number of books in library: {l.numberOfBooks}")
        case 0:
            print("Thank you...")
            quit = True
        case _:
            print("Invalid option.....")
