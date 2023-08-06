import mysql.connector
import bcrypt

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "registration"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE registration")
# mycursor.execute("CREATE TABLE users(id INT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), password VARCHAR(100))")

# dat = "INSERT INTO users(id, name, email, password) VALUES(%s, %s, %s, %s)"
# daats = [("1", "John Dawson", "jdaw@gmail.com", "jad12354"),
#          ("2", "Sammy Crabb", "samcra@yahoo.com", "sac1458"),
#          ("3", "david Gomez", "davgo@yahoo.com", "davgee4587"),
#          ("4", "sarah Gomez", "sargo@yahoo.com", "sargee4587"),
#          ("5", "ako bola", "akobee@yahoo.com", "akbeee4587")]


# mycursor.executemany(dat, daats)
# mydb.commit()

# print(mycursor.rowcount, "Data inserted")

# id_1 = input("Enter id: ")
# name_1 = input("Enter name: ")
# # email_1 = input("Enter email: ")
# password_1 = input("Enter password: ")


# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(password_1.encode(), salt)

# def create_user():
#         sql = "INSERT INTO users(id, name, email, password) VALUES(%s, %s, %s, %s)"
#         val = id_1, name_1, email_1, password_1
#         mycursor.execute(sql, val)
#         mydb.commit()


# LOG IN

name_1 = input("Enter name ")
password_1 = input("Enter password ")

# def check_credentials(name, password):
#   mycursor.execute("SELECT password FROM users WHERE name = %s", (name_1,))
#   fetchdata = mycursor.fetchone()

#   if fetchdata is None:
#     return False
#   else: return fetchdata[0] == password_1

# def logIn():
#   if check_credentials(name_1, password_1):
#     return ("Log In successful")
#   else: return("Log In failed")

# print(logIn())

# class UserAuthenticator:
#     def __init__(self):
#         self.name_1 = input("Enter name: ")
#         self.password_1 = input("Enter password: ")

#     def check_credentials(self, name, password):
#         self.mycursor.execute("SELECT password FROM users WHERE name = %s", (name,))
#         fetchdata = self.mycursor.fetchone()

#         if fetchdata is None:
#             return False
#         else:
#             return fetchdata[0] == password

#     def logIn(self):
#         if self.check_credentials(self.name_1, self.password_1):
#             print("Log In successful")
#         else:
#             print("Log In failed") 


# if __name__ == "__main__":
#     authenticator = UserAuthenticator()
#     print(authenticator.logIn())


# david Gomez
# davgo@yahoo.com
# davgee4587


# def dellete():
#   mycursor.execute("DELETE FROM users WHERE id = 1234")
#   mydb.commit()
#   return(mycursor.rowcount, "Row Deleted successfully")

# print(dellete())


# PHONEBOOK
# mycursor.execute("CREATE DATABASE phoneBook")
# mycursor.execute("CREATE TABLE contact_list(id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(100), last_name VARCHAR(100), contact VARCHAR(10))")

# id_a = int(input("Enter id: "))
# fname = input("Enter first_name: ")
# lname = input("Enter last name: ")
# contas = input("Enter phone number: ")


# def phone():
#     sql = "INSERT INTO contact_list(id, first_name, last_name, contact) VALUES(%s, %s, %s, %s)"
#     val = id_a, fname, lname, contas
#     mycursor.execute(sql, val)
#     mydb.commit()


# phone()

# class Phone:
#   def __init__(self, id, first_name, last_name, contact):
#     self.id_a = id
#     self.fname = first_name
#     self.lname = last_name
#     self.contas = contact
  
# phoneOO = Phone(id_a, fname, lname, contas)

# sql = "INSERT INTO contact_list(id, first_name, last_name, contact) VALUES(%s, %s, %s, %s)"
# val = phoneOO.id_a, phoneOO.fname, phoneOO.lname, phoneOO.contas

# mycursor.execute(sql, val)
# mydb.commit()




# VOTERS REGISTER
# mycursor.execute("CREATE DATABASE voters_register")
# mycursor.execute("CREATE TABLE voters(id INT PRIMARY KEY, firstName VARCHAR(100) NOT NULL, lastName VARCHAR(100) NOT NULL,"
#                   " otherNames VARCHAR(100), birthDate VARCHAR(20) NOT NULL, gender CHAR(10), pollingName VARCHAR(200), "
#                  " pollingNumber INT NOT NULL)")

# DATA INPUT FORM

# id_ = input("Enter id#: ")
# firstName_ = input("Enter First Name: ")
# lastName_ = input("Enter Last Name: ")
# otherNames_ = input("Enter Other Names: ")
# birthDate_ = input("Enter Date of Birth: ")
# gender_ = input("Enter Gender: ")
# pollingName_ = input("Enter Polling Station Name: ")
# pollingNumber_ = input("Enter Polling Number: ")

# def voterReg():
#   sql = "INSERT INTO voters(id, firstName, lastName, otherNames, birthDate, gender, pollingName, pollingNumber) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)" 
#   val = id_, firstName_, lastName_, otherNames_, birthDate_, gender_, pollingName_, pollingNumber_
#   mycursor.execute(sql, val)
#   mydb.commit()

# voterReg()

# print(mycursor.rowcount, ("Data Input Successful"))


# POLLING OFFICER LOG IN
# mycursor.execute("CREATE TABLE officeUser(id INT AUTO_INCREMENT PRIMARY KEY, full_name VARCHAR(100), username VARCHAR(100), "
#                           " password VARCHAR(100) NOT NULL)")


# id1 = input("ID Number: ")
# fname_ = input("Full Name: ")
# user_ = input("User Name: ")
# password_ = input("Password: ")

# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(password_.encode(), salt)

# user1 = "INSERT INTO officeUser(id, full_name, username, password) VALUES(%s, %s, %s, %s)"
# values1 = id1, fname_, user_, hashed
# mycursor.execute(user1, values1)
# mydb.commit()
# print(mycursor.rowcount, "Data input successful")



# def check_login(username, password):
#   mycursor.execute("SELECT password FROM officeUser WHERE username = %s", (user_,))
#   fetchuser = mycursor.fetchone()

#   if fetchuser is None:
#     return False
#   else: 
#     return fetchuser[0] == password

# def confirmlog():
#   if check_login(user_, password_):
#     print("log In successful")
#   else:
#     print("log In faiiled")



# a.srasraku
# as1245


# mycursor.execute("DELETE FROM voters WHERE id = '1'")
# mydb.commit()
# print(mycursor.rowcount, "Data deleted successfully")


