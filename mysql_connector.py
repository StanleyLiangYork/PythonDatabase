import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="stanley123",
        database = "testdb"
    )
# print(mydb)

# make a cursor
cursor =  mydb.cursor()

sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"

student1 = ("Stanley", 30)
students = [("John", 11), ("Smith", 9), ("Bob", 8), ("Peter", 12)]

# cursor.execute(sqlFormula, student1)
cursor.executemany(sqlFormula, students)
mydb.commit()

# cursor.execute("CREATE DATABASE testdb")
# cursor.execute("CREATE TABLE students (name VARCHAR(100), age INTEGER(3))")
# cursor.execute("SHOW TABLES")

# for table in cursor:
#     print(table)