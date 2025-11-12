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


