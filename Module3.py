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