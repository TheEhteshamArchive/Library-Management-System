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