from modules.books import add_book, view_books
from modules.students import add_student, view_students, search_student, delete_student
from modules.issue_return import issue_book, return_book, view_issued_books


while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Add Student")
    print("4. View Students")
    print("5. Search Student")
    print("6. Delete Student")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. View Issued Books")
    print("10. Exit")

    choice = input("Choose: ")

    if choice == "1":

        title = input("Title: ")
        author = input("Author: ")
        quantity = int(input("Quantity: "))

        add_book(title, author, quantity)

        print("Book Added!")

    elif choice == "2":

        view_books()

    elif choice == "3":

        name = input("Student Name: ")
        add_student(name)

        print("Student Added!")

    elif choice == "4":

        view_students()
    
    elif choice == "5":

        name = input("Search student name: ")
        search_student(name)
    
    elif choice == "6":

        student_id = int(input("Student ID: "))
        delete_student(student_id)

    elif choice == "7":

        student_id = int(input("Student ID: "))
        book_id = int(input("Book ID: "))

        issue_book(student_id, book_id)

    elif choice == "8":

        student_id = int(input("Student ID: "))
        book_id = int(input("Book ID: "))

        return_book(student_id, book_id)

    elif choice == "9":

        view_issued_books()

    elif choice == "10":

        print("Exiting...")
        break

    else:
        print("Invalid choice")