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