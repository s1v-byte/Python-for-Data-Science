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

