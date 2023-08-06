import mysql.connector
import bcrypt

mydb = mysql.connector.connect(
    host = "localhost",
    user =  "root",
    password = "",
    database = "revision_db"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE revision_db")
# print("Database created succefully")

# mycursor.execute("CREATE TABLE revise(id INT PRIMARY KEY, course VARCHAR(100), date VARCHAR(20), password VARCHAR(20))")
# print("Table created succefully")


id_ =  int(input("Enter id "))
Course_name = input("Enter course to study ")
date_ = input("Enter Date ")
password = input("Enter password ")

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password.encode(), salt)

# def revis1():
#     revs = "INSERT INTO revise(id, course, date, password) VALUES(%s, %s, %s, %s)"
#     rev1 = id_, Course_name, date_, hashed

#     mycursor.execute(revs, rev1)
#     mydb.commit()


# revis1()

class revis1:
    def __init__(self, id, course, date, hashed):
        self.id_ = id
        self.Course_name = course
        self.date_ = date
        self.hashed = hashed
    
revsObj = revis1(id_, Course_name, date_, hashed)

sql = "INSERT INTO revise(id, course, date, password) VALUES(%s, %s, %s, %s)"
vals = revsObj.id_, revsObj.Course_name, revsObj.date_, revsObj.hashed

mycursor.execute(sql, vals)
mydb.commit()


