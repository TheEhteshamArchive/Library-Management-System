from database import connect

def add_student(name):
    db = connect()
    cursor = db.cursor()

    query = """
            insert into students(name) values (%s)"""
    
    cursor.execute(query, (name,))
    db.commit()

    cursor.close()
    db.close()

def view_students():
    db = connect()
    cursor = db.cursor()

    cursor.execute("select * from students")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()