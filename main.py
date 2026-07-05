from database import connect

try:
    db = connect()
    print("! ! Connected ! !")
    db.close()
except Exception as e:
    print("Error: ", e)

from modules.books import add_book
bookTitle = input("Enter the books Title: ")
bookAuthor = input("Enter the books Author: ")
bookQuantity = int(input("Enter Quantity: "))

add_book(
    bookTitle,
    bookAuthor,
    bookQuantity
)

print("! ! Book Added ! !")

from modules.books import view_books
view_books()