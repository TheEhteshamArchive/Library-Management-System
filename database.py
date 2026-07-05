import mysql.connector as Con

def connect():
    return Con.connect(
        host = "localhost",
        user = "root",
        password="Akis.123",
        database="Management"
    )