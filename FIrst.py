print("Michael Jackson")
print("MIKU \t JACKSON") #inputs TAB
print("MIKU \nJACKSON") #inputs a new paragraph

#String
Artist = "Michael Jackson"
Singer = Artist[0]
print("String: "+Singer)
#Output = M 

#String Different kind of print
Artist = "Michael Jackson"
print("String result:",Artist[3])
#Output = 3 <-- starts at 0

#String but negative
Artist = "Michael Jackson"
print("Negative String: "+Artist[-15])
#output = M

#String:Slicing
Artist = "Michael Jackson"
print("Slicing: "+Artist[8:15])
#output = Mich

#String:Stride keeps the cut version
Artist = "M1iscahaaaesl"
print("Slicing: "+Artist[::2]) #Cut the text into 3 texts
#output = Mhlas

#TUPLES: SLICING 
Artist = "Michael Jackson"
print("Length:",Artist,len(Artist)) #len determines the length of the character
#Output = 15

#Len Determining how many elements, not index by using length
Names = "Michael Jackson", "dave"
Totalnames = (Names)
print ("len used for determining elemends and not index:", len(Totalnames))

#Strings: IMMUTABLE
Artist = "Michael Jackson"
print("\n","\n",Artist.replace("Michael", "Miku")) #Replace Michael with Miku
#Output = Miku Jackson

#-----------------------TUPPLES-----------------------
#Tupples
Tuple1 = ("disco", 1, 2.3) #any types that inside the parenthesis () can exist
print("\n",Tuple1[0], Tuple1[-1])
#Output = disco 2.3

#Combining Tupples
Tuple1 = ("disco", 1, 23)
Tuple2 = Tuple1 + ("bar", 2, 24)
print(Tuple2)
#Output "disco", 1, 23, "bar", 2, 24

#SLICING TUPPLES
Tuple1 = ("disco", 1, "bar", .2, 4)
Tuple2 = Tuple1[0:4]
Tuple3 = Tuple1[2:5]
print("\n",Tuple2, Tuple3, "Length: ",len(Tuple1))
#Output = ("disco", 1, "bar", .2) ("bar", .2, 4) "Length: 4"

#Tupples add tupples
omg = ("dave", 1, "john",2,3,4,5,6) #len value = 8
wa = "sads"
sad =  omg + (wa,)
print(sad, len(sad))
#Output = (("dave", 1, "john",2,3,4,5,6, "sads") 9

#Nested Tupples
tuples1 = (1,2,3,("four", "five","seven","eight","nine"),(4,5))
tuples2 = tuples1[3][2]
print(tuples2,"length:",len(tuples2))#Select from index 3 and collect value 2(seven) slice by 2
#Output 5

#Tupples LISTS
tuples1 = [1,2,3,["four", "five"],["six", "seven"],[4,5]]
print(tuples1[3])
#Output = ["four", "five"]

#Tupples Lists Extend
tuples1 = [1,2,3,["four", "five"],["six", "seven"],[4,5]]
tuples1.extend(["HELLO"])
print(tuples1[6][:3])
#Output = HEL

#Tupples List muttable (change)
tuples1 = [1,2,3,["four", "five"],["six", "seven"],[4,5]]
tuples1[3] = "FOUR"
print(tuples1)
#Output = [1, 2, 3, 't', ['six', 'seven'], [4, 5]]

#delete 
tuples1 = [1,2,3,["four", "five"],["six", "seven"],[4,5]]
del tuples1[1]     # removes the element at index 1
print(tuples1)
#Output = [1, 3, ['four', 'five'], ['six', 'seven'], [4, 5]]

#Seperate strings into seperate character
tuples1 = "a,b,c,d" #Data should already have , each index lol
tuples2 = tuples1.split(",")
tuples3 = tuples2 + [3]
print(tuples3)
#Output = ['a', 'b', 'c', 'd', 3]