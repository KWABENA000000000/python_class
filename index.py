'''print('ik akoi')
print(4+5)
name = input('What is your name')
colour = input('Your favourite colour')
print(name, colour)'''

'''mylist = ["apple", "banana", "cherry"]
fruit = (mylist[1])

print(mylist[1])
print(fruit[2:])
print(mylist[2])'''

'''firstName = "John"
lastName =  "Owusu"
fullName = f'{firstName} [{lastName}] is good'
print(fullName)'''


fruits = [
    'apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon', 'mango',
    'pineapple', 'kiwi', 'pear', 'cherry', 'blueberry', 'raspberry', 'lemon',
    'lime', 'peach', 'plum', 'apricot', 'pomegranate', 'coconut', 'avocado',
    'fig', 'guava', 'grapefruit', 'papaya', 'melon', 'cantaloupe', 'passionfruit',
    'dragonfruit', 'blackberry', 'raspberry', 'blackcurrant', 'cranberry',
    'gooseberry', 'kiwifruit', 'lychee', 'mangosteen', 'nectarine', 'persimmon',
    'quince', 'star fruit', 'tangerine', 'apricot', 'boysenberry', 'elderberry',
    'honeydew', 'jackfruit', 'mulberry', 'olive', 'rhubarb', 'soursop', 'ugli fruit',
    'yuzu', 'ackee', 'breadfruit', 'cherimoya', 'durian', 'feijoa', 'grapefruit',
    'kiwano', 'loquat', 'mandarin', 'pawpaw', 'plantain', 'salak', 'santol',
    'sapodilla', 'tamarillo', 'tamarind', 'ugli fruit', 'watermelon', 'ziziphus',
    'apricot', 'banana', 'coconut', 'date', 'elderberry', 'fig', 'grape', 'honeydew',
    'ilama', 'jambul', 'kiwi', 'lime', 'mango', 'nectarine', 'orange', 'papaya',
    'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli fruit', 'vanilla',
    'watermelon', 'xigua', 'yangmei', True
]

'''fruitsss = ['Banana', 'orange', '1', 'XAear', 'Mango', 'sweetmon', '20']
vegetable = ['cabbage', 'onion', 'tomato', 'okro']
fruitsss.extend(vegetable)
print(fruitsss)'''


#TUPLES

# fruitsNew = ('apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya')
# (a, b, *c) = fruitsNew
# # print(a)
# # print(b)
# print(*c)


# tuple1 = ('a', 'b', 'c')
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])

# thisdict = {'name': 'Toyota',
#         'year':   '2010',
#         'model': 'lancruiser'}
# mydict = thisdict 
# print(mydict)


# i = 0
# while i < 6:
#     i += 1
#     print(i)
# else:
#         print('i no longer true')

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
# weight = int(input("what's your weight? "))  
# unit = input('Unit of measurement')
# if unit == 'lbs': 
#     convert = 0.2* weight
#     print(f'your weight is {convert} kg')
# else:
#   convert = (10*weight)
#   print(f'your weight is {convert} lbs')

# secretNumber = 9
# guessLimit = 3
# guessCount = 0
# while guessCount < guessLimit:
#     guessCount += 1
#     guess = int(input('Guess: '))
#     if  guess == secretNumber:
#         print('You won')
#         break
# else:
#     print('you failed')


#ENTER FULL USERNAME AND PRINT TO SHOW INITIALS


# def define_name():
#     name = 'Isaac'
#     print(name)

# define_name()

# (h**2)/m
# (h*h)/m

# def body_mass(height, weight):
#     return(height**2)/weight

# print(body_mass(1.60, 20))


# def statename(name = 'anonymous'):
#     print(name)

# statename()

#LAMBDA

# input_email = "kofikumi64gmail.com" #/ phonenumber / username
# input_password = "passme123"
# password_db = " "

# if(input_password == password_db):
#     print('open homepage')
# else:
#     print('password incorrect')



# logIn_Address = input("Enter email address / phone number / username ")
# email_bb = "isakwako@gmail.com"
# phone_number_db1 = ""
# username = ""

# def logInn(if(input_email == email_bd):
#         print(f"email was used  {input_email}")
#         print("proceed to enter your password")
#         if (input_password ==password_bd):
#             print("login"))

# if (logIn_Address == email_bb) or (logIn_Address == phone_number_db1) or (logIn_Address == username):
    
#     elif(input_phone==phone_db):
#         print(f"phone number was used  {input_phone}")
#         print("proceed to enter your password")
#         if (input_password ==password_bd):
#             print("login")
#     elif( input_username==username_db):
#         print(f"username was used  {input_username}")
#         print("proceed to enter your password") 
#         if (input_password ==password_bd):
#             print("login")

# else:
#     print('wrong log in details')

# personalInfor = [
#   {
#     "name": "marley",
#     "age": 20,
#     "address": {
#       "country": "Ghana",
#       "zip_code": "+233",
#       "phoneNumbers": [
#         7777777, 
#         900000
#         ],
#     },
#     "gender": "male",
#     "occupation": "developer",
#   },
# ]


# # print(type(personalInfor))

# personalInfor[0]['occupation'] = 'dancer'

# print(personalInfor)




# # Test Data 1
# mark_weight = 92  # kg 
# mark_height = 1.95  # m 

# john_weight = 78  # kg 
# john_height = 1.69  # m 

# # Calculate BMI for Mark and John
# mark_bmi = mark_weight // (mark_height ** 2)
# john_bmi = john_weight // (john_height ** 2)

# # Check if Mark has a higher BMI than John
# mark_higher_bmi = mark_bmi > john_bmi


# print("Mark's BMI:", mark_bmi)
# print("John's BMI:", john_bmi)
# print("Mark has a higher BMI than John:", mark_higher_bmi)

# if mark_higher_bmi is True:
#     print(f"Mark's BMI {mark_bmi} is higher than John {john_bmi}")
# else:
#     print(f"John's BMI {john_bmi} is Higher than Mark {mark_bmi} ")


# # Test Data 2
# mark_weight = 95  # kg
# mark_height = 1.88  # m

# john_weight = 85  # kg
# john_height = 1.76  # m

# # Calculate BMI for Mark and John
# mark_bmi = mark_weight / (mark_height ** 2)
# john_bmi = john_weight / (john_height ** 2)

# # Check if Mark has a higher BMI than John
# mark_higher_bmi = mark_bmi > john_bmi

# print("Mark's BMI:", mark_bmi)
# print("John's BMI:", john_bmi)
# print("Mark has a higher BMI than John:", mark_higher_bmi)


# def fizz_buzz(input):
#   if (input % 5 == 0) and (input % 3 == 0):
#     return 'fizz_buzz'
#   if input % 3 == 0:
#     return 'fizz'
#   if input % 5 == 0:
#     return 'buzz'

# print(fizz_buzz(15))

# def my_function(food):
#     for x in food:
#       print(x)
  
# fruits = ['banaa', 'orange', 'mellons']

# my_function(fruits)

# CHECK AND CHANGE RECURSION LIMIT AND 
# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())


# def greet():
#   print('Hello')
#   greet()


# LAMBDA

add = lambda a, b: a+b
#print(add(2, 5))

adds = lambda *arg: sum(arg)
#print(adds(2, 5, 17, 20, 11))

addss = lambda x, y=20, z= 10: x*y+z
#print(addss(5))

addzz = lambda x, y,z: x*y/2
#print(addzz(z=3, x=10, y=5))

#FILTER WITH LAMBDA
num = [20, 25, 12, 30, 35, 33, 40, 46]
greater = list(filter(lambda num: num>30, num))

#print(greater)

numb = [20, 25, 12, 30, 35, 33, 40, 46]
divide = list(filter(lambda x:(x%4==0),numb))
#print(divide)

#MUTIPLICATION AND RAISE TO POWER
numbss = [20, 25, 12, 30, 35, 33, 40, 46]
multiply =  list(map(lambda x: (x*2), numbss))
#print(multiply)

numbs =[2, 5, 7, 4, 9, 8]
cube = map(lambda x:pow(x,3), numbs)
# print(list(cube))


#CLASSES

# class Person:
#   def __init__(self, name):
#    self.name = name
#   def talk(self):
#     print('talk')


# john = Person
# john.talk()

# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)

# class Person:
#   def __init__(self, **details):
#     self.personalDetails = details
  

# p1 = Person(name = 'Isaac', age = 35, town = 'Koforidua', yearBorn = 1987, workPlace = 'NIA')
# print(p1.personalDetails )

# class Person1:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"
  
# pss = Person1('John', 38)
# print(pss)


# class Personn:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
  
#   def myfunc(self):
#    return f"Hello! I am {self.name} and {self.age} years old"

# prr = Personn('John', 35)
# print(prr.myfunc())

# CALCULATE THE AREA OF RECTANGLE
# class Rectangle:
#   def __init__(self, height, width):
#     self.height = height
#     self.width = width
  
#   def rectangleArea(self):
#     return self.height * self.width

# area = Rectangle(15, 25)
# print(area.rectangleArea())

# class BankAccount:
#   def __init__(self, acct_number, balance):
#     self.acct_number = acct_number
#     self.balance = balance
  
#   def deposit(self, depoAmt):
#     self.balance += depoAmt
  
#   def withdrawal(self, wthAmt):
#     if self.balance >= wthAmt:
#       self.balance -=  wthAmt
#     else:
#       print('Insufficient Amount')
  
#   def get_balance(self):
#     return self.balance
  
# account =BankAccount(20155502, 1440)

# account.deposit(200)
# account.withdrawal(850)
# account.withdrawal(900)
# print(account.get_balance())  

class dog:
  def bark(self):
    print('bark')


