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

#Strings: IMMUTABLE
Artist = "Michael Jackson"
print(Artist.replace("Michael", "Miku")) #Replace Michael with Miku
#Output = Miku Jackson

#-----------------------TUPPLES-----------------------
#Tupples
Tuple1 = ("disco", 1, 2.3) #any types that inside the parenthesis () can exist
print(Tuple1[0], Tuple1[-1])
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
print(Tuple2, Tuple3, "Length: ",len(Tuple1))
#Output = ("disco", 1, "bar", .2) ("bar", .2, 4) "Length: 4"

#https://apps.cognitiveclass.ai/learning/course/course-v1:CognitiveClass+PY0101EN+v3/block-v1:CognitiveClass+PY0101EN+v3+type@sequential+block@2d204ac4fa3143048a998da7e53702d7/block-v1:CognitiveClass+PY0101EN+v3+type@vertical+block@bc103d3618c54b20891e959ff7e8842b
Ratings = (10,"9", 6)
print(Ratings.replace("9", "Re"))
