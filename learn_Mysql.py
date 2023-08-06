import mysql.connector
import bcrypt


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "demos1_db"
  
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE demos1_db")
#mycursor.execute("CREATE TABLE demo (id INT AUTO_INCREMENT PRIMARY KEY, full_name VARCHAR(100) NOT NULL, age INT NOT NULL)")
# mycursor.execute("DROP TABLE users")

# data1 = "INSERT INTO demo(id, full_name, age) VALUES(%s, %s, %s)"
# data2 = [("1", "Mensha Evans", "23"),
#           ("2", "Eugnee Brown", "24"),
#           ("3", "Salam Abdul", "28"),
#           ("4", "Ansah Hawa", "22"),
#           ("5", "Solomon Owusu", "21")]
# mycursor.executemany(data1, data2)

# mydb.commit()
# print(mycursor.rowcount, "Data inserted successfully")

# mycursor.execute("DELETE FROM users WHERE id = 1")
# mydb.commit()
# print(mycursor.rowcount, "Row Deleted successfully")

mycursor.execute("SELECT full_name FROM demo WHERE id = 1")
mydata = mycursor.fetchone()
mydb.commit()


for data in mydata:
  print(data)