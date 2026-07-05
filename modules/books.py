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