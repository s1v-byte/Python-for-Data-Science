"""
Learning Objectives
In this lesson you will learn about:
Reading files with open
Writing files with open
Loading data with Pandas
Working with and Saving data with Pandas
"""

#-------------------------

        #READING

#Reading Line 1 of the file:
with open ("testing.txt", "r")as read1:
    print(read1.readline())

    #Reading All Lines of the file:    
with open ("testing.txt", "r") as read1:
    print(read1.readlines()) #BUT TURNS ALL CONTENTS INTO LISTS FORMAT

    #Reading but INDEX specify and IT CONTINUES THE index count
with open("testing.txt", "r") as read1: #This is line 1
    print(read1.readline(4)) #prints this
    print(read1.readline(8)) #prints  is line 
    
#Reading Files with Open using For loop
with open ("testing.txt","r") as readfile:
    for line in readfile:
        print(line)
#--------------------------

            #WRITING

#Writing with multiple lines
with open("testing2.txt", "w") as File2:
    File2.write("This is line A")
    File2.write("\n This is line B")
    File2.write("\nThis is line 3")

# Iterate through the lines using for loop
with open("testing.txt","r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
print("\n")

#Output
"""
Iteration 0 :  this is line 1

Iteration 1 :  line 2

Iteration 2 :  line 3
"""

    #Iterate but in a clean way
with open("testing.txt", "r") as file1:
    for i, item in enumerate(file1):
        print(f"Line {i}: {item}", end="")


#Writing using LISTS and FOR LOOP
Lines = ["This is 1\n", "This is 3\n", "This is 3\n"]
with open("testing2.txt", "w") as File2:

    for line in Lines:
        File2.write(line)

#Writing Files by Converting floats,ints in the lists into STRINGS
Lists = [
    "Product", "Quantity", "Price",
    "Apple", 10, 0.50
]

with open("sales_raw.txt", "w") as File1:
    for item in Lists:
        File1.write(str(item) + "\n")  # convert to string + newline
    print("file has been created")


#Writing file by using append (Adding a Data in last)
with open("testing2.txt", "a")as File2:
    File2.write("\nThis is append")
    

#Copying existing file into a new file
with open("testing3.txt", "r") as readfile:
    with open("testing4.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)