

class Lirary():
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self , bookName , bookAuther):
        self.books.append({'bookName' : bookName , 'bookAuther' : bookAuther })
        self.noBooks = len(self.books)

l1 = Lirary()
while True:

    bookName = input("Enter your book name: ")
    bookAuther = input("Enter your book Auther Name name: ")

    l1.addBook(bookName , bookAuther)
    action = input("Press 'q' to quit, 'r' to see all details of books in Library, or any other key to add a new book to the library: ")
    if(action == 'r'):
        for i in l1.books:
            print(i)
        action = input("Press 'q' to quit, or any other key to add a new book to the library: ")
    elif(action == 'q'):
        break


    




# class Library():
#     def __init__(self,bookName, bookAuthor):
#         self.book = bookName
#         self.auther = bookAuthor

#     def __str__(self):
#         return f'Book Name: {self.bookName}, Author: {self.bookAuthor}'


# allBooks = [];


# while True:
#     bookName = input("Enter your book name: ")
#     bookAuther = input("Enter your book Auther Name name: ")

#     bookName = Library(bookName , bookAuther)

#     allBooks.append(bookName)

#     print(f'\n Total books in Lirary {len(allBooks)}')
    

#     action = input("Press 'q' to quit, 'r' to see all details of books in Library, or any other key to add a new book to the library: ")
#     if(action == 'r'):
#         for i in allBooks:
#             print(i)
#     elif(action == 'q'):
#         break