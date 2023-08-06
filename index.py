#STRINGS
# print("*" * 10)
#
# Name = "Isaac"
# Age = 30
# Is_New = True
# print(type(Name))
# print(type(Age))
# print(type(Is_New))

# triple_quotes = '''
# Hi Isaac your journey in learning
# python programming started and you are
# doing well keep it and continue working hard
# '''
# print(triple_quotes)

'''Same triple quotes can be used to comment
out a long expression
or notes in python'''

#extract using INDEX
extract = "python as a course"
# print(extract[:]) -- copy
#print(extract[0]) -- first letter
# print(extract[-1]) -- last letter
#print(extract[0:5]) -- range
#print(extract[3:])
#print(extract[:-3])

#FORMATTED STR
# firstName = "John"
# lastName = "Smith"
# fullName = f'{firstName} {lastName} is a coder'
# print(fullName)

#INPUTS
# name = input("What's your name? ")
# color = input("What's your favorite color? ")
# print(name + " likes " + color)

#TYPE CONVERSION
# int() -- converts str to int
# float() -- converts to float
# bool() -- converts to boolean

# weight_lbs = int(input("What's your weight in pounds? "))
# weight_kg = weight_lbs * 0.45
# print(weight_kg)

#STR METHODS(Refers to functions specific to an object or variable).
#strMethod = "Python for Beginners"
#print(strMethod.upper()) -- converts upper / lower case
#print(strMethod.find('Python')) --  finds the index of an item
#print('Python' in strMethod) -- using boolean statement to find the existence of an item
#print(strMethod.replace("Python", "Absolute Python")) Replaces item in an expression
#print(strMethod.title())

#ARITHMETIC OPERATORS

#'IF' STATEMENT

# House_price = 1000000
# has_good_credit = False
# if has_good_credit:
#     down_payment = House_price * 0.1
# else:
#     down_payment = House_price * 0.2
#
# print(f"Down Payment: {down_payment}")

# LOGICAL OPERATORS USED IN SITUATIONS TO COMBINE MULTIPLE INSTANCES
# AND, OR

# COMPARISON OPERATORS COMPARE VARIABLES WITH VALUES
# == >< !=

# name = input('Enter Full Name ')
# if len(name) < 3:
#     print('must exceed 3 characters')
# elif len(name) > 50:
#     print('must not exceed 50 characters')
# else:
#     print('name looks good')


# weight = int(input("what's your weight? "))
# unit = input("Enter measurement unit ")

# if unit == "kg":
#     weight_in_kilos = weight//0.45
#     print(f'you are {weight_in_kilos}lbs')
# else:
#     weight_in_lbs = weight * 0.45
#     print(f'you are {weight_in_lbs}kg')

# if weight == 120:
#     print(weight * 10)

# LIST
# friends = ["John", "Smith", "James", "Joseph", "Kabiru", "Issah"]
# Birth_years = [1978, 1999, 1987, 2000, 1998, 1992]
# friends.pop(4)
# print(friends)

# RANGE IN LIST

# start = 1
# end = 10
# numoo = range(start, end+1)
# print(list(numoo))

# friends = ["John", "Smith", "James", "Joseph", "Kabiru", "Issah"]
# for x in range(len(friends)):
#     print(x +1, friends[x])

# LIST COMPEHENSION
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)
 


#FUNCTIONS
# def say_hi(name, age):
#     print(f"Hello {name}, you are {age} years old")
#
# say_hi("James", 35)

#arguments(*args)
# def children(*kids):
#     print(f"Hello {kids[0:]}")
#
# children('Kofi', 'Samuel', 'Eugene', 'Emma', 'Yaa')

# keyword arguments (kwargs)
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child1)
#
# my_function(child1 = "Emil", child3 = "Linus", child2 = "Tobias")


#apply ** to the kwargs when the arguements to be received is known.
# def the_children(**kids):
#     print(f"The kids are {kids}")
#
# the_children(firstName = 'Sammy', lastName = 'Kofi', middleName = 'Eli')

#DEFAULT PARAMETER
# def my_function(country = "Norway"):
#   print("I am from " + country)

#my_function()
# my_function("Brazil")

# def my_function(x):
#     return 5 * x
# print(my_function(20))
# BUILDING A CALCULATOR
# num1 = int(input('Enter number '))
# operata = input('Enter operator ')
# num2 = int(input('Enter number '))
#
# if operata == '*':
#     answer = num1 * num2
#     print(answer)
# elif operata == '/':
#     answer = num1 / num2
#     print(answer)
# elif operata == '-':
#     answer = num1 - num2
#     print(answer)
# elif operata == '+':
#     answer = num1 + num2
#     print(answer)
# else:
#     print('error')

# #WHILE LOOP
# i = 0
# while i < 10:
#     i += 1
#     if i == 6:
#         continue
#     print(i)


'''personalInfor = [
  {
    "name": "marley", "age": 20, "address": {"country": "Ghana","zip_code": "+233","phoneNumbers": [7777777,900000]},
    "gender": "male","occupation": "developer",},
]'''

# Changing key value of a dict
# personalInfor[0]["occupation"] = "Dancer"
# print(personalInfor)


# APPLYING LOOPS IN dict
# for person in personalInfor:
#     print(person["name"], person["gender"], person["age"], person["occupation"], sep =",")

#eliminating white space and capitalizing each word
# first = input('Enter first Name ').strip().title()
# last = input('Enter last Name ').strip().title()
# print(first, last, end="") ----prints all arguments on same line
# print("Hello, \"friend\"") -- print to include quotes on str item

# FLOAT
# x = float(input('enter a number '))
# y = float(input('enter a number '))
# z = x + y
# print(round(x + y)) ---round to nearest figure
# print(f"{z:.2f}")


# CONDITIONAL 
# Using "match" "case" instead of "if" "else" CONDITIONAL 

# name = input("Enter Name ")
# match name:
#     case "Harry":
#         print("Boys room")
#     case "Eugene":
#         print("Boys Room")
#     case "Stella":
#         print("Girls Room")
#     case _:
#         print("Not Available")

# OTHERWAYS

# match name:
#     case "Harry" | "Eugene" | "Sammy":
#         print("Boys Room")
#     case "Stella":
#         print("Girls Room")
#     case _:
#         print("Not Available")


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
    'watermelon', 'xigua', 'yangmei', "okro"
]

fruitsss = ['Banana', 'orange', '1', 'XAear', 'Mango', 'sweetmon', '20']
vegetable = ['cabbage', 'onion', 'tomato', 'okro']
fruitsss.extend(vegetable)

def my_func(u):
  return len(u)


fruits.sort(key=my_func)



#TUPLES
thisset = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)




fruitsNew = ('apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya')
(a, b, *c) = fruitsNew
# print(a)
# print(b)
#print(*c)


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

# add = lambda a, b: a+b
# #print(add(2, 5))

# adds = lambda *arg: sum(arg)
# #print(adds(2, 5, 17, 20, 11))

# addss = lambda x, y=20, z= 10: x*y+z
# #print(addss(5))

# addzz = lambda x, y,z: x*y/2
#print(addzz(z=3, x=10, y=5))

#FILTER WITH LAMBDA
# num = [20, 25, 12, 30, 35, 33, 40, 46]
# greater = list(filter(lambda num: num>30, num))

# #print(greater)

# numb = [20, 25, 12, 30, 35, 33, 40, 46]
# divide = list(filter(lambda x:(x%4==0),numb))
# #print(divide)

# #MUTIPLICATION AND RAISE TO POWER
# numbss = [20, 25, 12, 30, 35, 33, 40, 46]
# multiply =  list(map(lambda x: (x*2), numbss))
# #print(multiply)

# numbs =[2, 5, 7, 4, 9, 8]
# cube = map(lambda x:pow(x,3), numbs)
# print(list(cube))

#CLASSES

# class Person:
#   def __init__(self, name): -------constructor // initializer
#    self.name = name ---------------properties

#   def talk(self): -----------------method
#     print('talk')

# john = Person --- instance
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


# class Human:
#   def __init__(self, name, color, height, age):
#     self.name = name
#     self.color = color
#     self.height = height
#     self.age = age
  
#   def __str__(self):
#     return(f"{self.name} {self.color} {self.height} {self.age}")

# print(beings.age)
# print(beings.color)
# print(beings.height)
# print(beings.name)

# beings = Human('Kwame', 'Black', 2.80, 25)
# print(beings)

# class Person:
#     def __init__(self, age, yearBorn):
#         self.age = age
#         self.year = yearBorn
    
#     def __str__(self):
#         return(f"I am {self.age} years old and born on {self.year}")
    
# details = Person(28, 1991)
# print(details)



# class Students:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def add_grade(self):
        

#MOLDULES

import random
# coin = random.choice(["head", "tail"])
# print(coin)

# number = random.randint(1, 10)
# print(number)

import statistics
# print(statistics.mean([54, 78]))

import sys
#argv ----arguement vector
#sys.exit --- lets you exit

# ERRORS
# IndexError --- items outside a range
#SyntaxError ---- occurs from incomplete arguements by the programmer

# CALCULATOR
# def main():
#     x = int(input("What is x? "))
#     print("x squared is", square(x))

# def square(n):
#     return n*n

# main()

# name = []
# for _ in range(3):
#     print(name.append(input("whats your name")))

# if not name // if name == ""


# RECURSION
# 5! means 5 factorial thats (5*4*3*2*1)

def recursive_factoral(n):
  if n < 0:
    return -1
  elif n < 2:
    return 1
  else:
     return (n * recursive_factoral(n - 1))

# print(recursive_factoral(10))

class Person():
  def __init__(self, num1, operand, num2):
    self.num1 = num1
    self.operand = operand
    self.num2 = num2

  def function(self):
    self.num1 = int(input("_"))
    self.operand = input("_")
    self.num2 = int(input("_"))
    
    if self.operand == '*':
      return  self.num1 * self.num2 
    elif self.operand == '/':
      return  self.num1 / self.num2 
    elif self.operand == '+':
      return  self.num1 + self.num2 
    elif self.operand == '-':
      return  self.num1 - self.num2
    else:
      return("Invalid data")

x = Person(2,'*',6)
# print(x.function())


class Person1():
  def __init__(self, first, last, age):
    self.fname = first
    self.lname = last
    self.age = age

  def __str__(self):
    return (f"{self.fname} {self.lname} {self.age}")

details = Person1("Joshua", "Ishmael", 35)
# print(details)

#FILE SYSTEM

data = open("work/demo.txt", "rt")
x = data.readlines()

# print(x)

# with open("work/demo.txt", "rt") as data:
#     for i, line in enumerate(data, 1):
#         if i == 3:
#             print(line)
#             break



# myFile = Open("work/demo.txt", "a")
# myFile.write("hay people")
# myFile.closed()

# myFile = Open("work/demo.txt", "a")
# print(myFile.read())
# myFile.closed()


# APPNDED(Adds up to the existing content)
# jak = open("work/demo.txt", "a")
# jak.write("\nKwame NKrumah is a genius")
# jak.closed()


# WRITE(clears content of existing file and adds the new)
# jak = open("work/demo.txt", "w")
# jak.write("Nana Addo is president")
# jak.close()

# print(open("work/demo.txt", "r").read())









