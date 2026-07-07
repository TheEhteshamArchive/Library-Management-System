from modules.books import add_book, view_books
from modules.students import add_student, view_students
from modules.issue_return import issue_book

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Book")
    print("3. Add Students")
    print("4. View Students")
    print("5. Issue Book")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":

        title = input("Title: ")
        author = input("Author: ")
        quantity = int(input("Quantity: "))

        add_book(title, author, quantity)

        print("Book Added!")
    elif choice == "3":
        name = input("Student Name: ")
        add_student(name)
        
    
    elif choice == "4":
        
        view_students()

    elif choice == "5":
        student_id = int(input("Student ID: "))
        book_id = int(input("Book ID: "))
        issue_book(student_id, book_id)
    
    elif choice == "6":
        break
    else:
        print("Invalid choice")

