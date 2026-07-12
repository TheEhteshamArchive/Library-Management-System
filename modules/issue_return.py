from database import connect

def issue_book(student_id, book_id):
    db = connect()
    cursor = db.cursor()

    #Chck book availabiltiy 
    cursor.execute(
        "select quantity from books where book_id = %s", (book_id,)
    )
    result = cursor.fetchone()

    if result is None:
        print("Book does not exist")
        return
    
    if result[0] <= 0:
        print("Book not Available")
        return
    
    #Add the issued record
    cursor.execute(
        """insert into issued_books(student_id, book_id, issue_date)
        values(%s, %s, CURDATE())""", (student_id, book_id)
    )

    #Reduce teh quantity
    cursor.execute(
        """update books set quantity = quantity - 1 where book_id = %s""", (book_id,)
    )

    db.commit()
    
    print("Book issued successfully")

    cursor.close()
    db.close()

def return_book(student_id, book_id):
    db = connect()
    cursor = db.cursor()

    cursor.execute(
        """
        DELETE FROM issued_books
        WHERE student_id = %s AND book_id = %s
        """,
        (student_id, book_id)
    )

    cursor.execute(
        """
        UPDATE books
        SET quantity = quantity + 1
        WHERE book_id = %s
        """,
        (book_id,)
    )

    db.commit()

    print("Book returned successfully")

    cursor.close()
    db.close()


def view_issued_books():
    db = connect()
    cursor = db.cursor()

    query = """
    SELECT 
        issued_books.issue_id,
        students.name,
        books.title,
        issued_books.issue_date

    FROM issued_books

    JOIN students
    ON issued_books.student_id = students.student_id

    JOIN books
    ON issued_books.book_id = books.book_id
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    print("\n===== Issued Books =====")

    for row in rows:
        print(row)

    cursor.close()
    db.close()