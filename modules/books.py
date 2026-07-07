from database import connect

def add_book(title, author, quantity):
    db = connect()
    cursor = db.cursor()

    query = """
    insert into books(title, author, quantity) values (%s, %s, %s)
    """

    cursor.execute(query, (title, author, quantity))
    db.commit()
    
    cursor.close()
    db.close()

def view_books():
    db = connect()
    cursor = db.cursor()

    cursor.execute("Select * from books")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

def search_book(title):
    db = connect()
    cursor = db.cursor()
    query = """
            Select * from books where title like %s"""
    cursor.execute(query, (f"%{title}%",))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

def delete_book(book_id):
    db = connect()
    cursor = db.cursor()

    query = """
                delete from books where book_id = %s"""

    cursor.execute(query, (book_id,))
    db.commit()

    cursor.close()
    db.close()

def update_quantity(book_id, quantity):
    db = connect()
    cursor = db.cursor()

    query = """
            update books set quantity = %s where book_id = %s"""
    
    cursor.execute(query, (quantity, book_id))
    db.commit()

    cursor.close()
    db.close()