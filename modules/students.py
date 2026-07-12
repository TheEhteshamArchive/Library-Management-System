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

def search_student(name):
    db = connect()
    cursor = db.cursor()

    query = """
    SELECT * FROM students
    WHERE name LIKE %s
    """

    cursor.execute(query, (f"%{name}%",))

    rows = cursor.fetchall()

    print("\n===== Search Results =====")

    for row in rows:
        print(row)

    cursor.close()
    db.close()


def delete_student(student_id):
    db = connect()
    cursor = db.cursor()

    query = """
    DELETE FROM students
    WHERE student_id = %s
    """

    cursor.execute(query, (student_id,))
    db.commit()

    print("Student deleted!")

    cursor.close()
    db.close()