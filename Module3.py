#Conditions and Branching
#If else
age = 12
if (age>18):
    print("enter")
else: 
    print("You may not enter")
print("Move along")
#Output 
#You may not enter
#Move along

#ELIF 
age = 18
if (age>18):
    print("enter")#if 18 up enter
elif(age==18): #if 18 free candy and enter
        print("u r 18 so enter with free candy")
elif(age==0): 
        print("why is ur age 0?")
else:
    print("You are too young")
print("Move along")
#Output
#u r 18 so enter with free candy
#Move along

#OR
age = 6
if (age < 5) or (age >5):
    print("ur less")
elif(age == 5):
    print("ur 5")
else:
    print("ur more")
#OUTPUT = ur more

#AND
year = 1983
if (year > 1979) and (year <1990):
    print("this year was made in the 80s")
else:
    print("this year is either less than 1979 or greater than 1990")
#OUTPUT = this year was made in the 80s

#LEARNINGS:
#elif - else if shortcut and usually placed under the first if
#LOGICAL OPERATORS = and , or , not (!)

#-----------------------LOOPS-------------------------
#FOR LOOPS = repeat something a certain number of times
A=[3,4,5]
for i in A:
     print(i)
#OUTPUT = 3
#       = 4
#       = 5

#RANGE
for i in range(5):
    print(i)
#OUTPUT = 0 1 2 3 4 


for i in range(0, 5):
    print(i)
#OUTPUT = 0 1 2 3 4 


for i in range(3, 5):
    print(i)
#OUTPUT = 3 4 


squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])
#OUTPUT:
    """
Before square  0 is red
After square  0 is white
Before square  1 is yellow
After square  1 is white
Before square  2 is green
After square  2 is white
Before square  3 is purple
After square  3 is white
Before square  4 is blue
After square  4 is white
    """

#FOR LOOP x length
dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])     
#OUTPUT = 
"""
1982
1980
1973
"""

#WHILE LOOPS = conditional
x=11
y=1
while(y != x): # <---- print Y if Y is not == x (11) stop till reach 11
    print(y) #PRINT Y
    y=y+1 #Y + 1
#Output = 1
#       = 2
# "" "" "" 
#       = 10  <---- HANGGANG 10 LANG UNG PRINT NYA SINCE 11=11

#Basic while Loop
i = 1
while i <= 5:
    print(i)
    i += 1
#Output 
"""
1
2
3
4
5
"""

#While loop but infinite if no breaks
x = 1
while x <= 10:
    print(x)
    if x == 5:
        break      # exits loop even though condition is True
    x += 1
#Output: 12345

#While loop skipping values
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue   # skip printing 3
    print(x)
#Output: 1245

#with else
x = 1

while x < 3:
    print(x)
    x += 1
else:
    print("Loop finished normally")
#Output: 1,2 Loop finshed normally

#NESTED WHILE LOOP
i = 1
while i <= 3:
    j = 1
    while j <= 2: #<-------- PRIORITIZED SI NESTED MATASPOS BAGO I PRINT UNG MAIN WHILE
        print(i, j)
        j += 1
    i += 1
#Output:  
"""
1 1
1 2
2 1
2 2
3 1
3 2
"""
#While loop STRING INPUT
password = ""

while password != "secret":
    password = input("Enter password: ")

print("Access granted!")
#Output: Enter Password: 

#------------------------- FUNCTIONS--------------------------
#len is a function 
#similar to len, sum is a function because it adds the values
#same as sorted are sort
"""
code above are sum() sorted() but .sort()
"""
#Basic Function
def add1(a): #<--- add1 is a variable name, more like function name, def means define
    b=a+1    #<--- formula for add1, so pag tinawag add1, that indentation will form no matter what
    return b #<--- anything that is inside the indent is a formula for the variable
c = add1(10) #<--- OUTSIDE the indentation, defines the VALUE of add1, which is (10)
print(c) #OUTPUT: 11     #Since b=10+1

#Basic function - Multiply
def Mult(a,b):
    c=a*b
    return c
d = Mult(2,2.4) #<---- Pwede int and float at the same time
print(d)
#Output: 4.8

#Basic function - Int + string
def Mult(a,b):
    c=a*b
    return c
d = Mult(2,"hehe-") #<---- 2*"hehe-" = hehe-hehe-
print(d)
#Output: hehe-hehe

#Basic function - String only and no RETURN cuz string no need
def MJ():
    print("MICHAEL JACKSON")
    #no RETURN but it outputs: None
mjay = MJ()
print(mjay)
#output: MICHAEL JACKSON None

#A "STATIC" FUNCTION because this function does nothing
def MJ():
    pass
    return None
    #pass and return None are same method (to let the function do nothing)
s = MJ()
print(s)

#Multiple tasks Function:
def add1(a):
    b=a+1
    print(a,"plus 1 equals",b)
    return b
sum1 = add1(2)
print(sum1)
#Output: 2 plus 1 equals 3 3 <-- two 3 cuz i printed the sum1

#USING LOOP IN FUNCTION
def printStuff(Stuff):
    for i, s in enumerate(Stuff):
        print("Album", i, "Rating is ",s)
album_ratings = ["HELLO", 12,2]
printStuff(album_ratings)
#output:
"""
Album 0 Rating is  HELLO
Album 1 Rating is  12
Album 2 Rating is  2
"""

#GLOBAL SCALE FUNCTION
def AddDC(x): 
    x=x+"DC" #<---- LOCAL SCOPE
    print(x) #Prints the function <---- LOCAL SCOPE
    return(x) #<--- LOCAL SCOPE
x = "AC" #Define the X   <---- GLOBAL SCOPE
z = AddDC(x) #Calls the FUNCTION <GLOBAL SCOPE
#Output: ACDC

#LOCAL Variable Scale
def PinkFloyd(x):
    global Claimsales
    Claimsales = "45 Million"
    return Claimsales
PinkFloyd("required may value")
print(Claimsales)
#Output: 45 million

#---------------Object and Classes-------------
#Basic Class And Object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create objects
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1.name, p1.age)
print(p2.name, p2.age)

#Class, object, METHODS
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    #Method
    def bark(self):
        print(f"{self.name} is barking!") #<--Method

dog1 = Dog("Max", "Labrador")
dog1.bark()

#Class with Getters and Setters:
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_speed(self, new_speed):
        self.speed = new_speed

car = Car("Toyota", 120)
print(car.get_speed())
car.set_speed(150)
print(car.get_speed())

#With if else
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} by {self.owner}. New balance: {self.balance}")
        else:
            print("Not enough money!")
            
acc1 = BankAccount("John", 1000)
acc2 = BankAccount("Sarah", 500)

acc1.deposit(200)   # John now has 1200
acc2.withdraw(300)  # Sarah now has 200
#Output: Deposited 200. New balance: 1200
#        Not enough money!

#LIBRARY CONCEPT ----------------
class Book:
    
    def __init__(self, title, author, year, available):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        
    def borrow(self):
        if self.available:
            self.available = False
            print(f"\nYou borrowed: {self.title}")
        else:
            print(f"Sorry, {self.title} is not available.")
        
    def return_book(self):
        self.available = True
        print(f"\n  You returned: {self.title}")
        
class Library:
    
    # SHELVES
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_available_books(self):
        print("\nAvailable books:")
        for book in self.books:
            if book.available:
                print(f"- {book.title} ({book.year})")
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print("Book not found in library.")
    
    # NEW: return_book method
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()  # Call the Book's method
                return
        print("Book not found in library.")


# Create library and add books
library = Library() 
        
# Create books
Book1 = Book("The Hobbit", "Tolkien", 1937, True)
Book2 = Book("Dune", "Frank Herbert", 1965, True)

library.add_book(Book1)
library.add_book(Book2)

# List books
library.list_available_books()

# Borrow a book
library.borrow_book("Dune") 

# List again to confirm it was borrowed
library.list_available_books()

# Return a book
library.return_book("Dune")

# List again to confirm it is available
library.list_available_books()

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}")


def print_all_students(student_list):
    for student in student_list:
        student.display_info()


# --- Main Program ---
s1 = Student("Alice", 85)
s2 = Student("Bob", 92)
s3 = Student("Charlie", 78)

students = [s1, s2, s3]

print_all_students(students)
